from django.db import models


class Notes(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.CharField(max_length=255)
