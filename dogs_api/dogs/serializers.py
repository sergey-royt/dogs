from rest_framework.serializers import ModelSerializer

from dogs_api.dogs.models import Dog, Breed


class DogSerializer(ModelSerializer):
    class Meta:
        model = Dog
        fields = "__all__"


class BreedSerializer(ModelSerializer):
    class Meta:
        model = Breed
        fields = "__all__"
