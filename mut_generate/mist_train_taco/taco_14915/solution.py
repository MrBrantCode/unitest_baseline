"""
QUESTION:
The 26 letters of the English alphabets are randomly divided into 5 groups of 5 letters with the remaining letter being ignored.  Each of the group is assigned a score of more than 0.  The ignored letter always has a score of 0.

With this kata, write a function ```nameScore(name)``` to work out the score of a name that is passed to the function.

The output should be returned as an object:

Only letters have a score. Spaces do not.

You can safely assume that ```name``` does not contain any punctuations or symbols.  There will also be no ```empty string``` or ```null``` value.

A static ```alpha``` object for testing has been preloaded  for your convenience in the following format:

Note that the ```alpha``` object will be randomly generated each time you run the test.

#Example

In accordance to the above ```alpha``` object, the name ```Mary Jane``` will have a name score of ```20``` => M=3 + a=1 + r=4 + y=5 + J=2 + a=1 + n=3 + e=1
"""

def calculate_name_score(name: str, alpha: dict) -> dict:
    # Create a flat dictionary of scores for each letter
    scores = {k: v for (keys, v) in alpha.items() for k in keys}
    
    # Calculate the score for the given name
    name_score = sum((scores.get(a, 0) for a in name.upper()))
    
    # Return the result as a dictionary with the name as the key and the score as the value
    return {name: name_score}