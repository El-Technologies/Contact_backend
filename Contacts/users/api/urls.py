from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from users.api.views import registration , logout
from . import views


urlpatterns = [
    path('login/' , obtain_auth_token , name = 'login'),
    path('register/' ,views.registration , name = 'register'),
    path('logout/' , views.logout , name = 'logout'),
    path('profile/<str:pk>/' , views.ProfileView.as_view() , name ='profile') ,
    path('create_profile/', views.ProfileCreate.as_view() , name= 'create_profile'),
    path('update_profile/<str:pk>/' , views.ProfileDetails.as_view() , name = 'update_profile'),
]