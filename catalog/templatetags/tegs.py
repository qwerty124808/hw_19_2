from django import template

register = template.Library()

@register.simple_tag
def media_path(file_name):
    return f"/media/{file_name}"
    # return file_name