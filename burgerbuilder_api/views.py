from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token

from burgerbuilder_api import serializers
from burgerbuilder_api import permissions
from burgerbuilder_api import models


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('email',)

    @action(methods=['put'], detail=True, serializer_class=serializers.PasswordSerializer, 
    permission_classes=[permissions.IsSuperuserOrIsSelf], url_path='change-password', url_name='change_password')
    def set_password(self, request, pk=None):
        serializer = serializers.PasswordSerializer(data=request.data)
        user = self.get_object()
        if serializer.is_valid():
            if not user.check_password(serializer.data.get('old_password')):
                return Response({'old_password': ['Wrong password.']}, 
                                status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            user.set_password(serializer.data.get('new_password'))
            user.save()
            return Response({'status': 'password set'}, status=status.HTTP_200_OK)

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        response = super(UserLoginApiView, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})


class IngredientsViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating ingredients items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.IngredientsSerializer
    queryset = models.Ingredients.objects.all()
    permission_classes = (permissions.IsSuperuserOrIsSelf,)


class IngredientsViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating ingredients items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.IngredientsSerializer
    queryset = models.Ingredients.objects.all()
    permission_classes = (permissions.IsSuperuserOrIsSelf,)


class ContactDataViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating contact data"""
    uthentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ContactDataSerializer
    queryset = models.ContactData.objects.all()
    permission_classes = (permissions.IsSuperuserOrIsSelf,)


class OrderViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating Orders data """
    uthentication_classes = (TokenAuthentication,)
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()
    permission_classes = (permissions.IsSuperuserOrIsSelf,)