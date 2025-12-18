"""
QUESTION:
Implement the `conv` function, which calculates the cross-correlation scores between a given signal and a template. The function should take two parameters: `signal` (list of integers) and `template` (list of integers). The cross-correlation score at position `i` is calculated as the sum of the element-wise products of the signal and the template, where the template is shifted to align with the signal, and missing signal values are assumed to be 0. The function should return a list of cross-correlation scores.
"""

def conv(signal, template):
    scores = []
    signal_length = len(signal)
    template_length = len(template)

    for i in range(signal_length - template_length + 1):
        score = 0
        for j in range(template_length):
            score += signal[i + j] * template[j]
        scores.append(score)

    return scores