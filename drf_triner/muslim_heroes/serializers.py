from rest_framework import serializers
from .models import Heroes


# class HeroesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Heroes
#         fields = ("name", "image", "category", "gender")

class HeroesSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    image = serializers.ImageField()
    description = serializers.CharField()
    category = serializers.CharField()
    gender = serializers.CharField()
    birth_date = serializers.DateField()
    death_date = serializers.DateField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
