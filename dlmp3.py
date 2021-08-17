#!/bin/env python
#!Requires : youtube_dl & ffmpeg
#! Usage : python dlmp3.py https://www.youtube.com/watch?v=zzjQg-JdwTg
#!Philippe H.
#! You probably need to check your path to install ffmpeg

import youtube_dl #installed youtube_dl file

options = {
    'format':'bestaudio/best',
    'extractaudio':True,            #extracting audio
    'audioformat':'mp3',            #file options and format
    'outtmpl':'%(id)s.%(ext)s',     #name the file the ID of the video
    'noplaylist':True,
    'nocheckcertificate':True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',# Used ffmpeg for converting the file to mp3
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}

with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=zzjQg-JdwTg']) #final downloading
