"""
QUESTION:
Create a function `stats` that takes a list of integers and floats as input and returns a dictionary containing the minimum, maximum, mean, and median of the list in a single line of code.
"""

def stats(lst):
    import statistics as st
    return {'Min': min(lst), 'Max': max(lst), 'Mean': st.mean(lst), 'Median': st.median(lst)}