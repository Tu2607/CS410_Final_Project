import numpy as np
import sys
import frequency_table
import pygame
import time


#########Test code ##############
def list_of_wave():
  amplitude = np.iinfo(np.int16).max
  t = np.linspace(0., 1., 48000)  #Check my math and code here
  notes = []
  for value in frequency_table.frequency.values():
    print(value)
    x = (0.5 * amplitude * np.sin(2 * np.pi * value * t)).astype(np.int16)
    notes.append(x)
  return np.array(notes)

def main(): 
  keys = np.loadtxt("keys-copy.txt", dtype= str)
  sines = list_of_wave() #Return the a 2d array with each row is a sine wave for each notes

  pygame.mixer.init(44100, -16, 1, 2048) #Initialize the mixer. This must happen before anything else with pygame sound

  #Test code to make sure that the sound is playing
  a = pygame.sndarray.make_sound(sines[0])
  b = pygame.sndarray.make_sound(sines[1])
  c =  pygame.sndarray.make_sound(sines[2])
  a.play()
  time.sleep(5) #this is needed in order to have sound. weird...
  b.play()
  time.sleep(5)
  c.play()
  time.sleep(5)
  #Mapping, uncomment to have the keyboard map
  #sounds = map(pygame.sndarray.make_sound, sines) #Copying the line 100 from the git.  The idea is the same
  #keyboard = dict(zip(keys, sounds)) #Ziping the key to sound

if __name__ == "__main__":
  main()





