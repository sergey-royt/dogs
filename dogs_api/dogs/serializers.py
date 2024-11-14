from rest_framework.serializers import HyperlinkedModelSerializer

from dogs_api.dogs.models import Dog, Breed


class DogSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Dog
        fields = "__all__"


class BreedSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Breed
        fields = "__all__"
