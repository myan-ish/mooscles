from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from users.views import login

auth_urls = [
]

api_v1_urls = []

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include(auth_urls)),
    path("login/",login)
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
