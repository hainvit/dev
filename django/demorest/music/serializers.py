"""
Import packages
"""
from rest_framework import serializers

from .models import MusicModel


class MusicSerializer(serializers.Serializer):
    id = serializers.CharField(required=False)
    name = serializers.CharField()
    email = serializers.CharField()

    def create(self, validated_data):
        return MusicModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
