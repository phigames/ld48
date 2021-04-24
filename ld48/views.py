import json
import random

from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

from ld48 import models


def count_lines():
    with open("alternatives.jsonl") as f:
        for i, l in enumerate(f):
            pass
    return i


LINE_COUNT = count_lines()


def load_quote():
    with open("alternatives.jsonl") as f:
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


@require_POST
def upvote(request, post_id):
    post = models.Post.objects.get(post_id)
    post.upvotes += 1
    post.save()
    return JsonResponse({"success": True})
