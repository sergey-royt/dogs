from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Breed(models.Model):
    TINY = "T"
    SMALL = "S"
    MEDIUM = "M"
    LARGE = "L"
    SIZE_CHOICES = [
        (TINY, "Tiny"),
        (SMALL, "Small"),
        (MEDIUM, "Medium"),
        (LARGE, "Large"),
    ]

    INT_VALIDATOR_MIN_1_MAX_5 = [MinValueValidator(1), MaxValueValidator(5)]

    name = models.CharField(max_length=255)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    friendliness = models.IntegerField(validators=INT_VALIDATOR_MIN_1_MAX_5)
    trainability = models.IntegerField(validators=INT_VALIDATOR_MIN_1_MAX_5)
    shedding_amount = models.IntegerField(validators=INT_VALIDATOR_MIN_1_MAX_5)
    exercise_needs = models.IntegerField(validators=INT_VALIDATOR_MIN_1_MAX_5)

    def __str__(self) -> models.CharField:
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.PROTECT)
    gender = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    favorite_food = models.CharField(max_length=255)
    favorite_toy = models.CharField(max_length=255)

    def __str__(self) -> models.CharField:
        return self.name
