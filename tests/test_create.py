import pytest
from django.test import TestCase
from items.models import Cake
from django.test import Client
from django.urls import reverse
from typing import List

from items.serializers import CakeSerializer
client = Client()

BASE_PAYLOAD = dict(
	name='test_name',
	comment = 'my comment',
	imageUrl = 'http://www.google.com',
	yumFactor = 5
)

def changed_payload(change: dict, key_to={}) -> dict:
	data = dict(**BASE_PAYLOAD)
	data.update(change)

	for key_from, _key_to in key_to.items():
		value = data.pop(key_from)
		data[_key_to] = value

	return data

@pytest.mark.parametrize(
	'payload, change, status, error',
	(
		[changed_payload, {}, 200, {}],
		[
			changed_payload,
			dict(yumFactor=6),
			400,
			dict(yum_factor=['This field must be between 1-5'])
		],
		[
			changed_payload,
			dict(imageUrl='google'),
			400,
			dict(image_url=['field needs to be a url.'])
		],
	)
)
@pytest.mark.django_db
def test_create_valid(payload, change, status, error):
	response = client.post(reverse('add-cake'), payload(change))
	assert response.status_code == status
	if response.status_code != 200:
		assert response.json() == error


@pytest.mark.django_db
def test_delete_cakes():
	cake = Cake.objects.create(**changed_payload({}, key_to=dict(imageUrl='image_url', yumFactor='yum_factor')))
	assert Cake.objects.count() == 1
	response = client.delete(reverse('delete-cake', kwargs=dict(pk=cake.pk)))
	assert response.status_code == 204
	assert Cake.objects.count() == 0

@pytest.mark.django_db
def test_delete_fail_cakes():
	# test what happens when the object to delete doesnt exist
	assert Cake.objects.count() == 0
	response = client.delete(reverse('delete-cake', kwargs=dict(pk=7)))
	assert response.status_code == 404
	assert response.json() == dict(detail= 'Not found.')


@pytest.mark.django_db
def test_get_all_cakes():
	data = changed_payload({}, key_to=dict(imageUrl='image_url', yumFactor='yum_factor'))
	[Cake.objects.create(**data) for i in range(7)]
	assert Cake.objects.count() == 7
	response = client.get(reverse('all-cake'))
	returned = response.json()
	assert len(returned) == 7
	assert returned[0].get('yumFactor') == 5
	assert 'imageUrl' in returned[0]
	assert 'yumFactor' in returned[0]
