from pygame import *

def initSound():
    mixer.init()

def playSfx(track, loops=0, channel=1):
    chn = mixer.Channel(channel)
    track_full = "data/sounds/" + str(track) + ".ogg"
    snd = mixer.Sound(track_full)
    chn.play(snd, loops)

def getChannelBusy(channel):
    chn = mixer.Channel(channel)
    return chn.get_busy()

