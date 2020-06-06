#Inspiration from Bart Massey Simple Sampler program
#All credits go to him

import sampler
import numpy as np 
from scipy.io.wavfile import read, write
import scipy.signal
import scipy.fftpack
import cmath
import matplotlib.pyplot as plt

notes = []
A3 = np.sin(np.linspace(0., 2. * np.pi * 220, 44100))
notes.append(A3)

def smoothing(array, window_len = 13, window= 'blackman'):
    cumsum_vec = np.cumsum(np.insert(array, 0, 0))
    ma_vec = (cumsum_vec[window_len:] - cumsum_vec[:-window_len]) / window_len

    return ma_vec

    """
    if array.ndim != 1:
        raise ValueError("Not 1d array")
    
    if array.size < window_len:
        raise ValueError("Array too small")

    s = np.r_[array[window_len-1:0:-1], array, array[-2:-window_len-1:-1]]

    w = eval('np.'+window+'(window_len)')

    y = np.convolve(w/w.sum(), s, mode = 'valid')
    return y
    """

def list_of_notes(notes_count, base_note):
    loop = sampler.Loop(base_note)
    for n in range(notes_count):
        if n != 0:
            factor = 2**(n / 12) #semitones factor
            new_note = loop.sample(220 * factor, 44100)
            new_note = smoothing(new_note) 
            notes.append(new_note)

list_of_notes(3, A3)


        



