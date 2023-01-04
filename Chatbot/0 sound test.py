from playsound import playsound
import time, random
from tqdm import tqdm as tqdm

text=input("Write a sentence to translate to Beep and Boop.")
for letter in tqdm(text, "Processing: "):
        time.sleep(0.01)
for letter in text:
        if letter.isalpha():
                if letter.istitle():
                        playsound(letter.lower()+"c.mp3")
                else:
                        playsound(letter + ".mp3")
        elif letter.isnumeric():
                playsound(letter + ".mp3")
        elif letter == " ":
                time.sleep(0.1)
        elif letter == ",":
                time.sleep(0.3)
        else:
                time.sleep(0.5)
