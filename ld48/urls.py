from django.contrib import admin
from django.urls import path

from ld48 import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("quote/", views.quote, name="quote"),
    path("ratings/", views.ratings, name="ratings"),
    path("posts/<username>/", views.posts, name="posts"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),
]
