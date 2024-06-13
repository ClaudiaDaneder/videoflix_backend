
import os
import django_rq
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.core.files import File

from .tasks import convert480p, convert720p, getThumbnail
from .models import Video


@receiver(post_save, sender=Video)
def video_post_save(sender, instance, created, **kwargs):
    if created:
        queue = django_rq.get_queue('default', autocommit=True)
        queue.enqueue(convert480p, instance.video_file.path)
        queue.enqueue(convert720p, instance.video_file.path)

        thumbnail_path = 'media/thumbnails/' + os.path.basename(instance.video_file.path) + '.jpg'
        getThumbnail(instance.video_file.path, thumbnail_path)
        instance.thumbnail_path = thumbnail_path
        instance.save()


@receiver(post_delete, sender=Video)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Video` object is deleted.
    """
    if instance.video_file:
        base, ext = os.path.splitext(instance.video_file.path)
        if os.path.isfile(instance.video_file.path):
            os.remove(instance.video_file.path)

        video_480p_path = base + '_480p' + ext
        if os.path.isfile(video_480p_path):
            os.remove(video_480p_path)

        video_720p_path = base + '_720p' + ext
        if os.path.isfile(video_720p_path):
            os.remove(video_720p_path)

    if instance.thumbnail_path:
        if os.path.isfile(instance.thumbnail_path):
            os.remove(instance.thumbnail_path)