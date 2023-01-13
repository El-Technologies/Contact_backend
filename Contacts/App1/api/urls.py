from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ContactList.as_view() , name='contactList'),
    path('contact_details/<str:pk>/', views.ContactDetails.as_view() , name = 'contact_details')
]