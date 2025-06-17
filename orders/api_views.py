from rest_framework import viewsets, permissions
from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    
    def get_permissions(self):
        if self.action in ['list', 'retrive']:
            return [permissions.AllowAny()]
        return super().get_permissions()