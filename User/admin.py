from django.contrib import admin
from User.models import User, Post

# Register your models here.

# @admin.register(User)
# class UserModelAdmin(admin.ModelAdmin):

#     list_display = ['first_name','last_name','email','password','username']


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):

    list_display = ['user','text','created_at','updated_at']