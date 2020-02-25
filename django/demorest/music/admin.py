"""
Import pakages
"""
from django.contrib import admin

# Register your models here.

from .models import MusicModel

admin.site.register(MusicModel)
