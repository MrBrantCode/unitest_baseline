"""
QUESTION:
Create a class `AudioRecording` with methods `is_recording` and `length`. The class should have attributes `Recording`, `LengthHigh`, and `LengthLow`. The `is_recording` method should return a boolean value indicating whether the recording is in progress based on the `Recording` attribute. The `length` method should calculate and return the total length of the recording in milliseconds by combining the `LengthHigh` and `LengthLow` attributes using bitwise operations. The `Recording` attribute value greater than 0 indicates an ongoing recording. The `LengthHigh` and `LengthLow` attributes represent the high and low bits of the recording length, respectively, with the `LengthHigh` value requiring a 7-bit left shift for combination.
"""

def entance(recording, length_high, length_low):
    recording_in_progress = recording > 0
    total_length = (length_high << 7) | length_low
    return recording_in_progress, total_length