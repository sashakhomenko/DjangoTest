from django.db import models
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('women', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, )
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name
