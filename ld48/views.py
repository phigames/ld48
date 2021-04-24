import json
import random

from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

from ld48 import models

N_RATE = 6
N_RATE_BEST = 3


def count_lines():
    with open("quotes.jsonl") as f:
        for i, l in enumerate(f):
            pass
    return i


LINE_COUNT = count_lines()


def load_quote():
    with open("quotes.jsonl") as f:
        i = random.randint(0, LINE_COUNT)
        for n, line in enumerate(f):
            if i == n:
                return json.loads(line)


@require_GET
def quote(request):
    quote = ["load", "shit"]
    context = {
        "quote": quote,
    }
    return render(request, "ld48/quote.html", context)


@require_POST
def post(request):
    data = json.loads(request.body)
    return JsonResponse({"success": True})


@require_GET
def rate(request, username):
    models.Post.objects.exclude(username=username).order_by("?")[:N_RATE]
    context = {
        "posts": [
            {
                "text": f"example post {i}",
                "username": f"User {i}",
            }
            for i in range(N_RATE)
        ],
        "n_rate_best": N_RATE_BEST,
    }
    return render(request, "ld48/rate.html", context)


@require_POST
def upvote(request, post_id):
    post = models.Post.objects.get(post_id)
    post.upvotes += 1
    post.save()
    return JsonResponse({"success": True})
