from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatter = [
    path('admin/' , admin.site.urls),
    path('' , include('store.urls')),
]

urlpatter += static(settings.MEDIA_URL , document_root= settings.MEDIA_ROOT)