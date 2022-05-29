from django.db import models
from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.conf import Settings, settings

class Task(models.Model):
    title=models.TextField(null=True,blank=True)
    completed=models.BooleanField(default=False,blank=True,null=True)

    def __str__(self):
        return str(self.title)[0:50]
    class Meta:
        verbose_name_plural="My TODO LIST"
