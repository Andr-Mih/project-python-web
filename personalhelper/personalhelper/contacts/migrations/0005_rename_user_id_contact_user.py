# Generated by Django 3.2.7 on 2021-09-06 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20210906_2218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='user_id',
            new_name='user',
        ),
    ]