from django.urls import path
from .views import OrderCreateView, OrderDeleteView, OrderDetailView, OrderListView, OrderUpdateView, track_order, home
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('rastrear/', track_order, name='track_order'),
    path('', home, name='home'),
    path('encomendas/', OrderListView.as_view(), name='order_list'),
    path('encomendas/nova/', OrderCreateView.as_view(), name='order_create'),
    path('encomendas/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('encomendas/<int:pk>/editar/',
         OrderUpdateView.as_view(), name='order_update'),
    path('encomendas/<int:pk>/excluir/',
         OrderDeleteView.as_view(), name='order_delete'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    
]
