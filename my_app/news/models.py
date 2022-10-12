from django.db import models
from django.urls import reverse

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
    title = models.CharField(max_length=150, verbose_name="Title")
    content = models.TextField(blank=True,
                               verbose_name="Content")  # content can be kept blank. In the database ("") will be stored.
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name="Photo", blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Is published?")
    category = models.ForeignKey("Category", on_delete=models.PROTECT, verbose_name="Name of category")

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"news_id": self.pk})

    def __str__(self):
        return self.title

    # Meta data in Django admin panel
    class Meta:
        verbose_name = "News"
        verbose_name_plural = "All News"
        ordering = ["-created_at"]


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Name of category")

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "All Category"
        ordering = ["title"]
