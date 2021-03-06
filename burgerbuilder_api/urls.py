from django.urls import path, include
from rest_framework.routers import DefaultRouter

from burgerbuilder_api import views

router = DefaultRouter()
router.register('profiles', views.UserProfileViewSet) 
router.register('ingredients', views.IngredientsViewSet)
router.register('contact-data', views.ContactDataViewSet)
router.register('orders', views.OrderViewSet)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]