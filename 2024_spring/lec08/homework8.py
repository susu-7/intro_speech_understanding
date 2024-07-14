import numpy as np

def dft_matrix(N):
    '''
    Create a DFT transform matrix, W, of size N.
    '''
    k = np.arange(N)
    n = np.arange(N)
    kn = np.outer(k, n)
    W = np.exp(-2j * np.pi * kn / N)
    return W

