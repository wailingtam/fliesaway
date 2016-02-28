from rest_framework import serializers
from django.contrib.auth.models import User, Group
from rest_framework import generics

from .models import UserProfile, Destination, TripPreference


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'name')

    def create(self, validated_data):
        group = Group(
            name=validated_data['name']
        )
        group.save()
        return group


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'trips', 'food', 'sports', 'monuments', 'party', 'relax')

    def create(self, validated_data):
        user_profile = UserProfile(
            user = User.objects.get(pk=validated_data['user']),
            food = validated_data['food'],
            sports = validated_data['sports'],
            monuments = validated_data['monuments'],
            party = validated_data['party'],
            relax = validated_data['relax']
        )
        user_profile.save()
        return user_profile
#     pk = serializers.IntegerField(read_only=True)
#     spotify_username = serializers.CharField(required=False, allow_blank=True, max_length=50)


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ('id', 'city', 'votes', 'trip')

    def create(self, validated_data):
        destination = Destination(
            city=validated_data['city'],
            votes=validated_data['votes'],
            trip=Group.objects.get(pk=validated_data['trip'])
        )
        destination.save()
        return destination


class TripPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripPreference
        fields = ('id', 'trip', 'user', 'budget', 'duration')

    def create(self, validated_data):
        trip_preference = TripPreference(
            trip=Group.objects.get(pk=validated_data['trip']),
            user=User.objects.get(pk=validated_data['user']),
            budget=validated_data['budget'],
            duration=validated_data['duration']
        )
        trip_preference.save()
        return trip_preference
