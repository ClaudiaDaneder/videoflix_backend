import os
import subprocess

def convert480p(source):
    base, ext = os.path.splitext(source)
    target = base + '_480p' + ext
    cmd = 'ffmpeg -i "{}" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, target)
    subprocess.run(cmd)

def convert720p(source):
    base, ext = os.path.splitext(source)
    target = base + '_720p' + ext
    cmd = 'ffmpeg -i "{}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, target)
    subprocess.run(cmd)


def getThumbnail(source, target):
    os.makedirs(os.path.dirname(target), exist_ok=True)
    cmd = 'ffmpeg -i "{}" -ss 00:00:01.000 -update true -frames:v 1 "{}"'.format(source, target)
    subprocess.run(cmd)