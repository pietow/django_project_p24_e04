from django.http import HttpResponse, JsonResponse, HttpResponseForbidden, HttpResponseServerError 
from django.shortcuts import render
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
    

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"
