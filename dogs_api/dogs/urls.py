from django.urls import path, include
from rest_framework.routers import DefaultRouter

from dogs_api.dogs import views


router = DefaultRouter()
router.register(r"breeds", views.BreedViewSet)
router.register(r"dogs", views.DogViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
