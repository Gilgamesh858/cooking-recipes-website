from django import template
register = template.Library()

@register.filter
def first_recipe(h, key):
    return h[0][key]
