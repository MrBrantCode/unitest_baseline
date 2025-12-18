"""
QUESTION:
Write a function named `conjugate_verb` that takes a verb as an argument and returns a JSON string containing the conjugations of the verb for the present, past, future, perfect, continuous, and perfect continuous tenses. The JSON string should be formatted with indentation. The function should handle regular verb conjugations by adding "s" or "ed" to the verb as needed, and should also handle irregular verb conjugations for the present continuous, past perfect, and past perfect continuous tenses. 

The JSON string should be in the following format:
```json
{
    "present": {
        "first_singular": "",
        "second_singular": "",
        "third_singular": "",
        "first_plural": "",
        "second_plural": "",
        "third_plural": ""
    },
    "past": {
        "first_singular": "",
        "second_singular": "",
        "third_singular": "",
        "first_plural": "",
        "second_plural": "",
        "third_plural": ""
    },
    "future": {
        "first_singular": "",
        "second_singular": "",
        "third_singular": "",
        "first_plural": "",
        "second_plural": "",
        "third_plural": ""
    },
    "perfect": {
        "first_singular": "",
        "second_singular": "",
        "third_singular": "",
        "first_plural": "",
        "second_plural": "",
        "third_plural": ""
    },
    "continuous": {
        "first_singular": "",
        "second_singular": "",
        "third_singular": "",
        "first_plural": "",
        "second_plural": "",
        "third_plural": ""
    },
    "perfect_continuous": {
        "first_singular": "",
        "second_singular": "",
        "third_singular": "",
        "first_plural": "",
        "second_plural": "",
        "third_plural": ""
    }
}
```
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