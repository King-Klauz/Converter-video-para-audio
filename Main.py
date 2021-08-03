import os
from moviepy.editor import *

video = 'teste1.mp4'

print('Lendo arquivo mp4')
print('-'*20)
mp4 = VideoFileClip(os.path.join(video))
nome_mp3 = video[:-4]+'.mp3'
print('Convertendo para mp3')
mp4.audio.write_audiofile(os.path.join(nome_mp3))
print('-'*20)
print('Converteu mp4 ' + video + ' para mp3 ' + nome_mp3)