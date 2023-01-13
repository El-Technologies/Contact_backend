from App1.models import Contact
from .serializers import ContactSerializer
from rest_framework.exceptions import ValidationError
from rest_framework import status 
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from .pagination import ContactPagination
from App1.api.permissions import IsAdminOrReadOnly , IsContactUserOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly , IsAuthenticated
from rest_framework.views import APIView 
from rest_framework import filters , generics
from django_filters.rest_framework import DjangoFilterBackend

class ContactList(generics.ListCreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=firstname' , '=lastname' , '=email' , '=phone_number']
# class ContactList(APIView):
#     pagination_class = ContactPagination
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['firstname' , 'lastname' , 'email' , 'phone_number']
#     def get(self , request):
#         contacts = Contact.objects.all()
#         serializer = ContactSerializer(contacts , many = True)
#         return Response(serializer.data)
#     def post(self , request):
#         serializer = ContactSerializer(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

# class ContactDetails(APIView):
#     pagination_class = ContactPagination
#     permission_classes = [IsContactUserOrReadOnly]
#     def get(self , request , id):
#         try:
#             contact = Contact.objects.get(id = id)
#         except Contact.DoesNotExist:
#             return Response({'Error' : 'Contact not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = ContactSerializer(contact)
#         return Response(serializer.data)
#     def put(self , request , id):
#         contact = Contact.objects.get(id = id)
#         serializer = ContactSerializer(contact , data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#     def delete(self , request , id):
#         contact = Contact.objects.get(id = id)
#         contact.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class ContactDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsContactUserOrReadOnly]
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

