from django.conf.urls.static import static
from config import settings
from django.contrib import admin
from django.urls import path, include, reverse
from django.contrib.auth.decorators import user_passes_test


urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)