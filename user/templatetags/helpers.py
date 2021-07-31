from django import template

register = template.Library()

@register.filter(name="cut")
def cut(value,arg):
    """
    This cuts out all args from the values string.
    """
    return value.replace(arg, "")