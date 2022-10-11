from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = (
    [
    path('admin/', admin.site.urls),
    path('', include('brands.urls')),
    path('', include('models.urls')),
    path('', include('users.urls')),



] + static(settings.STATIC_URL, document_url=settings.STATIC_URL)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

)
