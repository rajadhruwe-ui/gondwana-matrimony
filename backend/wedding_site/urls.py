from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static   # ✅ FIXED

def api_root(request):
    return JsonResponse({
        "message": "Wedding Site API is running",
        "endpoints": [
            "/register/",
            "/login/",
            "/profile/",
            "/preferences/",
            "/location/",
            "/photos/"
        ]
    })

urlpatterns = [
    path('', api_root),   # ✅ Root welcome API
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('matrimony/', include('matrimony.urls')),
    path('weddings/', include('weddings.urls')),
]

# ✅ MEDIA FILES (only for development or trusted servers)
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
