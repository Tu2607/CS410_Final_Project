import numpy
import sys
from tkinter import *
import pygame
from pygame.locals import *

# initialize the pygame modules
pygame.init()

# set the keys to different frequencies / wav files
# having a lot of wav file might look bulky, so we could update 
# these assignments to be frequencies
# the underscores are where the file path games

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


