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
    path("check_username/", views.check_username, name="check-username"),
    path("display_post/", views.display_post, name="display_post"),
]
