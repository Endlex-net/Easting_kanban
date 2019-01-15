from rest_framework.documentation import include_docs_urls

from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path(
        'drf-docs/',
        include_docs_urls(
            title='DRF Docs',
            authentication_classes=[],
            permission_classes=[],
        ),
    ),
]

urlpatterns += [
    path('board/', include('board.urls')),
    path('account/', include('account.urls')),
]
