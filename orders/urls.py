from django.urls import path
from .views import track_order, home, OrderCreateView

urlpatterns = [
    path('rastrear/', track_order, name='track_order'),
    path('', home, name='home'),
    
    # CRUD
    path('encomendas/nova/', OrderCreateView.as_view(), name='order_create'),
]
