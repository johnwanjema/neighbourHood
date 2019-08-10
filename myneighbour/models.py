from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Hood(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    population = models.IntegerField()
    admin = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    landing_page = models.ImageField(upload_to='photos',null=True)

    class Meta:
        ordering = ['name']

class Business(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    email = models.EmailField()

    class Meta:
        ordering = ['name']


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profiles/')
    bio = models.CharField(max_length=250)
    email = models.EmailField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['bio']

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


class Post(models.Model):
    image = models.ImageField(upload_to = 'neighbourhood/')
    description = models.CharField(max_length=500)
    neighbourhood = models.ForeignKey('Hood')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('Profile', null=True)
    
    def save_profile(self):
        self.save()

    class Meta:
        ordering = ['description']
        
