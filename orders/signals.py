from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Order


@receiver(pre_save, sender=Order)
def notify_status_change(sender, instance, **kwargs):
    if not instance.pk:
           # Novo objeto, não notifica
           return
    try:
           old_order = Order.objects.get(pk=instance.pk)
    except Order.DoesNotExist:
           return
       
    if old_order.status != instance.status:
           subject = f"Atualização de status: {instance.tracking_code}"
           message = (
               f"Olá!\n\n"
               f"O status da sua encomenda {instance.tracking_code} foi alterado para: {instance.get_status_display()}.\n"
               f"Destinatário: {instance.recipient}\n"
               f"Endereço: {instance.delivery_address}\n"
               f"Última atualização: {instance.updated_at}\n"
           )
           # Aqui você pode definir o e-mail real do destinatário, se disponível
           # Substitua pelo e-mail real do cliente, se houver
           recipient_list = ['cliente@exemplo.com']
           send_mail(subject, message, None, recipient_list)
