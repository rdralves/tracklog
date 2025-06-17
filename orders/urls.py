from django.urls import path
from .views import track_order

urlpatterns = [
    path('rastrear/', track_order, name='track_order'),
]
