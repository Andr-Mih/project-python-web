# Generated by Django 3.2.7 on 2021-09-06 14:05

from django.db import migrations, models
import storages.backends.sftpstorage


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contact_contact_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='contact_name',
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_adress',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_phone',
            field=models.CharField(default='0501111111', max_length=10),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_photo',
            field=models.FileField(blank=True, null=True, storage=storages.backends.sftpstorage.SFTPStorage(), upload_to=''),
        ),
    ]