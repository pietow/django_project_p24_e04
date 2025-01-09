from django.urls import path
from .views import home_page_view, HomePageView, AboutPageView

urlpatterns = [
    path('', home_page_view, name='my_home'),
    # path('', HomePageView.as_view(), name='my_home'),
    path('about/', AboutPageView.as_view(), name='about'),
]
