from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include('user.urls')),
    path("account/", include('user_account.urls')),
    path("feed/", include('social.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
