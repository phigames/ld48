from django.contrib import admin
from django.urls import path

from ld48.views import get_quote

urlpatterns = [
    path("admin/", admin.site.urls),
    path("quote/", get_quote),
]
