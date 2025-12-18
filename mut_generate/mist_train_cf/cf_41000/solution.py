"""
QUESTION:
Write a function `process_csv_data(csv_data)` that takes a list of lists `csv_data` as input, where each inner list represents a line from a CSV file with 13 elements. The function should update a dictionary `h` where the top-level keys are strings, the values corresponding to the top-level keys are dictionaries with keys "oorsprong" and "profiel" that map to dictionaries. The innermost dictionaries should have string keys and integer values. The function should iterate over the `csv_data`, using the 8th element of each line as the top-level key in `h`, the 4th element as the key in the "oorsprong" dictionary, and the 7th element as the key in the "profiel" dictionary. The function should increment the corresponding values in the "oorsprong" and "profiel" dictionaries by the integer value of the 13th element of each line. The function should return the updated dictionary `h`. The initial state of the dictionary `h` should be an empty dictionary.
"""

def process_csv_data(csv_data):
    h = {}
    for line_list in csv_data:
        h[line_list[7]] = h.get(line_list[7], {"oorsprong": {}, "profiel": {}})
        h[line_list[7]]["oorsprong"][line_list[3]] = h[line_list[7]]["oorsprong"].get(line_list[3], 0) + int(line_list[12])
        h[line_list[7]]["profiel"][line_list[6]] = h[line_list[7]]["profiel"].get(line_list[6], 0) + int(line_list[12])
    return h