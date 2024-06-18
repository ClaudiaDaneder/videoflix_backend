import os
import subprocess
from content.models import Video

# def convert360p(source):
#     base, ext = os.path.splitext(source)
#     target = base + '_360p' + ext
#     cmd = 'ffmpeg -i "{}" -s hd360 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, target)
#     subprocess.run(cmd, shell=True)

def convert360p(source, video_id):
    base, ext = os.path.splitext(source)
    target = 'videos_uploaded/360p/' + os.path.basename(base) + '_360p' + ext
    os.makedirs(os.path.dirname(target), exist_ok=True)
    cmd = 'ffmpeg -i "{}" -s hd360 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, target)
    subprocess.run(cmd, shell=True)
    video = Video.objects.get(id=video_id)
    video.video_360p_path = 'media/' + target
    video.save()


# def convert720p(source):
#     base, ext = os.path.splitext(source)
#     target = base + '_720p' + ext
#     cmd = 'ffmpeg -i "{}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, target)
#     subprocess.run(cmd, shell=True)

def convert720p(source, video_id):
    base, ext = os.path.splitext(source)
    target = 'videos_uploaded/720p/' + os.path.basename(base) + '_720p' + ext
    os.makedirs(os.path.dirname(target), exist_ok=True)
    cmd = 'ffmpeg -i "{}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, target)
    subprocess.run(cmd, shell=True)
    video = Video.objects.get(id=video_id)
    video.video_720p_path = 'media/' + target
    video.save()

# def convert1080p(source):
#     base, ext = os.path.splitext(source)
#     target = base + '_10800p' + ext
#     cmd = 'ffmpeg -i "{}" -s hd1080 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, target)
#     subprocess.run(cmd, shell=True)

def convert1080p(source, video_id):
    base, ext = os.path.splitext(source)
    target = 'videos_uploaded/1080p/' + os.path.basename(base) + '_1080p' + ext
    os.makedirs(os.path.dirname(target), exist_ok=True)
    cmd = 'ffmpeg -i "{}" -s hd1080 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, target)
    subprocess.run(cmd, shell=True)
    video = Video.objects.get(id=video_id)
    video.video_1080p_path = 'media/' + target
    video.save()

def getThumbnail(source, target):
    os.makedirs(os.path.dirname(target), exist_ok=True)
    cmd = 'ffmpeg -i "{}" -ss 00:00:01.000 -update true -frames:v 1 "{}"'.format(source, target)
    subprocess.run(cmd, shell=True)
