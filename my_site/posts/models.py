from django.db import models
from users.models import Users
# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=150,unique=True)
    actual = models.BooleanField()

class Brend(models.Model):
    brend = models.CharField(max_length=150,unique=True)
    popular = models.BooleanField()

class Products(models.Model):
    name = models.CharField(max_length=200,unique=True)
    price = models.PositiveIntegerField(default=0)
    count = models.PositiveIntegerField(default=0)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)
    brend = models.ForeignKey(Brend,on_delete=models.CASCADE)
    likes = models.ManyToManyField(Users, related_name='post_likes')
    dislikes = models.ManyToManyField(Users, related_name='post_dislikes')