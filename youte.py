from pytube import YouTube
YouTube('https://www.youtube.com/watch?v=jNEkXs2zfbs').streams.first().download()
yt = YouTube('https://www.youtube.com/watch?v=jNEkXs2zfbs')
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')
desc()
first()
download()