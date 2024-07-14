import numpy as np

def minimum_Fs(f):
    '''
    Find the lowest sampling frequency that would avoid aliasing for a pure tone at f Hz.
    '''
    Fs = 2 * f  # Minimum sampling frequency to avoid aliasing
    return Fs

def omega(f, Fs):
    '''
    Find the radial frequency (omega) that matches a given f and Fs.
    '''
    omega = 2 * np.pi * f / Fs  # Angular frequency in radians per sample
    return omega

def pure_tone(omega, N):
    '''
    Create a pure tone of N samples at omega radians/sample.
    '''
    n = np.arange(N)  # Sample indices
    x = np.cos(omega * n)  # Cosine wave at each sample
    return x


