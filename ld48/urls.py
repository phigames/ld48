from django.contrib import admin
from django.urls import path

from ld48 import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("quote/", views.get_quote),
    path("upvote/<uuid:post_id>", views.post_upvote),
]
