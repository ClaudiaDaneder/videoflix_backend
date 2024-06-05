
import os
import django_rq
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from .tasks import convert480p
from .models import Video


import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Video)
def video_post_save(sender, instance, created, **kwargs):
    logger.info("Video gespeichert")
    if created:
        try:
            queue = django_rq.get_queue('default', autocommit=True)
            queue.enqueue(convert480p, instance.video_file.path)
        except Exception as e:
            logger.error(f"Fehler beim Einreihen der Aufgabe: {e}")

@receiver(post_delete, sender=Video)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Video` object is deleted.
    """
    if instance.video_file:
        if os.path.isfile(instance.video_file.path):
            os.remove(instance.video_file.path)