from django.contrib import admin

from burgerbuilder_api import models

admin.site.register(models.UserProfile)
admin.site.register(models.Ingredients)
admin.site.register(models.ContactData)
admin.site.register(models.Order)


