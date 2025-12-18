"""
QUESTION:
Write a function named 'parse_binary_data' that takes a binary data string as input and returns the extracted heart rate recordings and corresponding timestamps. Assume the structure of the binary data is unknown and needs to be reverse-engineered.
"""

import struct

def parse_binary_data(binary_data):
    # Use the struct library to unpack the binary data
    # Assuming the structure is a sequence of 4-byte integers for the timestamp 
    # followed by a 2-byte integer for the heart rate
    heart_rate_recordings = []
    timestamps = []
    
    for i in range(0, len(binary_data), 6):
        data = binary_data[i:i+6]
        # Unpack the data into timestamp and heart rate
        timestamp, heart_rate = struct.unpack('!IH', data)
        heart_rate_recordings.append(heart_rate)
        timestamps.append(timestamp)
        
    return heart_rate_recordings, timestamps