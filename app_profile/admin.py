from django.contrib import admin
from .models import Profile

# This allows you to view the profiles under the admin tab
admin.site.register(Profile)