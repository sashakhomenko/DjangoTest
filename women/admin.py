from django.contrib import admin
from .models import *


class WomenAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Women)
admin.site.register(Category, CategoryAdmin)
