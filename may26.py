# ANGIE NOTES: 
# Some things I'm thinking about: 
# Having the option to hit the key on screen and the option to use the keyboard
# to play keys
# Currently thinking of having 3 octaves

import simpleaudio as sa              # lets the user play sounds (recording) 
import time as t                      # keeps track of time (recording)
from _thread import start_new_thread  # we're going to have a lot of features
                                      # running at once, so this helps with that
from tkinter import Tk, Frame         # lets us have the piano graphics

# in case the user wants to start recording
record_start = t.time()

# ---------- USER OPTIONS ----------

# record what the user wants to record
# TO DO: THE BACK PART OF THIS FUNCTION
def record(file, note): 
  my_recording = open(file, 'a')
  end = t.time()
  time = ending_pt - starting_pt
  my_recording.write(_____idk what goes here yet_____)

# play what the user recorded
# TO DO: THIS WHOLE FUNCTION 
# NOTE: I think we might need another function for playback? So we can see it
# on the screen too? Or that could be done in this function. Will look more 
# into it. 
def play(file): 

# ---------- MOUSE EVENTS ----------

# lets the user know if they're recording or not
# TO DO: THIS WHOLE FUNCTION
def is_recording(event):
  

# what the user sees when they press a button; the keys and the record button
# TO DO: FIND IMAGE FOR THE BLANKS; img = 
def press_button(event): 
  if event.widget.name == 'white_key': 
    img = '_____white key_____'
  elif event.widget.name == 'black_key':  
    img = '_____black key_____'
  else
    img = '_____start button_____'
  # TO DO ON THIS LINE: initialize the normal keys; key = .....
  event.widget.configure(image = key)
  event.widget.image = key

# what the user sees when they release a button; the keys and the record button

def release_button(event): 
  if event.widget.name == 'white_key':
    img = '_____white key released_____'
  elif event.widget.name == 'black_key':
    img = '_____black key released___'
  else: 
    img = '_____stop button_____'
  # TO DO ON THIS LINE: initialize the released keys; key = .....
  event.widget.configure(image = key)
  event.widget.image = key

# ---------- MAIN ----------
# there's obvi more to add here
def main(): 
  root = Tk()

if __name__ == '__main__': 
  main()

