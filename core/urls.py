
from django.contrib import admin
from django.urls import path, include
from django.comf.urls.static import static

from core import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)