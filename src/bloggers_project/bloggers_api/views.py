from django.shortcuts import render
from rest_framework import filters, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly # for users logged in or not
from rest_framework.permissions import IsAuthenticated #strictly logged in users

from . import models, permissions, serializers

# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
	''' Handles the view of blogger's profile, 
		it handles the CRUD as it is the ModelViewSet'''
	
	serializer_class = serializers.UserProfileSerializer
	queryset = models.UserProfile.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes =(permissions.UpdateOwnProfile,)
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name', 'email')


class LoginViewSet(viewsets.ViewSet):
	''' Handles the view of blogger's login entry, 
	it handles the CRUD as it is the ModelViewSet
	'''
	
	#provides a unique token for each login session
	serializer_class = AuthTokenSerializer

	def create(self, request):
 
		return ObtainAuthToken().post(request)


class UserProfileFeedViewSet(viewsets.ModelViewSet):

	''' Handles the view of blogger's blog updates, 
		it handles the CRUD as it is the ModelViewSet'''

	authentication_classes = (TokenAuthentication,)
	serializer_class = serializers.ProfileFeedSerializer
	queryset = models.ProfileFeedItem.objects.all()
	permission_classes =(permissions.PostOwnStatus, IsAuthenticatedOrReadOnly)

	def perform_create(self, serializer):
		'''sets the user profile to the logged in user'''

		serializer.save(user_profile=self.request.user)
	
  