import os
import sys
import wave
from pydub import AudioSegment
import numpy as np 
from tqdm import tqdm 

def sortsounds():
    sdir = "../../../PBD1 REPO/Reply Sounds/"
    wav_files = os.listdir(sdir)
    for w in tqdm(range(len(wav_files))):
        os.rename(sdir + wav_files[w], sdir + "unnamed " + str(w) + ".wav")
sortsounds()
