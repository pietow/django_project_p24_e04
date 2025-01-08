from django.urls import path
from .views import home_page_view, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='my_home'),
    path('', home_page_view, name='my_home'),
]
