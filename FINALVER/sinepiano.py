# Angie McGraw, Tu Vu
# CS 410P: Computers, Sound, and Music Final Course Project
# A Program to Play Piano Using Sine Waves on Your Screen

#Credits to Professor Bart Massey for his audio sampler
#This project would have been very tough without it.

import simpleaudio as sa                                 # used to play the wav file
from tkinter import Tk, Frame, Label, PhotoImage, BOTH   # used for the keyboard visuals
import numpy as np                                       # basic python library
import sampler                                           # importing Professor Massey's sampler
from scipy.io.wavfile import read, write                 # used to write wav files

# smooth out the sine wave
def smoothing(array, window_len = 13):
    cumsum_vec = np.cumsum(np.insert(array, 0, 0))
    ma_vec = (cumsum_vec[window_len:] - cumsum_vec[:-window_len]) / window_len
    return ma_vec

# create a list of 36 notes; each note is represented by a sine wave
# the notes are created from the base note, C3, using semitones
# the notes array consists of a list of 36 sine waves
def list_of_notes(notes_count, base_note):
    loop = sampler.Loop(base_note)
    for n in range(notes_count):
        if n != 0:
            factor = 2**(n / 12)  # semitones factor
            new_note = loop.sample(131 * factor, 44100)  # what the new note is
            new_note = smoothing(new_note)  # smooth out the note
            notes.append(new_note)  # add that to the note array 

# write out the wave file
def wavwrite(f, s):
  write(f, 44100, (32767 * s).astype(np.int16))

# the notes array consists of a list of 36 sine waves
notes = []

# C3 is our base note that is generated from a sine wave
C3 = np.sin(np.linspace(0., 2. * np.pi * 131, 44100))

# add the C3 note to the notes array 
notes.append(C3)

# list_of_notes contains our 36 notes
list_of_notes(36, C3)

# plays the wav file associated with the key      
def play_note(event):
  new_note = notes[event.widget.index]  # create a new note
  wavwrite("generated.wav", new_note) # write the note out to generated.wav

  # wavefile object
  w = sa.WaveObject.from_wave_file('generated.wav')
 
  # play generated.wav 
  w.play()

# class that initializes the keyboard 
class Keyboard(Frame):

  # basic class initialization 
  def __init__(self, parent):
    Frame.__init__(self, parent)  # initialize the window that 
                                  # contains the keyboard
    self.parent = parent          # this makes sure that the parent 
                                  # process stays in bound
                
    self.initialize()             # initialize the 3 octaves on the 
                                  # keyboard

  # initialize the 3 octaves on the keybord
  # index 0: contains the position of the key on the screen, start
  # at position 0
  # index 1: contains the name of the key, i.e. C3 for natural keys, 
  # C#3 for sharp keys
  # index 2: contains the index of the key, this will be used to play 
  # its corresponding wav file 
  def initialize(self):
    keyname = [
      [0, 'C3', 0],
      [35, 'C#3', 1],
      [50, 'D3', 2],
      [85, 'D#3', 3],
      [100, 'E3', 4],
      [150, 'F3', 5],
      [185, 'F#3', 6],
      [200, 'G3', 7],
      [235, 'G#3', 8],
      [250, 'A3', 9],
      [285, 'A#3', 10],
      [300, 'B3', 11],
      [350, 'C4', 12],
      [385, 'C#4', 13],
      [400, 'D4', 14],
      [435, 'D#4', 15],
      [450, 'E4', 16],
      [500, 'F4', 17],
      [535, 'F#4', 18],
      [550, 'G4', 19],
      [585, 'G#4', 20],
      [600, 'A4', 21],
      [635, 'A#4', 22],
      [650, 'B4', 23], 
      [700, 'C5', 24], 
      [735, 'C#5', 25], 
      [750, 'D5', 26], 
      [785, 'D#5', 27], 
      [800, 'E5', 28], 
      [850, 'F5', 29], 
      [885, 'F#5', 30], 
      [900, 'G5', 31], 
      [935, 'G#5', 32], 
      [950, 'A5', 33], 
      [985, 'A#5', 34], 
      [1000, 'B5', 35]
    ]

    # name the window 
    self.parent.title('SinePiano')
       
    # if the name of the note has length 2, like C3, it is a 
    # natural note, and so, gets assigned its corresponding picture 
    for k in keyname:
      if len(k[1]) == 2:
        img = 'images/nat.gif'
        k.append(self.build(img, k))  # this puts the label on the image

    # if the name of the note has length 3, like C#3, it is a
    # sharp note, and so, gets assigned its corresponding picture
    for k in keyname:
      if len(k[1]) == 3:
        img = 'images/sharp.gif'
        k.append(self.build(img, k))  # this puts the label on the image

    # set the width and height of the keyboard window
    width, height = 1050, 190

    # set up the screen width and screen height
    # the next few lines of code stem from "A Concise Introduction to Programming 
    # in Python" by Mark J. Johnson: Chapter 28, Graphical User Interfaces
    screen_width, screen_height = self.parent.winfo_screenwidth(), self.parent.winfo_screenheight()
    x, y = (screen_width - width) / 2, (screen_height - height) / 2
    
    # set up the screen with the screen width, height, x, and y 
    self.parent.geometry('%dx%d+%d+%d' % (width, height, x, y))
    
    # set the key name  
    self.parent.keyname = keyname

    # this line of code was taken from the website, "The Tkinter Pack Geometry Manager" 
    # this line of code makes sure that the items in the screen window, stay within 
    # the screen window
    self.pack(fill = BOTH, expand = 1)

  # key visuals
  def build(self, img, k):
    # this line of code was taken from the website, "The Tkinter PhotoImage Class" 
    key_image = PhotoImage(file = img)
    
    # label the image 
    key_name = Label(self, image = key_image)
    key_name.image = key_image
    key_name.place(x = k[0], y = 0)             # k[0] has the position of the key 
    key_name.name = k[1]                        # k[1] has the key name
    key_name.index = k[2]                       # k[2] has the index of the key 
    key_name.bind('<Button-1>', play_note)      # binding for the key 
    return key_name

# main 
def main():
  root = Tk()              # intialize
  start = Keyboard(root)   # start the keyboard program 
  start.mainloop()         # keep the screen open 

# main 
if __name__ == '__main__':
    main()
