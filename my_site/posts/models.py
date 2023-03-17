from django.db import models
from users.models import Users
# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=150,unique=True)
    actual = models.BooleanField()

    def __str__(self):
        return self.category

class Brend(models.Model):
    brend = models.CharField(max_length=150,unique=True)
    popular = models.BooleanField()

    def __str__(self):
        return self.brend

class Products(models.Model):
    name = models.CharField(max_length=200,unique=True)
    price = models.PositiveIntegerField(default=0)
    count = models.PositiveIntegerField(default=0)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)
    brend = models.ForeignKey(Brend,on_delete=models.CASCADE,)
    likes = models.ManyToManyField(Users, related_name='post_likes',blank=True)
    dislikes = models.ManyToManyField(Users, related_name='post_dislikes',blank=True)
    photo = models.ImageField(upload_to='img')

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Products, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.post}:{self.name}'