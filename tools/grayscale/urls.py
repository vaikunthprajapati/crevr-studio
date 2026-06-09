from .views import *
from django.contrib import admin
from django.urls import path
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("takephoto/", takePhoto, name="takephoto"),
    path("", takePhoto, name="home"),
    path("compress/", compressing, name="compress"),
    path("resizing/", resizing, name="resizing"),
    path("rotatephoto/", rotate, name="rotatephoto"),
    path("brightness/", brightness, name="brightness"),
    path("contrast/", contrast, name="contrast"),
    path("blur/", blur, name="blur"),
    path("convert/", convert_file, name="convert"),
    path("watermark/", watermark, name="watermark"),
    path("crop/", Crop, name="crop"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
