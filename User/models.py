from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class User(models.Model):

#     first_name = models.CharField(max_length=30) 
#     last_name = models.CharField(max_length=30) 
#     email = models.EmailField(max_length=50, blank=True, unique=True)
#     password = models.CharField(max_length=20)
#     username = models.CharField(max_length=50)

#     def __str__(self):
#         return str(self.username)

class Post(models.Model):

    user = models.ForeignKey(User, on_delete= models.PROTECT)
    text = models.TextField()
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


