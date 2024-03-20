from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from users.views import login
from workout.urls import urlpatterns as workout_urls
from workout.views import index_page

auth_urls = [
]

api_v1_urls = []

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include(auth_urls)),
    path("login/",login),
    path("", index_page),
    path("workout/", include(workout_urls)),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
