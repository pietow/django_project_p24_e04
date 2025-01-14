from django import template

register = template.Library()

@register.inclusion_tag('footer.html')
def render_footer(company_name="My Company"):
    return {'company_name': company_name}