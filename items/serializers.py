from urllib.parse import urlparse

from items.models import Cake
from rest_framework import serializers


def yum_factor_check(value: int):
    if value > 5 or value < 1:
        raise serializers.ValidationError('This field must be between 1-5')


def check_url(value: str):
    try:
        result = urlparse(value)
        if not all([result.scheme, result.netloc]):
            raise Exception
    except Exception:
        raise serializers.ValidationError('field needs to be a url.')


class CakeSerializer(serializers.Serializer):
    name = serializers.CharField()
    comment = serializers.CharField()
    image_url = serializers.CharField(
        max_length=200, validators=[check_url], label="imageUrl"
    )
    yum_factor = serializers.IntegerField(
        label="yumFactor", validators=[yum_factor_check]
    )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        image_url = data.pop('image_url')
        yum_factor = data.pop('yum_factor')
        data.update(yumFactor=yum_factor, imageUrl=image_url)
        return data

    def to_internal_value(self, data):
        data = data.dict()
        yum_factor = data.pop('yumFactor')
        image_url = data.pop('imageUrl')
        data['image_url'] = image_url
        data['yum_factor'] = yum_factor
        return super().to_internal_value(data)

    def create(self, validated_data: dict):
        return Cake.objects.create(**validated_data)
