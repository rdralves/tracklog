from django.views.generic import ListView
from django.shortcuts import render
from .models import Order
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


def home(request):
    nome = 'teste'
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