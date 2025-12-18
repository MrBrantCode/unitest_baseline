"""
QUESTION:
Write a function `find_peaks` that takes an array of integers representing elevation data and returns a list of the highest peaks in the array. A peak is defined as a sequence of continuous ascending values followed by descending values. The function should return all peaks with the highest value. The function should also handle edge cases where the highest peak is at the end of the array or there are multiple peaks with the same highest value.
"""

def find_peaks(data):
    peaks = []
    climbing, peak = False, None

    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            climbing = True
            peak = max(peak, data[i]) if peak is not None else data[i]
        elif data[i] < data[i-1] and climbing:
            peaks.append(peak)
            climbing = False
            peak = None

    if climbing:  # Handle the case that the peak is the last elem in array
        peaks.append(peak)

    # Find the highest peak(s)
    max_peak = max(peaks) if peaks else None  # In case no peak is found, return None
    highest_peaks = [peak for peak in peaks if peak == max_peak]

    return highest_peaks