"""
QUESTION:
Write a function `convert_corpus_to_tensor` that takes a 3-dimensional corpus of 12,000 monochrome, bitmap images, each measured at 24x24 pixels, and returns a 4-dimensional tensor. The resulting tensor should have dimensions representing the number of samples, image height, image width, and channels of the color (with 1 channel for monochrome images).
"""

import numpy as np

def convert_corpus_to_tensor(corpus):
    return np.reshape(corpus, (corpus.shape[0], corpus.shape[1], corpus.shape[2], 1))