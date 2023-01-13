from App1.models import Contact
from rest_framework import serializers

class ContactSerializer(serializers.ModelSerializer):
    contact_user = serializers.StringRelatedField(read_only = True)

    class Meta:
        model = Contact
        fields = '__all__'