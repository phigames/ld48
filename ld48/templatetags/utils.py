from django import template

register = template.Library()


@register.filter
def times(number: int):
    return range(1, number + 1)


@register.inclusion_tag("ld48/star_rating.html")
def star_rating(post):
    return {"post": post, "editable": True}


@register.inclusion_tag("ld48/post.html")
def show_post(post):
    return {"post": post}
