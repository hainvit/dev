"""
Import packages
"""
import uuid
from django.db import models

# Create your models here.


class MusicModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        db_table = 'music'
