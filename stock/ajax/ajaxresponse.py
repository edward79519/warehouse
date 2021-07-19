from django.http import JsonResponse
from stock.models import Item


def get_item_count(request):
    item_id = request.GET.get('id_item')
    item = Item.objects.get(id=item_id)
    context = {
        'item_cnt': item.item_cnt,
    }
    return JsonResponse(context)
