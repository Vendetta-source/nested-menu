from django import forms
from menu.models import ItemMenu


class ItemMenuForm(forms.ModelForm):
    class Meta:
        model = ItemMenu
        fields = '__all__'