# %%
from pytube import YouTube
import os
import subprocess
import argparse

# %%

parser = argparse.ArgumentParser()
parser.add_argument('youtube_link', type=str)
parser.add_argument('filename', type=str)
parser.add_argument('--output_path', default='/Users/anhdungle/Filme')
args = parser.parse_args()
# %%
youtube_link = args.youtube_link
audio_output_path = args.output_path
y = YouTube(youtube_link)
t = y.streams.all()
t[0].download(output_path=audio_output_path, filename=args.filename)
print(f'Downloaded {os.path.join(audio_output_path, args.filename)}')

# %%
