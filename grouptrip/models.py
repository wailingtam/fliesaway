from django.db import models
from django.contrib.auth.models import User, Group


# Create your models here.
# class UserProfile(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    trips = models.ManyToManyField(Group)

    food = models.BooleanField(default=False)
    sports = models.BooleanField(default=False)
    monuments = models.BooleanField(default=False)
    party = models.BooleanField(default=False)
    relax = models.BooleanField(default=False)

    # representation of the object
    def __str__(self):
        return self.user.username


class TripPreference(models.Model):
    trip = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    budget = models.IntegerField(blank=False)
    WEATHER_CHOICES = (
        ('SUNNY', 'Sunny'),
        ('CLOUDY', 'Cloudy'),
        ('RAINY', 'Rainy'),
        ('SNOWY', 'Snowy'),
        ('ANY', 'Any'),
    )
    weather = models.CharField(max_length=6,
        choices=WEATHER_CHOICES,
        default = 'ANY')
    duration = models.IntegerField(blank=False)

    unique_together = ('trip', 'user')

    def __str__(self):
        return self.trip.name + "-" + self.user.username


class Destination(models.Model):
    trip = models.ForeignKey(Group, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.trip.name + "-" + self.city
