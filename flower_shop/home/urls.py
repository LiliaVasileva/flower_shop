from django.urls import path
from flower_shop.home.views import home_page

urlpatterns = [
    path('', home_page, name='home')
]