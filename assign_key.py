import frequency_table
import numpy as np

"""
KEY_DICTIONARY = { 
  '1': 'C3', 
  '2': 'C#3', 
  '3': 'D3', 
  '4': 'D#3', 
  '5': 'E3', 
  '6': 'F3', 
  '7': 'F#3', 
  '8': 'G3', 
  '9': 'G#3', 
  '0': 'A3', 
  'Q': 'A#3', 
  'W': 'B3',
  'E': 'C4', 
  'R': 'C#4', 
  'T': 'D4', 
  'Y': 'D#4', 
  'U': 'E4', 
  'I': 'F4', 
  'O': 'F#4', 
  'P': 'G4', 
  'A': 'G#4', 
  'S': 'A4', 
  'D': 'A#4', 
  'F': 'B4', 
  'G': 'C5', 
  'H': 'C#5', 
  'J': 'D5', 
  'K': 'D#5', 
  'L': 'E5', 
  'Z': 'F5', 
  'X': 'F#5', 
  'C': 'G5', 
  'V': 'G#5', 
  'B': 'A5', 
  'N': 'A#5', 
  'M': 'B5'
}
"""

class Piano(Frame): 
  def __init__(self, parent_process): 
    Frame.__init__(self, parent_process, background = 'White')
    self.parent_process = parent_process
    self.initialize()

  def initialize(self): 
    # 2d array to hold the keys?

#########Test code ##############
#Implement this in a function later
def list_of_wave():
  amplitude = np.iinfo(np.int16).max
  t = np.linspace(0., 3., 48000) 
  notes = []
  for value in frequency_table.frequency.values():
    x =(0.5 * amplitude * np.sin(2 * np.pi * value * t)).astype(np.int16)
    notes.append(x)
  return np.array(notes)

a = list_of_wave()
b = np.loadtxt("key.txt")
##When we have those array, we can zip them together.