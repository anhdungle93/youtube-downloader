# %%
from pytube import YouTube
import os
import subprocess

# %%
youtube_link = 'https://www.youtube.com/watch?v=ccvq0NR41Vg&list=RDccvq0NR41Vg&start_radio=1&t=1'
download_name = 'Kevz - Everything I Wanted (spanish version).mp3'
audio_output_path = '/Users/anhdungle/Music'
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
