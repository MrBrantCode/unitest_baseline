"""
QUESTION:
You are the judge at a competitive eating competition and you need to choose a winner!

There are three foods at the competition and each type of food is worth a different amount of points.
Points are as follows:

- Chickenwings: 5 points  

- Hamburgers: 3 points   

- Hotdogs: 2 points

Write a function that helps you create a scoreboard. 
It takes as a parameter a list of objects representing the participants, for example:
```
[
  {name: "Habanero Hillary", chickenwings: 5 , hamburgers: 17, hotdogs: 11},
  {name: "Big Bob" , chickenwings: 20, hamburgers: 4, hotdogs: 11}
]
```
It should return 
"name" and "score" properties sorted by score; if scores are equals, sort alphabetically by name.
```
[
  {name: "Big Bob", score: 134},
  {name: "Habanero Hillary", score: 98}
]
```
Happy judging!
"""

def calculate_scoreboard(participants):
    scores = {'chickenwings': 5, 'hamburgers': 3, 'hotdogs': 2}
    
    # Calculate the score for each participant
    result = []
    for person in participants:
        name = person.pop('name')
        score = sum(scores.get(k, 0) * v for k, v in person.items())
        result.append({'name': name, 'score': score})
    
    # Sort the result by score (descending) and by name (ascending) if scores are equal
    result.sort(key=lambda x: (-x['score'], x['name']))
    
    return result