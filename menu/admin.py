from django.contrib import admin
from menu.models import ItemMenu
from menu.forms import ItemMenuForm


class ItemMenuInline(admin.StackedInline):
    model = ItemMenu
    form = ItemMenuForm


class ItemMenuAdmin(admin.ModelAdmin):
    inlines = [ItemMenuInline]
    form = ItemMenuForm


admin.site.register(ItemMenu, ItemMenuAdmin)
