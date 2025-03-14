import pygame
import time
from mutagen.mp3 import MP3
pygame.init()
def play_music(music_file):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()
    audio = MP3(music_file)
    length = audio.info.length
    time.sleep(length)
pygame.quit()