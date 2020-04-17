from django.contrib import admin
from .models import User, Tweet, Topic


admin.site.register(User)
admin.site.register(Tweet)
admin.site.register(Topic)
# Register your models here.
