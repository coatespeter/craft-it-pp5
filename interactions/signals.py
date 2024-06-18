# interactions/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.admin.models import LogEntry, ADDITION
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from .models import Contact

@receiver(post_save, sender=Contact)
def notify_admin(sender, instance, created, **kwargs):
    if created:
        admin_user = User.objects.filter(is_superuser=True).first()
        if admin_user:
            LogEntry.objects.log_action(
                user_id=admin_user.pk,
                content_type_id=ContentType.objects.get_for_model(instance).pk,
                object_id=instance.pk,
                object_repr=str(instance),
                action_flag=ADDITION,
                change_message='New contact form submission.',
            )
