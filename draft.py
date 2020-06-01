import numpy as np
import sys
import pygame
import soundfile as sf
import samplerate

#########Test code ##############
def read_notes():
  data, sps = sf.read("C3.wav")
  return data, sps

#Might be a little bit of hardcoding with the MIDI key value for C3
def pitchshift(data, amount_of_notes):
  notes = []
  for n in range(amount_of_notes):
    #shift = 1/ (2** (n/12)) #Shift by one semitone
    shift = 2**(n/12)
    converter = 'sinc_fastest'
    output = samplerate.resample(data, shift, converter)
    notes.append(output)
  return notes
  
def main(): 
  keys = np.loadtxt("keys-copy.txt", dtype= str)
  array, rate = read_notes()
  list_of_notes = pitchshift(array,36) 

  pygame.mixer.init(rate, -16, 2) #Initialize the mixer. This must happen before anything else with pygame sound

  #Mapping, uncomment to have the keyboard map
  sounds = map(pygame.sndarray.make_sound, list_of_notes) #Copying the line 100 from the git.  The idea is the same
  keyboard = dict(zip(keys, sounds)) #Ziping the key to sound

if __name__ == "__main__":
  main()





