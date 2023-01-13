from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank = True , null = True , upload_to = 'profile_pictures')
    contact_number = models.IntegerField(default=9999)
    Twitter = models.CharField(max_length = 100 , blank = True)
    FaceBook = models.CharField(max_length =100, blank= True)
    Instagram = models.CharField(max_length = 100 , blank = True)
    
    def __str__(self):
        return self.user.username