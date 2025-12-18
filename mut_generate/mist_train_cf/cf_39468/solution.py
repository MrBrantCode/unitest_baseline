"""
QUESTION:
Implement a function `process_sources` that takes in a list of URLs, a dictionary of hosts where each value is a list of language options, and a language mapping dictionary. The function should return a list of tuples, where each tuple contains the language and source type for the corresponding URL. If the language or source type is not found in the mapping, it should be represented as `None`. The language mapping defaults to ('en', None) if no match is found.
"""

def process_sources(urls, hostDict, language_mapping):
    result = []
    for url in urls:
        for host, options in hostDict.items():
            if url in options:
                for lang_type, source_type in language_mapping.items():
                    if lang_type in options:
                        result.append((lang_type, source_type))
                        break
                else:
                    result.append(('en', None))
                break
        else:
            result.append(('en', None))
    return result