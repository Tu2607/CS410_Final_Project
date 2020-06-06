import simpleaudio as sa
from tkinter import Tk, Frame, Label, PhotoImage, BOTH
from _thread import start_new_thread
import numpy as np
import sampler

def smoothing(array, window_len = 13, window= 'blackman'):
    cumsum_vec = np.cumsum(np.insert(array, 0, 0))
    ma_vec = (cumsum_vec[window_len:] - cumsum_vec[:-window_len]) / window_len
    return ma_vec

def list_of_notes(notes_count, base_note):
    loop = sampler.Loop(base_note)
    for n in range(notes_count):
        if n != 0:
            factor = 2**(n / 12)  #semitones factor
            new_note = loop.sample(131 * factor, 44100)
            new_note = smoothing(new_note) 
            notes.append(new_note)

notes = []
C3 = np.sin(np.linspace(0., 2. * np.pi * 131, 44100))
notes.append(C3)
list_of_notes(36, C3)

# looks for the name of the note in the key array, return the label component
def search_key(name, arr):
  for x in range(len(arr)):
    if name == arr[x][1]:
      return arr[x][2]

# what the user sees when they press down a key
def press(event):
  if len(event.widget.name) == 2:
    img = 'images/nat.gif'
  else: 
    img = 'images/flat_sharp.gif'
  visual = PhotoImage(file = img)
  event.widget.configure(image = visual)
  event.widget.image = visual

# plays the wav file associated with the key      
def button_pressed(event):
  w = sa.WaveObject.from_wave_file('test' + event.widget.name + '.wav')
  w.play()
  press(event)

class Keyboard(Frame):
  def __init__(self, parent):
    Frame.__init__(self, parent)
    self.parent = parent
    self.initialize()

  def initialize(self):
    keyname = [
      [0, 'C3'],
      [35, 'C#3'],
      [50, 'D3'],
      [85, 'D#3'],
      [100, 'E3'],
      [150, 'F3'],
      [185, 'F#3'],
      [200, 'G3'],
      [235, 'G#3'],
      [250, 'A3'],
      [285, 'A#3'],
      [300, 'B3'],
      [350, 'C4'],
      [385, 'C#4'],
      [400, 'D4'],
      [435, 'D#4'],
      [450, 'E4'],
      [500, 'F4'],
      [535, 'F#4'],
      [550, 'G4'],
      [585, 'G#4'],
      [600, 'A4'],
      [635, 'A#4'],
      [650, 'B4'], 
      [700, 'C5'], 
      [735, 'C#5'], 
      [750, 'D5'], 
      [785, 'D#5'], 
      [800, 'E5'], 
      [850, 'F5'], 
      [885, 'F#5'], 
      [900, 'G5'], 
      [935, 'G#5'], 
      [950, 'A5'], 
      [985, 'A#5'], 
      [1000, 'B5']
    ]

    self.parent.title('Virtual Piano')
        
    for k in keyname:
      if len(k[1]) == 2:
        img = 'images/nat.gif'
        k.append(self.build(img, k))

    for k in keyname:
      if len(k[1]) == 3:
        img = 'images/flat_sharp.gif'
        k.append(self.build(img, k))

    width, height = 1050, 190
    screen_width, screen_height = self.parent.winfo_screenwidth(), self.parent.winfo_screenheight()
    x, y = (screen_width - width) / 2, (screen_height - height) / 2
    self.parent.geometry('%dx%d+%d+%d' % (width, height, x, y))
    self.parent.keyname = keyname
    self.pack(fill=BOTH, expand=1)

    # key visuals
  def build(self, img, k):
    key_image = PhotoImage(file=img)
    key_name = Label(self, image=key_image, bd=0)
    key_name.image = key_image
    key_name.place(x=k[0], y=0)
    key_name.name = k[1]
    key_name.bind('<Button-1>', button_pressed)
    return key_name

def main():
  root = Tk()
  start = Keyboard(root)
  start.mainloop()

if __name__ == '__main__':
    main()
