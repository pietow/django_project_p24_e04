from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden, HttpResponseServerError
from datetime import datetime

def home_page_view(request):
    # print("Request Object:", request)
    # print("Method:", request.method)
    # print("Cookies:", request.COOKIES)
    # print("Query Parameters:", request.GET)  # e.g., ?key=value
    # print("Raw Body:", request.body)

    return render(request, "home.html")


def home_page_view(request):
    # Using render to return a template response
    response = render(request, 'home.html')
    
    # Creating a custom HttpResponse
    html_response = HttpResponse('<h1>Hello</h1>')
    html_response.write('<div>Additional Content</div>')
    response.write('<div>Add to HOME</div>')
    html_response.set_cookie('my_cookie', 'cookie_value')
    
    # JSON response example
    json_response = JsonResponse({'status': 'success', 'message': 'Hello'})
    
    # Forbidden and server error examples
    forbidden_response = HttpResponseForbidden('Access Denied') # 403
    server_error_response = HttpResponseServerError('Server Error') # 500
    server_error_response.delete_cookie('my_cookie')

    # Return the response (example: using the HTML response here)
    return response
    # return html_response
    # return json_response
    # return forbidden_response
    return server_error_response

def home_page_view(request):
    context = {
        'title': 'Welcome to My Site',
        'today': datetime.now(),
        'numbers': [1, 2, 3],          # List of numbers
    }
    return render(request, 'home.html', context)

    

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"
