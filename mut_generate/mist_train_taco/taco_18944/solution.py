"""
QUESTION:
Mr. Khalkhoul, an amazing teacher, likes to answer questions sent by his students via e-mail, but he often doesn't have the time to answer all of them. In this kata you will help him by making a program that finds
some of the answers.

You are given a `question` which is a string containing the question and some `information` which is a list of strings representing potential answers.

Your task is to find among `information` the UNIQUE string that has the highest number of words in common with `question`. We shall consider words to be separated by a single space.

You can assume that:

* all strings given contain at least one word and have no leading or trailing spaces,
* words are composed with alphanumeric characters only

You must also consider the case in which you get no matching words (again, ignoring the case): in such a case return `None/nil/null`.

Mr. Khalkhoul is countin' on you :)
"""

def find_best_answer(question, information):
    # Convert the question to lowercase and split into words
    question_words = set(question.lower().split())
    
    # Initialize variables to track the best match
    best_score = 0
    best_answer = None
    
    # Iterate through each potential answer
    for info in information:
        # Convert the info to lowercase and split into words
        info_words = set(info.lower().split())
        
        # Calculate the number of common words
        common_words = question_words.intersection(info_words)
        score = len(common_words)
        
        # Update the best match if this one is better
        if score > best_score:
            best_score = score
            best_answer = info
    
    # Return the best answer or None if no common words were found
    return best_answer if best_score > 0 else None