from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer

class ProfilesList(generics.ListAPIView):

    # This gets the serialiser information to display 
    serializer_class = ProfileSerializer

    queryset = Profile.objects.all()