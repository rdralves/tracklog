from django.views.generic import DetailView
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


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    template_name = 'orders/order_form.html'
    fields = [
        'tracking_code', 'sender', 'recipient', 'delivery_address',
        'weight_kg', 'declared_value', 'status'
    ]
    # Ajuste depois, quando a lista existir
    success_url = reverse_lazy('order_list')


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'
    ordering = ['-created_at']


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/order_detail.html'
    context_object_name = 'order'
