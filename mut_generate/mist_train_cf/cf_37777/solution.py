"""
QUESTION:
Implement the `cfar_nms` function, which takes a 2D array `peaks`, a range of azimuth values `range_az`, and a threshold as input, and returns the updated `peaks` array after applying non-maximum suppression. The `cfar_nms` function should consider a 3x3 neighborhood for each element in the `peaks` array and retain only local maxima that are greater than or equal to the given threshold.
"""

import numpy as np

def cfar_nms(peaks, range_az, threshold):
    # Perform non-maximum suppression
    suppressed_peaks = np.copy(peaks)
    for i in range(1, peaks.shape[0] - 1):
        for j in range(1, peaks.shape[1] - 1):
            if peaks[i, j] >= threshold and peaks[i, j] > peaks[i-1, j-1] and peaks[i, j] > peaks[i-1, j] and peaks[i, j] > peaks[i-1, j+1] and peaks[i, j] > peaks[i, j-1] and peaks[i, j] > peaks[i, j+1] and peaks[i, j] > peaks[i+1, j-1] and peaks[i, j] > peaks[i+1, j] and peaks[i, j] > peaks[i+1, j+1]:
                suppressed_peaks[i, j] = peaks[i, j]
            else:
                suppressed_peaks[i, j] = 0
    return suppressed_peaks