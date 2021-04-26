import babel.dates
from django import template
from django.utils import timezone

register = template.Library()


@register.filter
def times(number: int):
    return range(1, number + 1)


@register.filter
def format_timedelta(time: timezone.datetime):
    return babel.dates.format_timedelta(time - timezone.now(), add_direction=True)


@register.inclusion_tag("ld48/star_rating.html")
def star_rating(post):
    return {"post": post}


@register.inclusion_tag("ld48/post.html")
def show_post(post):
    return {"post": post}


@register.inclusion_tag("ld48/minipost.html")
def show_minipost(post):
    return {"post": post}
