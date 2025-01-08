from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html" 


def home_page_view(request):
    return render(request, 'home.html')
    return HttpResponse("Hello World_bla!")

