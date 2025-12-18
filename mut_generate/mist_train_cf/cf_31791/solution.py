"""
QUESTION:
Write a function `extract_unique_sentences(data_dict)` that takes a dictionary `data_dict` containing the keys "sentence" and "label". The "sentence" key maps to a list of lists, where each inner list represents a sentence as a sequence of integers. The "label" key maps to a list of integers representing labels for each sentence. The function should return a new dictionary where the keys are unique sentences from the input data and the values are lists of corresponding labels.
"""

def extract_unique_sentences(data_dict):
    unique_sentences = {}
    for i in range(len(data_dict["sentence"])):
        sentence_tuple = tuple(data_dict["sentence"][i])
        label = data_dict["label"][i]
        if sentence_tuple in unique_sentences:
            unique_sentences[sentence_tuple].append(label)
        else:
            unique_sentences[sentence_tuple] = [label]
    return unique_sentences