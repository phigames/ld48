from django.contrib import admin
from django.urls import path

from ld48 import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("new/", views.new, name="new"),
    path("rate/", views.rate, name="rate"),
    path("posts/<username>/", views.posts, name="posts"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),
    path("check_username/", views.check_username, name="check-username"),
    path("credits/", views.credits, name="credits"),
]
