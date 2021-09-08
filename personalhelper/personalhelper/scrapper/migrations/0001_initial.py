# Generated by Django 3.2.7 on 2021-09-08 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=100)),
                ('games', models.CharField(max_length=10)),
                ('wins', models.CharField(max_length=10)),
                ('draws', models.CharField(max_length=10)),
                ('losses', models.CharField(max_length=10)),
                ('goals_in', models.CharField(max_length=10)),
                ('goals_out', models.CharField(max_length=10)),
                ('scores', models.CharField(max_length=10)),
            ],
        ),
    ]
