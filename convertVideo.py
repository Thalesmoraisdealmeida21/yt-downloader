# Python code to convert video to audio
import moviepy.editor as mp
import sys
import os
from pytube import YouTube, Playlist
from os import listdir
from os.path import isfile, join


VIDEO_URL = 'https://www.youtube.com/watch?v=3YxaaGgTQYM&list=RDI6byS9xg_-M'

PLAYLIST_URL = "https://www.youtube.com/playlist?list=PLWTSsd0y7OItC52oDqZC0C-ag2NOSkKE3"


playlist = Playlist("https://www.youtube.com/playlist?list=PLWTSsd0y7OIu0oGve6pBO0dB2mUMGdnas")

for url in playlist:
    print(url)
    video = YouTube(url)
    video.streams.get_highest_resolution().download()
    onlyfiles = [f for f in listdir('./') if isfile(join('./', f))]
    for file in onlyfiles:
        if os.path.splitext(file)[1] == '.mp4':
            print(file)
            clip = mp.VideoFileClip(file)
            clip.audio.write_audiofile(os.path.splitext(file)[0] + '.mp3')
            os.remove(file)





