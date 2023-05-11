from django.urls import path
from .views import *

urlpatterns = [
    path('', WomenHome.as_view(), name='home'),
    path('category/<slug:slug>/', WomenByCategory.as_view(), name='category'),
    path('women/<slug:slug>/', WomenDetailed.as_view(), name='women'),
    path('about/', about, name='about'),
    path('add_women', AddWomen.as_view(), name='add_women')
]
