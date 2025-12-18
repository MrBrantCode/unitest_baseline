"""
QUESTION:
There are just some things you can't do on television. In this case, you've just come back from having a "delicious" Barth burger and you're set to give an interview. The Barth burger has made you queezy, and you've forgotten some of the import rules of the "You Can't Do That on Television" set.

If you say any of the following words a large bucket of "water" will be dumped on you:
"water", "wet", "wash"
This is true for any form of those words, like "washing", "watered", etc.

If you say any of the following phrases you will be doused in "slime":
"I don't know", "slime"

If you say both in one sentence, a combination of water and slime, "sludge", will be dumped on you.

Write a function, bucketOf(str), that takes a string and determines what will be dumped on your head. If you haven't said anything you shouldn't have, the bucket should be filled with "air". The words should be tested regardless of case.

Examples:


Check out my other 80's Kids Katas:


80's Kids #1: How Many Licks Does It Take
80's Kids #2: Help Alf Find His Spaceship
80's Kids #3: Punky Brewster's Socks
80's Kids #4: Legends of the Hidden Temple
80's Kids #5: You Can't Do That on Television
80's Kids #6: Rock 'Em, Sock 'Em Robots
80's Kids #7: She's a Small Wonder
80's Kids #8: The Secret World of Alex Mack
80's Kids #9: Down in Fraggle Rock 
80's Kids #10: Captain Planet
"""

import re

WATER_PATTERN = re.compile('water|wet|wash', re.I)
SLIME_PATTERN = re.compile("\\bI don't know\\b|slime", re.I)

def determine_bucket_content(said: str) -> str:
    water = bool(WATER_PATTERN.search(said))
    slime = bool(SLIME_PATTERN.search(said))
    
    if water and slime:
        return 'sludge'
    elif water:
        return 'water'
    elif slime:
        return 'slime'
    else:
        return 'air'