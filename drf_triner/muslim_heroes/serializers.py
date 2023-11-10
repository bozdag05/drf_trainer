from rest_framework import serializers
from .models import Heroes


class HeroesSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Heroes
        fields = "__all__"
#
# class HeroesSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=200)
#     image = serializers.ImageField(read_only=True)
#     description = serializers.CharField()
#     category_id = serializers.CharField()
#     gender_id = serializers.CharField()
#     birth_date = serializers.DateField()
#     death_date = serializers.DateField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#
#     def create(self, validated_data):
#         return Heroes.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.description = validated_data.get("description", instance.description)
#         instance.category = validated_data.get("category", instance.category)
#         instance.gender = validated_data.get("gender", instance.gender)
#         instance.birth_date = validated_data.get("birth_date", instance.birth_date)
#         instance.death_date = validated_data.get("death_date", instance.death_date)
#         instance.time_update = validated_data.get("time_update", instance.time_update)
#         instance.is_published = validated_data.get("is_published", instance.is_published)
#         instance.save()
#         return instance
