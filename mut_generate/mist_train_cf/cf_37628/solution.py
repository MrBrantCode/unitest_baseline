"""
QUESTION:
Implement a function named `build_dataset` that takes a list of words and a vocabulary size as input and returns four values: the processed data, word counts, a dictionary mapping words to unique integer indices, and a reverse dictionary mapping integer indices back to words. The function should process the input list of words, keeping the most frequently occurring words up to the specified vocabulary size and replacing the remaining words with a special 'UNK' token. The function should not use any external libraries other than the standard Python library and NumPy for data processing.
"""

def build_dataset(words, vocabulary_size):
    count = [['UNK', -1]]
    count.extend(collections.Counter(words).most_common(vocabulary_size - 1))
    dictionary = dict()
    for word, _ in count:
        dictionary[word] = len(dictionary)
    data = list()
    unk_count = 0
    for word in words:
        if word in dictionary:
            index = dictionary[word]
        else:
            index = 0  # dictionary['UNK']
            unk_count += 1
        data.append(index)
    count[0][1] = unk_count
    reverse_dictionary = dict(zip(dictionary.values(), dictionary.keys()))
    return data, count, dictionary, reverse_dictionary