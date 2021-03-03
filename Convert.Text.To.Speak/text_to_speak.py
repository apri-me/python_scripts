import io
import pygame
from gtts import gTTS

def speak(text):
    with io.BytesIO() as file:
        gTTS(text=text, lang='en').write_to_fp(file)
        file.seek(0)
        pygame.mixer.init()
        pygame.mixer_music.load(file)
        pygame.mixer_music.play()
        while pygame.mixer_music.get_busy():
            continue

text = input("Say whatever you want:\n  >> ")
speak(text)