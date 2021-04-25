import json
import random

from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods

from ld48 import models


def max_line_index():
    with open("data/alternatives.jsonl") as f:
        for i, l in enumerate(f):
            pass
    return i


MAX_LINE_INDEX = max_line_index()


def load_quote():
    with open("data/alternatives.jsonl") as f:
        i = random.randint(0, MAX_LINE_INDEX)
        for n, line in enumerate(f):
            if i == n:
                return json.loads(line)


@require_http_methods(["GET"])
@ensure_csrf_cookie
def home(request: HttpRequest):
    return render(request, "ld48/home.html")


@require_http_methods(["GET", "POST"])
@ensure_csrf_cookie
def quote(request: HttpRequest):
    if request.method == "GET":
        quote = load_quote()
        context = {"quote": quote}
        return render(request, "ld48/quote.html", context)

    elif request.method == "POST":
        data = json.loads(request.body)
        words = data.get("words")
        text = ""
        for i, word in enumerate(words):
            if i > 0 and word.isalnum():
                text += " "
            text += word
        models.Post.objects.create(
            text=text,
            username=data.get("username"),
        )
        return JsonResponse({"success": True})


@require_http_methods(["GET", "POST"])
@ensure_csrf_cookie
def ratings(request: HttpRequest):
    if request.method == "GET":
        username = request.GET.get("username")
        posts = models.Post.objects.exclude(username=username).order_by(
            "n_ratings", "updated_at"
        )[:8]
        context = {
            "posts": posts,
        }
        return render(request, "ld48/ratings.html", context)

    elif request.method == "POST":
        post_id = request.GET.get("id")
        rating = float(request.GET.get("rating"))
        post = models.Post.objects.get(id=post_id)
        post.add_rating(rating)
        return JsonResponse({"success": True})


@require_http_methods(["GET"])
@ensure_csrf_cookie
def posts(request: HttpRequest, username: str):
    posts = models.Post.objects.filter(username=username)
    context = {
        "posts": [
            {
                "id": post.id,
                "text": post.text,
                "username": post.username,
                "image": "https://images.unsplash.com/photo-1619325364907-693737fc268c?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=500&ixid=MnwxfDB8MXxyYW5kb218fHx8fHx8fHwxNjE5MzU2NTIy&ixlib=rb-1.2.1&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=500",
                "average_rating": post.average_rating,
                "n_ratings": post.n_ratings,
            }
            for post in posts
        ]
    }
    return render(request, "ld48/posts.html", context)


@require_http_methods(["GET"])
@ensure_csrf_cookie
def leaderboard(request: HttpRequest):
    posts = models.Post.objects.order_by("-average_rating")
    context = {
        "posts": posts,
    }
    return render(request, "ld48/leaderboard.html", context)


@require_http_methods(["GET"])
@ensure_csrf_cookie
def check_username(request: HttpRequest):
    username = request.GET.get("username")
    if not username:
        return HttpResponse("Username must not be empty", status=400)
    posts = models.Post.objects.filter(username=username)
    if posts.count() > 0:
        return HttpResponse("Username already taken", status=400)
    else:
        return HttpResponse("", status=200)


@require_http_methods(["GET"])
@ensure_csrf_cookie
def display_post(request: HttpRequest):
    if request.method == "GET":
        post = posts = models.Post.objects.all()[0]
        context = {
            "post": {
                "id": post.id,
                "username": post.username,
                "text": post.text,
                "image": "https://images.unsplash.com/photo-1619325364907-693737fc268c?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=500&ixid=MnwxfDB8MXxyYW5kb218fHx8fHx8fHwxNjE5MzU2NTIy&ixlib=rb-1.2.1&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=500",
                "average_rating": post.average_rating,
                "n_ratings": post.n_ratings,
            }
        }
        return render(request, "ld48/post.html", context)
