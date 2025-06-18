from django.shortcuts import render
from .models import Order
from django.shortcuts import render


def home(request):
    return render(request, 'orders/home.html')

def track_order(request):
    contex = {}
    if request.method == 'POST':
        code = request.POST.get('tracking_code')
        try:
            order = Order.objects.get(tracking_code=code)
            contex['order'] = order
        except Order.DoesNotExist:
            contex['error'] = 'Encomenda não encontrada.'
    return render(request, 'orders/track_order.html', contex)