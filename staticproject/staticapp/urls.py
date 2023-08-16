from django.contrib import admin
from django.urls import path
from staticproject import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('',views.demo,name='demo'),

   # path('add/',views.addition,name='addition')
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)