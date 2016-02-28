from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from .serializers import UserSerializer, GroupSerializer, DestinationSerializer, UserProfileSerializer, TripPreferenceSerializer
from .models import Destination, UserProfile, TripPreference
# Create your views here.


def index(request):
    return HttpResponse("aloha")


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class TripPreferenceViewSet(viewsets.ModelViewSet):
    queryset = TripPreference.objects.all()
    serializer_class = TripPreferenceSerializer
