from django.db import models

# Create your models here.

"""
SQL fields
id - int
title - varchar
content - text
created_at - date_time
updated_at - date_time
photo - image
is_published - boolean
"""


class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True) # content can be kept blank. In the database ("") will be stored.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    is_published = models.BooleanField(default=True)
