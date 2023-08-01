from django.db import models


class MyModel(models.Model):
    some_field = models.CharField()

    def __str__(self):
        return self.some_field
