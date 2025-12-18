"""
QUESTION:
Create a function `processImageList` that takes a list of image filenames as input. The function should return an empty list if the input list is empty. It should skip processing any filename that is an empty string and perform a specific operation (not specified) on non-empty filenames, storing the results in a new list. The function must handle cases where the input list contains empty strings.
"""

from typing import List

def processImageList(imageList: List[str]) -> List[str]:
    return [filename for filename in imageList if filename != ""]