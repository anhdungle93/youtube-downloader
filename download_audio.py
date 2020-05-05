# %%
from pytube import YouTube
import os
import subprocess
import argparse

# %%

parser = argparse.ArgumentParser()
parser.add_argument('youtube_link', type=str)
parser.add_argument('filename', type=str)
parser.add_argument('--output_path', default='/Users/anhdungle/Music')
args = parser.parse_args()
#%%
youtube_link = args.youtube_link
download_name = 'Kevz - Everything I Wanted (spanish version).mp3'
audio_output_path = args.output_path
y = YouTube(youtube_link)
t = y.streams.filter(only_audio=True).all()
t[0].download(output_path=audio_output_path)
default_filename = t[0].default_filename
print(f'Downloaded {os.path.join(audio_output_path, default_filename)}')

# %%

subprocess.call([                               # or subprocess.run (Python 3.5+)
    'ffmpeg',
    '-i', os.path.join(audio_output_path, default_filename),
    os.path.join(audio_output_path, download_name)
])
os.remove(os.path.join(audio_output_path, default_filename))
print(
    f'Convert video file to {os.path.join(audio_output_path, download_name)}')
# %%
