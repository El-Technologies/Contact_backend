from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    contact_user = models.ForeignKey(User , on_delete = models.CASCADE )
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone_number = models.BigIntegerField()
    address = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.firstname + ' ' + self.lastname