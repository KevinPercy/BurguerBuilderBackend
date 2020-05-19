from rest_framework import serializers
from burgerbuilder_api import models


class UserProfileSerializer(serializers.ModelSerializer):
    """serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'password')
        extra_kwargs = {
            'password':{
                'write_only': True,
                'style': {'input_type':'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],            
            password=validated_data['password']
        )

        return user