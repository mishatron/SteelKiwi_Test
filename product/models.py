from __future__ import unicode_literals

from datetime import datetime
from django.utils.text import slugify

from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    slug = models.SlugField(blank=True)  # Allow blank submission in admin.

    def save(self, **kwargs):
        slug_str = "%s" % self.name
        self.slug = slugify(self, slug_str)
        super(Category, self).save(**kwargs)

    def __unicode__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.FloatField()
    created_at = models.DateTimeField(default=datetime.now())
    modified_at = models.DateTimeField(default=datetime.now())
    slug = models.SlugField(blank=True)  # Allow blank submission in admin.

    def save(self, **kwargs):
        slug_str = "%s" % self.name
        self.slug = slugify(self, slug_str)
        self.modified_at = datetime.now()
        super(Product, self).save(**kwargs)

    def __unicode__(self):
        return self.name
