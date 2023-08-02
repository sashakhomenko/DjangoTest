from django.conf.urls.static import static
from django.contrib import admin

from blog import settings
from django.urls import path, include
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('women.urls')),
    path('auth/', include('auth.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


