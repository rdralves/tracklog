from django.db import models

# Create your models here.


class Order(models.Model):
    STATUS_CHOICES = [
        ('AGUARDANDO', 'Aguardando coleta'),
        ('TRANSITO', 'Em trânsito'),
        ('ENTREGUE', 'Entregue'),
        ('CANCELADA', 'Cancelada'),
    ]

    tracking_code = models.CharField(max_length=20, unique=True)
    sender = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    delivery_address = models.CharField(max_length=255)
    weight_kg = models.DecimalField(max_digits=6, decimal_places=2)
    declared_value = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='AGUARDANDO')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tracking_code} - {self.status}"
