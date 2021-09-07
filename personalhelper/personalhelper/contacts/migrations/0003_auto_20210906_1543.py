# Generated by Django 3.2.7 on 2021-09-06 12:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import storages.backends.sftpstorage


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0002_contact_contact_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_photo',
            field=models.FileField(null=True, storage=storages.backends.sftpstorage.SFTPStorage(), upload_to='contacts/files/'),
        ),
    ]