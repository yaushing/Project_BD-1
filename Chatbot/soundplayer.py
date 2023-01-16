from playsound import playsound
import time, random
from tqdm import tqdm as tqdm
from splitter import hyphenate_word
from makesound import createsound
import os

def get_random_permutation(alrused, datalist):
        chosen = []
        used = []
        chosen = [random.choice(datalist), random.choice(datalist)]
        while chosen in alrused:
                chosen = [random.choice(datalist), random.choice(datalist)]
                if chosen not in alrused:
                        break
        used = alrused
        used.append(chosen)                  
        return used, chosen

def transsent(sentence):
        sdir = "../Chatbot/sylsound/"
        sdirb = "../Chatbot/sylsound/base/"
        punc = list("""!@#$%^&*()_+{}|:"<>?-=[]\;',./""")
        sentenced = ""
        for letter in sentence:
                sentenced += letter if letter not in punc else ""
        words = sentenced.split(" ")
        processed_word=[]
        processed_words=[]
        for word in words:
                processed_word = hyphenate_word(word)
                processed_words.append(" ".join(processed_word))
        processed_sentence = " ".join(processed_words)
        sounds = os.listdir(sdir)
        for syl in processed_sentence.split(" "):
                sounds = os.listdir(sdir)
                if (syl.lower() + ".wav") in sounds:
                        playsound(sdir + syl.lower() + ".wav")
                else:
                        sounds = os.listdir(sdir)
                        for i in range(len(sounds)):
                                if "unnamed" in sounds[i]:
                                        oldfdir = f"{sdir}{sounds[i]}"
                                        newfdir = f"{sdir}{syl.lower()}.wav"
                                        os.rename(oldfdir, newfdir)
                                        playsound(newfdir)
                                        break
                                else:
                                        base = os.listdir(sdirb)
                                        data = []
                                        perm = get_random_permutation(data, base)
                                        data = perm[0]
                                        chosensounds = perm[1]
                                        sortedperm = []
                                        for sound in chosensounds:
                                                sortedperm.append(f"{sdirb}{sound}")
                                        createsound(sortedperm, f"{syl.lower()}.wav")
                        playsound(sdir + syl.lower() + ".wav")
                                
