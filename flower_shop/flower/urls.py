from django.urls import path
from django.views.generic import TemplateView
from flower_shop.flower.views import FlowerWeddingTemplateView, FlowerFuneralTemplateView



urlpatterns = [
    path('wedding/', FlowerWeddingTemplateView.as_view(), name='wedding items'),
    path('funeral/', FlowerFuneralTemplateView.as_view(), name='funeral items'),
]