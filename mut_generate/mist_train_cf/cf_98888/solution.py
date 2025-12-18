"""
QUESTION:
Create a Python function `rearrange_sentence(sentence)` that takes a sentence as input and rearranges the words "company", "new", "plan", "publicize", and "the" to form a grammatically correct sentence. The words can appear in any order in the input sentence. If any of the required words are missing, the function should return an error message.
"""

def rearrange_sentence(sentence):
    words = sentence.split()
    company, new, plan, publicize, the = None, None, None, None, None
    for word in words:
        if "company" in word:
            company = word
        elif "new" in word:
            new = word
        elif "plan" in word:
            plan = word
        elif "publicize" in word:
            publicize = word
        elif "the" in word:
            the = word
    if company and new and plan and publicize and the:
        rearranged = f"{the.capitalize()} {company}'s {new} {plan} is to {publicize}"
        return rearranged
    else:
        return "Sentence is missing one or more required words"