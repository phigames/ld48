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
    username = request.GET.get("username")
    posts = models.Post.objects.exclude(username=username).order_by(
        "n_ratings", "-created_at"
    )[:20]
    context = {
        "posts": posts,
    }
    return render(request, "ld48/home.html", context)


@require_http_methods(["GET", "POST"])
@ensure_csrf_cookie
def new(request: HttpRequest):
    if request.method == "GET":
        quote = load_quote()
        context = {"quote": quote}
        return render(request, "ld48/new.html", context)

    elif request.method == "POST":
        data = json.loads(request.body)
        words = data.get("words")
        image = data.get("image")
        text = ""
        for i, word in enumerate(words):
            if i > 0 and word.isalnum():
                text += " "
            text += word
        models.Post.objects.create(
            text=text,
            username=data.get("username"),
            image=image,
        )
        return JsonResponse({"success": True})


@require_http_methods(["POST"])
@ensure_csrf_cookie
def rate(request: HttpRequest):
    post_id = request.GET.get("id")
    rating = float(request.GET.get("rating"))
    old = request.GET.get("old")
    if old is not None:
        old = float(old)
    post = models.Post.objects.get(id=post_id)
    post.add_rating(rating, old_rating=old)
    return JsonResponse({"success": True})


@require_http_methods(["GET"])
@ensure_csrf_cookie
def posts(request: HttpRequest, username: str):
    posts = models.Post.objects.filter(username=username).order_by("-created_at")
    context = {"posts": posts}
    return render(request, "ld48/posts.html", context)


@require_http_methods(["GET"])
@ensure_csrf_cookie
def leaderboard(request: HttpRequest):
    posts = models.Post.objects.order_by("-average_rating", "-n_ratings")[:15]
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
