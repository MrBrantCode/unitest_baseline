"""
QUESTION:
Write a function `categorize_amplitudes` that takes a list of frequency-amplitude pairs and categorizes the amplitudes into the appropriate buckets based on the given frequency ranges. The function should return a dictionary containing the categorized amplitudes for each bucket.

The input is a list of tuples where each tuple contains a frequency (int) and its corresponding amplitude (float). The frequency ranges and corresponding buckets are defined as follows: 
- Frequencies less than 875 do not fall into any bucket.
- Frequencies between 875 (inclusive) and 1250 (exclusive) fall into the "mid1bucket".
- Frequencies between 1250 (inclusive) and 1625 (exclusive) fall into the "mid2bucket".
- Frequencies between 1625 (inclusive) and 2000 (exclusive) fall into the "mid3bucket".

The output should be a dictionary containing the categorized amplitudes for each bucket, with keys "mid1bucket", "mid2bucket", and "mid3bucket". The input list size is between 1 and 1000 (inclusive).
"""

from typing import List, Tuple, Dict

def categorize_amplitudes(freq_amp_pairs: List[Tuple[int, float]]) -> Dict[str, List[float]]:
    categorized_amplitudes = {
        "mid1bucket": [],
        "mid2bucket": [],
        "mid3bucket": []
    }

    for freq, amp in freq_amp_pairs:
        if 875 <= freq < 1250:
            categorized_amplitudes["mid1bucket"].append(amp)
        elif 1250 <= freq < 1625:
            categorized_amplitudes["mid2bucket"].append(amp)
        elif 1625 <= freq < 2000:
            categorized_amplitudes["mid3bucket"].append(amp)

    return categorized_amplitudes