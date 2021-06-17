from pygame import *

def initSound():
    mixer.init()

def playSfx(track, loops=0):
    track_full = "data/sounds/" + str(track) + ".ogg"
    snd = mixer.Sound(track_full)
    mixer.Sound.play(snd, loops)

