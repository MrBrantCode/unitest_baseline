"""
QUESTION:
Write a function named `sequence_analysis` that takes a string of XML data as input, extracts a sequence of letters from it, and returns a tuple containing the frequency of each letter in the sequence and the missing letter in the sequence, if any. The sequence is assumed to be alphabetical and the missing letter is the one that would normally appear between two adjacent letters whose ASCII values differ by more than 1.
"""

def sequence_analysis(xml_data):
    root = ET.fromstring(xml_data)
    sequence = root.text.strip()
    letter_counts = Counter(sequence)
    missing_letter = None
    for i in range(1, len(sequence)):
        if ord(sequence[i]) - ord(sequence[i-1]) != 1:
            missing_letter = chr(ord(sequence[i-1]) + 1)
            break
    return letter_counts, missing_letter