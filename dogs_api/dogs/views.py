from typing import Any

from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response

from dogs_api.dogs.models import Dog, Breed
from dogs_api.dogs.serializers import DogSerializer, BreedSerializer


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

    def destroy(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Delete breed if there are no dogs"""

        breed = self.get_object()
        if breed.dogs.count() > 0:
            return Response("Breed has dogs", status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, *args, **kwargs)
