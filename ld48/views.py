import json
import random
import uuid

from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from ld48 import models

N_RATE = 6
N_RATE_BEST = 3


def max_line_index():
    with open("data/alternatives.jsonl") as f:
        for i, l in enumerate(f):
            pass
    return i


MAX_LINE_INDEX = max_line_index()


def load_quote():
    with open("alternatives.jsonl") as f:
        i = random.randint(0, MAX_LINE_INDEX)
        for n, line in enumerate(f):
            if i == n:
                return json.loads(line)


@require_http_methods(["GET", "POST"])
def quote(request: HttpRequest):
    if request.method == "GET":
        finalquote = [
            {
                "word": "Hello",
                "alternatives": [
                    "Hi",
                    "salü",
                ],
            },
            {"word": "this", "alternatives": ["that", "Andreas"]},
        ]
        context = {"quote": finalquote}
        return render(request, "ld48/quote.html", context)

    elif request.method == "POST":
        data = json.loads(request.body)
        models.Post.objects.create(
            text=data.get("text"),
            username=data.get("username"),
        )
        return JsonResponse({"success": True})


@require_http_methods(["GET", "POST"])
def ratings(request: HttpRequest):
    if request.method == "GET":
        username = request.GET.get("username")
        models.Post.objects.exclude(username=username).order_by("n_ratings")[
            :N_RATE
        ].order_by("?")
        context = {
            "posts": [
                {
                    "id": uuid.uuid4(),
                    "text": f"example post {i}",
                    "username": f"User {i}",
                }
                for i in range(N_RATE)
            ],
            "n_rate_best": N_RATE_BEST,
        }
        return render(request, "ld48/rate.html", context)

    elif request.method == "POST":
        for post_id, rating in request.GET.items():
            post = models.Post.objects.get(post_id)
            post.add_rating(rating)
        return JsonResponse({"success": True})


@require_http_methods(["GET"])
def posts(request: HttpRequest, username: str):
    posts = models.Post.objects.filter(username=username)
    context = {
        "posts": [
            {
                "id": post.id,
                "text": post.text,
                "average_rating": post.average_rating,
                "n_ratings": post.n_ratings,
            }
            for post in posts
        ]
    }
    return render(request, "ld48/posts.html", context)


@require_http_methods(["GET"])
def leaderboard(request: HttpRequest):
    posts = models.Post.objects.order_by("-average_rating")
    context = {
        "posts": [
            {
                "id": post.id,
                "username": post.username,
                "text": post.text,
                "average_rating": post.average_rating,
                "n_ratings": post.n_ratings,
            }
            for post in posts
        ]
    }
    return render(request, "ld48/leaderboard.html", context)
