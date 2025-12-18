"""
QUESTION:
Implement a function `process_calibration_data(info)` that takes a dictionary `info` containing information about the detector dimensions, the number of frames, and calibration data. The function should process the calibration data based on the provided information and return the processed calibration data as a numpy array. The function should support two formats of calibration data: individual sets for each frame under keys 'Calibration_data_for_frame_X', or a single set for all frames under the key 'Calibration_data'. The function should flip the calibration data vertically and use polynomial interpolation to generate the calibration values for each pixel. The shape of the output array should be (info['NumberOfFrames'], width) for individual calibration data or (width,) for a single calibration data, where `width` is the first element of `info['DetectorDimensions']`.
"""

import numpy as np

def process_calibration_data(info):
    width = info['DetectorDimensions'][0]
    
    if 'Calibration_data_for_frame_1' in info:
        calibration = np.ndarray((info['NumberOfFrames'], width))
        for f in range(len(calibration)):
            key = 'Calibration_data_for_frame_{:d}'.format(f + 1)
            flip_coef = np.flipud(info[key])
            calibration[f] = np.poly1d(flip_coef)(np.arange(1, width + 1))
        return calibration
    elif 'Calibration_data' in info:
        flip_coef = np.flipud(info['Calibration_data'])
        return np.poly1d(flip_coef)(np.arange(1, width + 1))