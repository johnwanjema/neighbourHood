from django.contrib import admin
from .models import Profile,Hood,Business,Post

# Register your models here.

admin.site.register(Business)
admin.site.register(Hood)
admin.site.register(Profile)
admin.site.register(Post)