from django.shortcuts import render
from django.views.generic import TemplateView
from flower_shop.flower.models import FlowerItem


class FlowerWeddingTemplateView(TemplateView):
    template_name = 'items-weddings.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        flower_wedding_item = list(FlowerItem.objects.filter(item_category='WEDDING'))

        context.update({
            'items': flower_wedding_item,
        })
        a = context
        return context


class FlowerFuneralTemplateView(TemplateView):
    template_name = 'items-funeral.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        flower_funeral_item = list(FlowerItem.objects.filter(item_category='FUNERAL'))

        context.update({
            'items': flower_funeral_item,
        })
        return context
