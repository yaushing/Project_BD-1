from playsound import playsound
import time, random
from splitter import hyphenate_word
import os

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
                        sounds = os.listdir(sdirb)
                        for i in range(len(sounds)):
                                if "unnamed" in sounds[i]:
                                        oldfdir = f"{sdirb}{sounds[i]}"
                                        newfdir = f"{sdir}{syl.lower()}.wav"
                                        os.rename(oldfdir, newfdir)
                                        playsound(newfdir)
                                        break
                                
transsent("hello there")
