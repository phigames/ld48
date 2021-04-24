import json

from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

from ld48 import models


@require_GET
def quote(request):
    quote = ["load", "shit"]
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
