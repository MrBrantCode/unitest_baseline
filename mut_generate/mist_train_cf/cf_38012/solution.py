"""
QUESTION:
Implement a function `process_data(label_dict, data_dict)` that takes two dictionaries as input: `label_dict` and `data_dict`. 

`label_dict` is a dictionary containing entities as keys and a list of dictionaries as values. Each dictionary in the list contains 'text' and 'start' keys representing the extracted text and its starting position.

`data_dict` is a dictionary containing the original content.

Modify `data_dict` based on the following rules:
- If the entity is 'extension', set the value of 'content' in `data_dict` to the concatenated text from all the entities in `label_dict`.
- If there are duplicate texts for the same entity, update the 'start' value of the duplicate text to be the same as the original text.

Return the modified `data_dict`. 

The 'start' value of the duplicate text should be updated only if the 'text' value is the same as the original text.
"""

def process_data(label_dict: dict, data_dict: dict) -> dict:
    for entity, entities in label_dict.items():
        if entity == 'extension':
            content = ''.join([ent['text'] for ent in entities])
            data_dict['content'] = content

            # Update start value for duplicate texts
            seen_texts = set()
            for ent in entities:
                if ent['text'] in seen_texts:
                    for orig_ent in entities:
                        if orig_ent['text'] == ent['text'] and orig_ent['start'] != ent['start']:
                            orig_ent['start'] = ent['start']
                else:
                    seen_texts.add(ent['text'])

    return data_dict