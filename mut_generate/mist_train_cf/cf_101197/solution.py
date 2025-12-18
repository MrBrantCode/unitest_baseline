"""
QUESTION:
Create a function `rearrange_sentence(sentence)` that takes a string sentence as input, containing the words "company", "new", "plan", "publicize", and "the" in any order. The function should rearrange these words to form a grammatically correct sentence and return the rearranged sentence as a string. The function should assume that the input sentence contains exactly one occurrence of each of the required words. If the input is missing any of the required words, the function should return an error message.
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