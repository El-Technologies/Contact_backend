# Generated by Django 4.1.5 on 2023-01-06 22:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App1', '0008_remove_contact_contact_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='contact_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
