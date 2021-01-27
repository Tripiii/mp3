from __future__ import unicode_literals
import youtube_dl
print("Insert the link")
link = input ("")

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '360',
    }],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

print("Contact me on discord for any problem: ᴛʀɪᴘɪ#5945") 
