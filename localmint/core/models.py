from django.db import models
from django.db.models import DateTimeField


class BaseModel(models.Model):
    created = DateTimeField(auto_now_add=True)
    modified = DateTimeField(auto_now=True)

    class Meta:
        abstract = True
