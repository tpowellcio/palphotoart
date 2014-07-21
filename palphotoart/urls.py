from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin

urlpatterns = patterns(
    "",
    url(r"^admin/", include(admin.site.urls)),
    url(r"", include("biblion.urls")),
)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
