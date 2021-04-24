import json

from django.http.response import JsonResponse
from django.views.decorators.http import require_GET, require_POST

from ld48 import models


@require_GET
def quote(request):
    return JsonResponse({"data": "quote"})


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
