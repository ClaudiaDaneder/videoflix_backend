import os
import subprocess



def convert480p(source):
    base, ext = os.path.splitext(source)
    target = base + '_480p.mp4'
    cmd = 'ffmpeg -i "{}" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}'.format(source, target)
    subprocess.run(cmd)