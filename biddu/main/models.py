from django.db import models
from django.contrib.auth.models import User
from django.urls.base import reverse

# Create your models here.
class UserInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    git_url=models.URLField(blank=True)
    profile_pic=models.ImageField(blank=True,upload_to='profile_image')


    def _str_(self):
        return self.user.username

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name


class Hostel(models.Model):
    hostel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200,default="")
    type = models.CharField(max_length=50)
    budget = models.IntegerField(default=0)
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.name