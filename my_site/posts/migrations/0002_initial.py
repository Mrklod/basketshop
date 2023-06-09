# Generated by Django 4.1.7 on 2023-03-14 16:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='dislikes',
            field=models.ManyToManyField(related_name='post_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='products',
            name='likes',
            field=models.ManyToManyField(related_name='post_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
