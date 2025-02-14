from django import template

register = template.Library()

@register.simple_tag
def hello_world(greeting='hello', name='bob'):
    return f'{greeting} World again, {name}'