"""
QUESTION:
Create a function `conjugate_verb` that takes a verb as input and returns a JSON string containing the conjugations of the verb in the present, past, future, perfect, continuous, and perfect continuous tenses. The function should return the conjugations for the first, second, and third persons in both the singular and plural forms.
"""

import json
def conjugate_verb(verb):
    present = {
        "first_singular": verb,
        "second_singular": verb + "s",
        "third_singular": verb + "s",
        "first_plural": verb,
        "second_plural": verb + "s",
        "third_plural": verb
    }
    past = {
        "first_singular": verb + "ed",
        "second_singular": verb + "ed",
        "third_singular": verb + "ed",
        "first_plural": verb + "ed",
        "second_plural": verb + "ed",
        "third_plural": verb + "ed"
    }
    future = {
        "first_singular": "will " + verb,
        "second_singular": "will " + verb,
        "third_singular": "will " + verb,
        "first_plural": "will " + verb,
        "second_plural": "will " + verb,
        "third_plural": "will " + verb
    }
    perfect = {
        "first_singular": "have " + verb + "ed",
        "second_singular": "have " + verb + "ed",
        "third_singular": "has " + verb + "ed",
        "first_plural": "have " + verb + "ed",
        "second_plural": "have " + verb + "ed",
        "third_plural": "have " + verb + "ed"
    }
    continuous = {
        "first_singular": "am " + verb + "ing",
        "second_singular": "are " + verb + "ing",
        "third_singular": "is " + verb + "ing",
        "first_plural": "are " + verb + "ing",
        "second_plural": "are " + verb + "ing",
        "third_plural": "are " + verb + "ing"
    }
    perfect_continuous = {
        "first_singular": "have been " + verb + "ing",
        "second_singular": "have been " + verb + "ing",
        "third_singular": "has been " + verb + "ing",
        "first_plural": "have been " + verb + "ing",
        "second_plural": "have been " + verb + "ing",
        "third_plural": "have been " + verb + "ing"
    }
    conjugations = {
        "present": present,
        "past": past,
        "future": future,
        "perfect": perfect,
        "continuous": continuous,
        "perfect_continuous": perfect_continuous
    }
    return json.dumps(conjugations, indent=4)