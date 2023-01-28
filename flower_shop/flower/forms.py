from django import forms
from flower_shop.flower.models import FlowerItem

class FlowerItemCreateForm(forms.ModelForm):
    class Meta:
        model = FlowerItem
        fields = '__all__'