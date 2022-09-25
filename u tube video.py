import pytube

link  = input('https://youtu.be/pdsxUAq_3R0')
yt = pytube.Youtube(link)
yt.streams.first().downlaod()
print('downloaded' , link)