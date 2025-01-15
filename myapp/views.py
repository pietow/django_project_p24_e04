from django.views.generic import TemplateView
from .mixins import ExtraContentMixin

class MyView(ExtraContentMixin, TemplateView):
    template_name = 'my_template.html'
    extra_context = {'key': 'hello world'}

class MyView2(ExtraContentMixin, TemplateView):
    template_name = 'my_template.html'
    extra_context = {'key': 'hello world'}
