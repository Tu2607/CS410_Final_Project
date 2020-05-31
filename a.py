import numpy as np
import sys
import pygame
import time
from tkinter import Tk, Frame, BOTH, Label, PhotoImage
import simpleaudio as sa
from _thread import start_new_thread

def list_of_wave(): 
  amplitude = np.iinfo(np.int16).max
  t = np.linspace(0., 1., 48000)
  notes = []
  for value in frequency_table.frequency.values(): 
    x = (0.5 * amplitude * np.sin(2 * np.pi * value * t)).astype(np.int16)
    notes.append(x)
  return np.array(notes)

def press(event):
   ## where the sound goes
   return

def release(event):
    note = DICTIONARY.get(event.char, None)  ## was using a dictionary at first
    if note:
        if len(note) == 3:
            img = 'img/flat_sharp.gif'
        else:
            img = 'img/nat.gif'
        disp = PhotoImage(file=img)
        find_label(note, event.widget.keys).configure(image = disp)
        find_label(note, event.widget.keys).image = disp

def press_label(event):
  if len(event.widget.name) == 2:
    img = 'img/nat_pressed.gif'
  else:
    img = 'img/flat_sharp.gif'
  disp = PhotoImage(file = img)
  event.widget.configure(image = disp)
  event.widget.image = disp

def release_label(event):
  if len(event.widget.name) == 2:
    img = 'img/nat.gif'
  else:
    img = 'img/flat_sharp.gif'
  disp = PhotoImage(file=img)
  event.widget.configure(image = disp)
  event.widget.image = disp

def find_label(name, array):
    for x in range(len(array)):
        if name == array[x][1]:
            return array[x][2]

class Keyboard(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.init_board()

    def init_board(self):
        keys = [
            [0, 'C3'],
            [45, 'C#3'],
            [60, 'D3'],
            [95, 'D#3'],
            [110, 'E3'],
            [160, 'F3'],
            [195, 'F#3'],
            [210, 'G3'],
            [245, 'G#3'],
            [260, 'A3'],
            [295, 'A#3'],
            [310, 'B3'],
            [360, 'C4'],
            [395, 'C#4'],
            [410, 'D4'],
            [445, 'D#4'],
            [460, 'E4'],
            [510, 'F4'],
            [545, 'F#4'],
            [560, 'G4'],
            [595, 'G#4'],
            [610, 'A4'],
            [645, 'A#4'],
            [660, 'B4'], 
            [695, 'C5'], 
            [710, 'C#5'], 
            [745, 'D5'], 
            [760, 'D#5'], 
            [795, 'E5'], 
            [810, 'F5'], 
            [845, 'F#5'], 
            [860, 'G5'], 
            [895, 'G#5'], 
            [910, 'A5'], 
            [945, 'A#5'], 
            [960, 'B5']
        ]

        for k in keys:
            if len(k[1]) == 2:
                img = 'img/nat.gif'
                k.append(self.disp_key(img, k))

        for k in keys:
            if len(k[1]) == 3:
                img = 'img/flat_sharp.gif'
                k.append(self.disp_key(img, k))

        board_width, board_height = 1050, 300
        screen_width, screen_height = self.parent.winfo_screenwidth(), self.parent.winfo_screenheight()
        x_axis, y_axis = (screen_width - board_width) / 2, (screen_height - board_height) / 2
        self.parent.geometry('%dx%d+%d+%d' % (board_width, board_height, x_axis, y_axis))

        self.parent.keys = keys
        self.parent.bind('<KeyPress>', press)
        self.parent.bind('<KeyRelease>', release)
        self.pack(fill=BOTH, expand = 2)

    def disp_key(self, img, key):
        key_disp = PhotoImage(file=img)
        label = Label(self, image = key_disp, bd = 0)
        label.image = key_disp
        label.name = key[1]
        label.place(x = key[0], y=0)
        return label

def main():
    root = Tk()
    app = Keyboard(root)
    app.mainloop()

if __name__ == '__main__':
    main()
