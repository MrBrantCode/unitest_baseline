"""
QUESTION:
Implement the `_load_dataset` function to process a dataset of texts and their corresponding labels. The dataset is represented as a list of tuples, where each tuple contains an integer identifier, a list of strings representing the text, and a list of dictionaries. Each dictionary in the list contains enriched string data. The labels for each text are provided in a separate dictionary, where the integer identifier maps to a set of topic names. 

The function should return a list of labelized texts, where a labelized text is a tuple containing the text data and a set of topic names. 

The input is `texts: List[Tuple[int, List[str], List[Dict]]` and `labels: Dict[int, Set[str]]`. The output should be `List[Tuple[Tuple[List[str], List], Set[str]]]`.
"""

from typing import List, Tuple, Dict, Set


def load_dataset(
    texts: List[Tuple[int, List[str], List[Dict]]], labels: Dict[int, Set[str]]
) -> List[Tuple[Tuple[List[str], List[Dict]], Set[str]]]:
    return [(text[1], text[2], labels[text[0]]) for text in texts]