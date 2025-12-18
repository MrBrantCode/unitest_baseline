"""
QUESTION:
Write a function `lastIndexOf` that finds the last index of a given substring within a string. The function should return the index of the last occurrence of the substring if it exists, and -1 otherwise. The index should be zero-based.
"""

def lastIndexOf(st, substr):
    if substr in st: 
        start = -1 
        while True: 
            pos = st.find(substr, start + 1) 
            if pos == -1: 
                break 
            start = pos 
        return start 
    else: 
        return -1 