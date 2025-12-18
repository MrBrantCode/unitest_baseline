"""
QUESTION:
Implement a function `process_text_features(text_features_list)` that takes in a list of tuples, where each tuple contains a canonical document ID and a text feature. The function should create a dictionary to store the text features based on their IDs, check for and handle duplicate text features within the same ID, and then serialize the dictionary into a list of examples. Each example in the list should be a dictionary containing the ID and a list of its corresponding text features. The function should return the list of examples.

The input list `text_features_list` is a list of tuples, where each tuple contains a canonical document ID and a text feature. The function should handle duplicate text features by printing a message and skipping the duplicate feature. The output list should not contain any duplicate text features.
"""

def process_text_features(text_features_list):
    id_to_text_features = {}
    for canonical_doc_id, text_features in text_features_list:
        if canonical_doc_id in id_to_text_features:
            if text_features in id_to_text_features[canonical_doc_id]:
                print(f'duplicate txt found! file: {text_features}')
                print(text_features, id_to_text_features[canonical_doc_id])
                continue
        else:
            id_to_text_features[canonical_doc_id] = []
        id_to_text_features[canonical_doc_id].append(text_features)
    return [{'id': doc_id, 'features': features} for doc_id, features in id_to_text_features.items()]