from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import viewsets

from dogs_api.dogs.models import Dog, Breed
from dogs_api.dogs.serializers import DogSerializer, BreedSerializer


class DogList(APIView):
    def get(self, request, format=None):
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DogDetail(APIView):
    @staticmethod
    def get_dog(pk):
        try:
            return Dog.objects.get(pk=pk)
        except Dog.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dog = self.get_dog(pk)
        serializer = DogSerializer(dog)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dog = self.get_object(pk)
        serializer = DogSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dog = self.get_object(pk)
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BreedList(viewsets.ViewSet):
    def list(self, request):
        queryset = Breed.objects.all()
        serializer = BreedSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BreedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class BreedDetail(viewsets.ViewSet):
    @staticmethod
    def get_breed(pk=None):
        queryset = Breed.objects.all()
        return get_object_or_404(queryset, pk=pk)

    def retrieve(self, request, pk=None):
        breed = self.get_breed(pk)
        serializer = BreedSerializer(breed)
        return Response(serializer.data)

    def update(self, request, pk=None):
        breed = self.get_breed(pk)
        serializer = BreedSerializer(breed, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        breed = self.get_breed(pk)
        breed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
