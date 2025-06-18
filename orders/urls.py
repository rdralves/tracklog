from django.urls import path
from .views import OrderCreateView, OrderDetailView, OrderListView, track_order, home

urlpatterns = [
    path('rastrear/', track_order, name='track_order'),
    path('', home, name='home'),
    path('encomendas/', OrderListView.as_view(), name='order_list'),
    path('encomendas/nova/', OrderCreateView.as_view(), name='order_create'),
    path('encomendas/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
]
