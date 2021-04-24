from django.contrib import admin
from django.urls import path

from ld48 import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("quote/", views.quote),
    path("rate/<username>/", views.rate),
    path("upvote/<uuid:post_id>/", views.upvote),
    path("post/", views.post),
]
