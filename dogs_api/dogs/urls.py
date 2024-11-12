from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from dogs_api.dogs import views


router = DefaultRouter()
router.register(r"breeds", views.BreedList, basename="breed-list")
router.register(r"breeds", views.BreedDetail, basename="breed_detail")

urlpatterns = [
    path("dogs/", views.DogList.as_view()),
    path("dogs/<int:pk>/", views.DogDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += router.urls
