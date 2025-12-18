"""
QUESTION:
# Task
 Mirko has been moving up in the world of basketball. He started as a mere spectator, but has already reached the coveted position of the national team coach!

 Mirco is now facing a difficult task: selecting five primary players for the upcoming match against Tajikistan. Since Mirko is incredibly lazy, he doesn't bother remembering players' names, let alone their actual skills. That's why he has settled on selecting five players who share the same first letter of their surnames, so that he can remember them easier. If there are no five players sharing the first letter of their surnames, Mirko will simply forfeit the game!

 Your task is to find the first letters Mirko's players' surnames can begin with(In alphabetical order), or return `"forfeit"` if Mirko can't gather a team.

# Input/Output


 - `[input]` string array `players`

  Array of players' surnames, consisting only of lowercase English letters.

 
 - `[output]` a string

  A **sorted** string of possible first letters, or "forfeit" if it's impossible to gather a team.


# Example

For `players = ["michael","jordan","lebron","james","kobe","bryant"]`, the output should be `"forfeit"`.

 For
 ```
 players = ["babic","keksic","boric","bukic",
              "sarmic","balic","kruzic","hrenovkic",
              "beslic","boksic","krafnic","pecivic",
              "klavirkovic","kukumaric","sunkic","kolacic",
              "kovacic","prijestolonasljednikovic"]
```
the output should be "bk".
"""

from collections import Counter

def find_team_letters(players):
    # Count the occurrences of each first letter
    first_letter_counts = Counter(player[0] for player in players)
    
    # Filter letters that appear at least 5 times
    valid_letters = [letter for letter, count in first_letter_counts.items() if count >= 5]
    
    # Sort the valid letters alphabetically
    sorted_letters = ''.join(sorted(valid_letters))
    
    # Return the sorted letters or "forfeit" if no valid letters
    return sorted_letters or "forfeit"