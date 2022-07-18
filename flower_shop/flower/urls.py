from django.urls import path
from flower_shop.flower.views import home_page


urlpatterns = [
    path('/',home_page,name='home'),
]