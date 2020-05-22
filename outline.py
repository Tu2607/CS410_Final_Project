# rough outline of some functions that we might need

import simpleaudio as sa
import time as t
from _thread import start_new_thread  # for playback
from tkinter import Tk

start = t.time()  # for recording audio

recording = False

# for visuals, this I can take a more in depth look at
class Piano(Frame): 

# playing the recording
def play(filename): 

# record
def record(filename, note): 

# find note based on user clicked; the array is connected to the dictionary
# used in key pressed
def find_note(note, array): 

# ---- For all the visual stuff dealing with mouse presses/keyboard presses ----
# record
def record_option(event): 

# play back
def play_back(event): 
 
# changes the image for pressing down the key
# event is the mouse event 
def pressed(event): 

# changes the image for releasing the key
def released(event): 

# pressing the keys
def pressed_keys(event): 

# releasing the keys
def released_keys(event): 

# pressing a button
def pressed_button(event): 

# releasing a button
def released_button

# ---- DICTIONARY ----
# 'key' is the name of the computer keyboard key
# 'C1' is the name of the note, 1 represents the octave that it's in
NOTES = { 
  'key': 'C1', 
}

# ---- MAIN ----
def main(): 
  root = Tk()
  play_piano = Piano(root)
  play_piano.mainloop()    # keep showing the piano until the user exits the program

if __name__ == '__main__':
  main()
