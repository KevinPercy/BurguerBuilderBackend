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

class PasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class IngredientsSerializer(serializers.ModelSerializer):
    """Serializer of Ingredients Model"""
    
    class Meta: 
        model = models.Ingredients
        fields = ('id', 'ingredient', 'quantity')


class ContactDataSerializer(serializers.ModelSerializer):
    """Serializer of Contact data Model"""

    class Meta:
        model = models.ContactData
        fields = ('id','name', 'email', 'street', 'country', 'zip_code', 'delivery_method')

class OrderSerializer(serializers.ModelSerializer):
    """Serializer of Order data model"""

    class Meta:
        model = models.Order
        fields = ('id', 'user_id', 'contact_data_id', 'salad', 'bacon', 'cheese', 'meat', 'price')
        # extra_kwargs = {
        #     'user_id':{
        #         'read_only':True
        #     },
        #     'contact_data_id':{
        #         'read_only':True
        #     }
        # }




    