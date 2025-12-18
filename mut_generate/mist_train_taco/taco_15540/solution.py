"""
QUESTION:
You have been presented with a cipher, your goal is to re-create the cipher with little information. Use the examples provided to see if you can find a solution to how this cipher is made. You will be given no hints, only the handful of phrases that have already been deciphered for you. 

Your only hint: Spaces are left alone, they are not altered in any way. Anytime there is a space, it should remain untouched and in place.

I hope you enjoy, but this one should be genuinely infuriating.
"""

def recreate_cipher(p: str) -> str:
    return ''.join((chr((ord(j) + i % 3 + (i - 1) // 3 - 97) % 26 + 97) if j != ' ' and i != 0 else j for (i, j) in enumerate(p)))