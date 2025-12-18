"""
QUESTION:
Rajiv is given a problem in class. 
" Suppose N burnt candles together make a new candle. then how many new candles are created if we start with M candles"

Please refer to similar MCQ Question for clarification.

SAMPLE INPUT
121

SAMPLE OUTPUT
30
"""

def calculate_new_candles(M, N):
    total_new_candles = 0
    remaining_candles = M
    
    while remaining_candles >= N:
        new_candles = remaining_candles // N
        remaining_candles = remaining_candles % N + new_candles
        total_new_candles += new_candles
    
    return total_new_candles