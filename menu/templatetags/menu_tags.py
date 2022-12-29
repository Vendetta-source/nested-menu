from django import template
from django.shortcuts import get_object_or_404
from menu.models import ItemMenu

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    menu = get_object_or_404(ItemMenu, menu_name=menu_name, parent=None)
    local_context = {
        'menu_item': menu
    }
    requested_pk = context['request'].path.split('/')[1]
    try:
        active_menu_item = ItemMenu.objects.get(pk=requested_pk)
    except:
        pass
    else:
        unwrapped_menu_item_ids = active_menu_item.get_elder_ids() + [active_menu_item.id]
        local_context['unwrapped_menu_item_ids'] = unwrapped_menu_item_ids
    return local_context


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu_item_children(context, menu_item_pk):
    menu_item = get_object_or_404(ItemMenu, pk=menu_item_pk)
    local_context = {'menu_item': menu_item}
    if 'unwrapped_menu_item_ids' in context:
        local_context['unwrapped_menu_item_ids'] = context['unwrapped_menu_item_ids']
    return local_context
