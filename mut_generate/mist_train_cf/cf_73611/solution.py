"""
QUESTION:
Create a function `optimized_bubble_sort(arr)` that sorts an array of Morse code numbers in ascending order. The function should break off immediately after a pass in which no swaps are required. Additionally, include helper functions `encode(n)` to convert Arabic numbers to Morse code and `decode(morse)` to convert Morse code to Arabic numbers. The input array consists of Morse code numbers represented as strings of dots (.) and dashes (-). The function should return the sorted array in Morse code.
"""

def encode(n):
    """Converts an Arabic number to Morse code."""
    morse_code = {
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----"
    }
    return morse_code.get(n, "")

def decode(morse):
    """Converts Morse code to an Arabic number."""
    morse_code = {
        ".----": "1",
        "..---": "2",
        "...--": "3",
        "....-": "4",
        ".....": "5",
        "-....": "6",
        "--...": "7",
        "---..": "8",
        "----.": "9",
        "-----": "0"
    }
    return morse_code.get(morse, "")

def optimized_bubble_sort(arr):
    """
    Sorts an array of Morse code numbers in ascending order.
    
    The function breaks off immediately after a pass in which no swaps are required.
    
    Args:
        arr (list): A list of Morse code numbers as strings.
    
    Returns:
        list: The sorted array in Morse code.
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            a = decode(arr[j])
            b = decode(arr[j + 1])
            if a > b:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr