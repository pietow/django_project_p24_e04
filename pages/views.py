from django.http import HttpResponse, JsonResponse, HttpResponseForbidden, HttpResponseServerError 
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from datetime import datetime

def home_page_view(request):
    context = {
        'title': 'Welcome to my Site',
        'today': datetime.now(),
        'numbers': [1, 2, 3],
        'dic': {'one': 'dict1', 'two': 2 },
    }
    return render(request, "home.html", context)

def my_view(request):
    if request.method == 'GET':
        return HttpResponse("result")

class MyView(TemplateView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        print(request.method)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = {
        'title': 'Welcome to my Site',
        'today': datetime.now(),
        'numbers': [1, 2, 3, 'bla', 'Hello world'],
        'dic': {'one': 'dict1', 'two': 2 },
        }
        return context
        
    

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        print(response)
        return response

class ActiveUserRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.COOKIES.get('my_cookie') == 'my_value':
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseForbidden('You are not allowed to access.')
        

class DashboardView(ActiveUserRequiredMixin, TemplateView): 
    template_name = 'dashboard.html'
