"""
QUESTION:
Implement the function `reorder_sentence(sentence, question_word)` that takes in a string `sentence` representing the input sentence and a string `question_word` representing the question word. The function should reorder the words in the sentence based on the following rules: 

- If the question word is "what" and the sentence starts with a verb matching the first letter of the question word, then the verb is moved after the attribute and before the preposition, the subject is then moved after that, and the answer is placed last. 
- If the question word is "who" or "when", the sentence remains unchanged. 

The function should return the reordered sentence as a string.
"""

def reorder_sentence(sentence: str, question_word: str) -> str:
    words = sentence.split()
    question_word = question_word.lower()
    verb = [word for word in words if word[0].lower() == question_word[0]]
    attribute = None
    subject = None
    answer = None
    preposition = None
    
    if question_word == 'what' and verb and words[0].startswith(str(verb[0])):
        for i, word in enumerate(words):
            if word == verb[0]:
                verb = word
            elif i == 1:
                attribute = word
            elif i == 2:
                preposition = word
            elif i > 2:
                if subject is None:
                    subject = word
                else:
                    answer = word
        return ' '.join([attribute, verb, preposition, subject, answer])
    else:
        return sentence