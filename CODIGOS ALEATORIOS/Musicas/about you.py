import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text,delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(Lyric, delay, speed):
    time.sleep(delay)
    animate_text(Lyric, speed)

def sing_song():
    lyrics = [
        ("Do you think I have forgotten?", 0.1),
        ("Do you think I have forgotten?", 0.1),
        ("Do you think I have forgotten?", 0.1),
        ("About you?", 0.2),
        ("There was something 'bout you that now I can't remember", 0.1),
        ("It's the same damn thing that made my heart surrender", 0.1),
        ("And I miss you on a train, I miss you in the morning", 0.1),
        ("I never know what to think about", 0.1),
        ("I think about you", 0.1),
    ]
    delays = [0.3, 5.0, 10.0, 15.0, 20.3, 25.0, 27.0, 30.2, 33.3]
    
    thereads = []
    for i in range(len(lyrics)):
        lyrics, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyrics, delays[i], speed))
        thereads.append(t)
        t.start()
    
    for thread in thereads:
        thread.join()
    
if __name__=="__main":
    sing_song()