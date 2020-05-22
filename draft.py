import numpy as np
import sys
from tkinter import *
import pygame
from pygame.locals import *

# initialize the pygame modules
pygame.init()

#If we're using a dictionary of keys...
#Have a file that basically have all the keys name so we can just use
#np.loadtxt to read it in
names = np.loadtxt("filename")
keys = {}
for i in range (names.shape[0]):
  keys[names[i]] = frequency # <-- the frequency we can just calculate it by hand and add it into the file


"""
def C_sharp(): 
  note.set("C#")
  sound = pygame.mixer.Sound(_____)
  sound.play()
  return

def D_sharp(): 
  note.set("D#") 
  sound = pygame.mixer.Sound(_____) 
  sound.play()
  return

def F_sharp(): 
  note.set("F#")
  sound = pygame.mixer.Sound(_____)
  sound.play()
  return 
  
def G_sharp(): 
  note.set("G#")
  sound = pygame.mixer.Sound(_____) 
  sound.play()
  return

def B_flat(): 
  note.set("Bb")
  sound = pygame.mixer.Sound(_____)
  sound.play()
  return

# and so on...
"""

