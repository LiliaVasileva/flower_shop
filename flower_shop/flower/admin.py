from django.contrib import admin

from flower_shop.flower.models import FlowerItem


class FlowerItemInlineAdmin(admin.StackedInline):
    model = FlowerItem

@admin.register(FlowerItem)
class FlowerItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'item_picture', 'item_price', 'item_discription', 'item_category')