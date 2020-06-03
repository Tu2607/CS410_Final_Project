import simpleaudio as sa
from tkinter import Tk, Frame, Label, PhotoImage, BOTH
from _thread import start_new_thread

DICTIONARY = {
    '`': 'C1',
    '1': 'D1',
    '2': 'E1',
    '3': 'F1',
    '4': 'G1',
    '5': 'A1',
    '6': 'B1',
    '7': 'C2',
    '8': 'D2',
    '9': 'E2',
    '0': 'F2',
    '-': 'G2',
    '=': 'A2',
    'q': 'B2',
    'w': 'C3',
    'e': 'D3',
    'r': 'E3',
    't': 'F3',
    'y': 'G3',
    'u': 'A3',
    'i': 'B3',
    'o': 'C4',
    'p': 'D4',
    'a': 'E4',
    's': 'F4',
    'd': 'G4',
    'f': 'A4',
    'g': 'B4',
    'h': 'C5',
    'j': 'D5',
    'k': 'E5',
    'l': 'F5',
    ';': 'G5',
    'z': 'A5',
    'x': 'B5',
    'c': 'C6',
    'v': 'D6',
    'b': 'E6',
    'n': 'F6',
    'm': 'G6',
    ',': 'A6',
    '.': 'B6',
    '~': 'C#1',
    '!': 'D#1',
    '#': 'F#1',
    '$': 'G#1',
    '%': 'A#1',
    '&': 'C#2',
    '*': 'D#2',
    ')': 'F#2',
    '_': 'G#2',
    '+': 'A#2',
    'W': 'C#3',
    'E': 'D#3',
    'T': 'F#3',
    'Y': 'G#3',
    'U': 'A#3',
    'O': 'C#4',
    'P': 'D#4',
    'S': 'F#4',
    'D': 'G#4',
    'F': 'A#4',
    'H': 'C#5',
    'J': 'D#5',
    'L': 'F#5',
    ':': 'G#5',
    'Z': 'A#5',
    'C': 'C#6',
    'V': 'D#6',
    'N': 'F#6',
    'M': 'G#6',
    '<': 'A#6'
}

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

# plays the key that's linked to what the user hit
def play_sound(event):
  if n:
    w = sa.WaveObject.from_wave_file('test' + n + '.wav')
    w.play()
  visual = PhotoImage(file = img)
  search_key(n, event.widget.keyname).configure(image = visual)
  search_key(n, event.widget.keyname).image = visual
  
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
      [0, 'C1'],
      [35, 'C#1'],
      [50, 'D1'],
      [85, 'D#1'],
      [100, 'E1'],
      [150, 'F1'],
      [185, 'F#1'],
      [200, 'G1'],
      [235, 'G#1'],
      [250, 'A1'],
      [285, 'A#1'],
      [300, 'B1'],
      [350, 'C2'],
      [385, 'C#2'],
      [400, 'D2'],
      [435, 'D#2'],
      [450, 'E2'],
      [500, 'F2'],
      [535, 'F#2'],
      [550, 'G2'],
      [585, 'G#2'],
      [600, 'A2'],
      [635, 'A#2'],
      [650, 'B2'], 
      [700, 'C3'], 
      [735, 'C#3'], 
      [750, 'D3'], 
      [785, 'D#3'], 
      [800, 'E3'], 
      [850, 'F3'], 
      [885, 'F#3'], 
      [900, 'G3'], 
      [935, 'G#3'], 
      [950, 'A3'], 
      [985, 'A#3'], 
      [1000, 'B3'],
      [1050, 'C4'], 
      [1085, 'C#4'], 
      [1100, 'D4'], 
      [1135, 'D#4'], 
      [1150, 'E4'], 
      [1200, 'F4'], 
      [1235, 'F#4'], 
      [1250, 'G4'], 
      [1285, 'G#4'], 
      [1300, 'A4'], 
      [1335, 'A#4'], 
      [1350, 'B4'], 
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

    width, height = 1600, 190
    screen_width, screen_height = self.parent.winfo_screenwidth(), self.parent.winfo_screenheight()
    x, y = (screen_width - width) / 2, (screen_height - height) / 2
    self.parent.geometry('%dx%d+%d+%d' % (width, height, x, y))
    self.parent.keyname = keyname
    self.parent.bind('<KeyPress>', play_sound)
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