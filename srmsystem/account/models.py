from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from website.models import *

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, default='https://i.ibb.co/KGZKQFx/av.jpg')
    bio = models.TextField(verbose_name="Bio", max_length="200", null=True, blank=True)
    nationality = models.TextField(verbose_name="Nationality", choices=helpers.GetCountiesDoubleTuple(), null=True, blank=True)
    races = models.ManyToManyField(Race, related_name="drivers")
    series = models.ManyToManyField(Series, related_name="drivers")

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + ", " + self.user.username

def get_name(self):
    return self.first_name + " " + self.last_name

User.add_to_class("__str__", get_name)
        

