import numpy as np
import sys
import frequency_table
import pygame
import soundfile as sf
import samplerate

#########Test code ##############
def read_notes():
  data, sps = sf.read("C3.wav")
  return data

#Might be a little bit of hardcoding with the MIDI key value for C3
def pitchshift(data, n):
  shift = 1/ (2** (n/12)) #Shift by one semitone
  converter = 'sinc_fastest'
  output = samplerate.resample(data, shift, converter)
  
  sf.write("test" + str(n) + ".wav", output, 44100, subtype= 'PCM_24')

def list_of_wave():
  amplitude = np.iinfo(np.int16).max
  t = np.linspace(0., 1., 48000)  #Check my math and code here
  notes = []
  for value in frequency_table.frequency.values():
    x = (0.5 * amplitude * np.sin(2 * np.pi * value * t)).astype(np.int16)
    notes.append(x)
  return np.array(notes)

def main(): 
  keys = np.loadtxt("keys-copy.txt", dtype= str)
  array = read_notes()
  pitchshift(array,1)
  pitchshift(array,2)
  sines = list_of_wave() #Return the a 2d array with each row is a sine wave for each notes

  pygame.mixer.init(44100, -16, 1, 2048) #Initialize the mixer. This must happen before anything else with pygame sound

  #Mapping, uncomment to have the keyboard map
  sounds = map(pygame.sndarray.make_sound, sines) #Copying the line 100 from the git.  The idea is the same
  keyboard = dict(zip(keys, sounds)) #Ziping the key to sound

if __name__ == "__main__":
  main()





