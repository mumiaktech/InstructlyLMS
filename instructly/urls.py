from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include URLs from your apps
    path('', include('home.urls')),  # Home app
    path('users/', include('users.urls')),  # User management (authentication, profiles, etc.)
    path('materials/', include('materials.urls')),  # Learning materials (videos, PDFs, etc.)
]

# ✅ Serve media files properly during development
if settings.DEBUG:
    from django.views.static import serve
    from django.urls import re_path

    # Serve user-uploaded media files (only in development)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Serve static files correctly during development
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    # ✅ Handle missing media/static files gracefully (optional)
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]
