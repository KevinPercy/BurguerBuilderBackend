from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    
    def create_user(self, email, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email) # takes care of the second half     
        user =  self.model(email=email)   

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and save a new superuser with given details """
        user = self.create_user(email, password)

        user.is_superuser = True
        user.is_staff = True
        
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique= True)
    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    
    def __str__(self):
        """Return the string representation of our user"""
        return self.email


class Ingredients(models.Model):
    """The burger ingredients"""
    ingredient = models.CharField(max_length=10)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        """return the models as a string"""
        return self.ingredient

class ContactData(models.Model):
    """The order contact data"""
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    street =  models.CharField(max_length=100)
    country = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=6)
    deliveryMethod = models.CharField(max_length=10)
    def __str__(self):
        """return the models as a string"""
        return '{} {}'.format(self.name, self.email)
    

class Order(models.Model):
    """The burger builder orders list"""
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    contact_data_id = models.ForeignKey(ContactData, on_delete=models.CASCADE)
    salad = models.PositiveIntegerField()
    bacon = models.PositiveIntegerField()
    cheese = models.PositiveIntegerField()
    meat = models.PositiveIntegerField()
    price = models.FloatField()

    def __str__(self):
        """return the models as a string"""
        return 'Order: {} {} {} {} {} '.format(self.salad, self.bacon, self.cheese, self.meat, self.price)




