from django.contrib.auth.models  import User
from .serializers import RegistrationSerializer , ProfileSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from users.models import Profile
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from .permissions import IsProfileOwnerOrReadOnly

@api_view(['POST' ,])
def registration(request):
    if request.method =='POST':
        serializer = RegistrationSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['Response'] = "Registration was successful"
            data['username'] = account.username
            data['email'] = account.email
            token = Token.objects.get(user = account).key
            data['token'] = token
        else :
            data = serializer.errors
        return Response(data , status = status.HTTP_201_CREATED)

@api_view(['POST' ,])
def logout(request):
    if request.method =='POST':
        request.user.auth_token.delete()
        return Response(status = status.HTTP_200_OK)

class ProfileView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        pk = self.kwargs['pk']
        profile = Profile.objects.filter(user = pk)
        return profile

class ProfileCreate(generics.CreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Profile.objects.all()

    def perform_create(self , serializer):
        user = self.request.user
        profile_queryset = Profile.objects.filter(user = user )
        if profile_queryset.exists():
            raise ValidationError("You've already created your profile , Try updating it.")
        else :
            serializer.save(user = user)

class ProfileDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsProfileOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()