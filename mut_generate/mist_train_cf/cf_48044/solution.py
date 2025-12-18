"""
QUESTION:
Write a function called `count_triplets` that takes a string and a character triplet as input and returns the frequency of the triplet in the string, considering only continuous characters. The function should count the occurrences of the triplet in the string and return the total count.
"""

def count_triplets(string, triplet):
    count = sum(1 for i in range(len(string) - 2) if string[i:i+3] == triplet)
    return count