from django.template import Library
register = Library()


@register.filter
def model_type(value):
    return type(value).__name__

