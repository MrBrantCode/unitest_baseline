"""
QUESTION:
Write a function called `optimize_message` that takes two parameters, `msgP` and `colors_array`, and returns the optimized message string after replacing certain substrings with corresponding color codes. The function should replace '#C0#' with `msgColor` and '#>#' with '\t' in `msgP`, and then replace specific substrings in `msgP` with corresponding color codes from `colors_array`. The function should optimize the replacement operations for better performance and correctness. The `msgColor` variable is assumed to be defined outside the function.
"""

def optimize_message(msgP, colors_array):
    msgP = msgP.replace('#C0#', msgColor)
    msgP = msgP.replace('#>#', '\t')
    for color_pair in colors_array:
        msgP = msgP.replace(color_pair[0], color_pair[1])
    return msgP