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
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    comment = serializers.CharField()
    imageUrl = serializers.CharField(
        max_length=200, validators=[check_url], source="image_url"
    )
    yumFactor = serializers.IntegerField(
        source="yum_factor", validators=[yum_factor_check]
    )

    def create(self, validated_data: dict):
        return Cake.objects.create(**validated_data)
