from django.http.response import JsonResponse


def get_quote(request):
    return JsonResponse({"data": "quote"})
