import numpy as np
import sys
import frequency_table

##THIS IS ALL A TEST
#create an list of sine waves for each note
def list_of_wave():
  amplitude = np.iinfo(np.int16).max
  t = np.linspace(0., 3., 48000) 
  notes = []
  for value in frequency_table.frequency.values():
    x =(0.5 * amplitude * np.sin(2 * np.pi * value * t)).astype(np.int16)
    notes.append(x)

  return notes  




