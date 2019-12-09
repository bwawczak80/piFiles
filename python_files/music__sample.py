import pygame
from mutagen.mp3 import MP3
import PIL.Image as coverArt
import os
from io import BytesIO
from tkinter import *

pygame.mixer.init()
pygame.display.init()

playlist = list()
play_song = "/home/pi/old_love.mp3"
playlist.append("old_love.mp3")
# print(playlist)

pygame.mixer.music.load( playlist.pop()) # gets the first track
# pygame.mixer.music.queue(playlist.pop())
# pygame.mixer.music.set_endevent ( pygame.USEREVENT) # checks for song end

#audio = MP3(play_song)
# artist = audio['TPE1'][0]
# title = audio['TIT2'][0]
# pict = audi['APIC:'].data
# imPIL = coverArt.open(BytesIO(pict))
# img = PhotoImage(imPIL)

pygame.mixer.music.play()

# running = True

# while running:
    # for event in pygame.event.get():
        # if event.type == pygame.USEREVENT:
            # print("next")
            # queue next song, play next song, etc
            
            
# pip install pygame