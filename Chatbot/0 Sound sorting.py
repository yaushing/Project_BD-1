import os 
from pydub import AudioSegment
import numpy as np 
from tqdm import tqdm 

mp3_files = os.listdir()
for src in tqdm (mp3_files):
    
    des = src.replace('.mp3','.wav')
    try:
        sound = AudioSegment.from_mp3(src)
        sound.set_channels(1)
        sound = sound.set_frame_rate(16000)                
        sound = sound.set_channels(1)    
        sound.export(des, format="wav")

    except:
        print(src)
        continue
