"""
QUESTION:
You have to build a pyramid.

This pyramid should be built from characters from a given string.

You have to create the code for these four methods:
```python
watch_pyramid_from_the_side(characters):

watch_pyramid_from_above(characters):

count_visible_characters_of_the_pyramid(characters):

count_all_characters_of_the_pyramid(characters):
```

The first method ("FromTheSide") shows the pyramid as you would see from the side.
The second method ("FromAbove") shows the pyramid as you would see from above.
The third method ("CountVisibleCharacters") should return the count of all characters, that are visible from outside the pyramid.
The forth method ("CountAllCharacters") should count all characters of the pyramid. Consider that the pyramid is completely solid and has no holes or rooms in it.

Every character will be used for building one layer of the pyramid. So the length of the given string will be the height of the pyramid. Every layer will be built with stones from the given character. There is no limit of stones.
The pyramid should have perfect angles of 45 degrees.

Example: Given string: "abc"

Pyramid from the side:
```
  c
 bbb
aaaaa
```
Pyramid from above:
```
aaaaa
abbba
abcba
abbba
aaaaa
```
Count of visible stones/characters: 
```
25
```
Count of all used stones/characters:
```
35
```

There is no meaning in the order or the choice of the characters. It should work the same for example "aaaaa" or "54321".

Hint: Your output for the side must always be a rectangle! So spaces at the end of a line must not be deleted or trimmed!

If the string is null or empty, you should exactly return this value for the watch-methods and -1 for the count-methods.

Have fun coding it and please don't forget to vote and rank this kata! :-) 

I have created other katas. Have a look if you like coding and challenges.
"""

def build_pyramid(characters):
    def watch_pyramid_from_the_side(characters):
        if not characters:
            return characters
        baseLen = len(characters) * 2 - 1
        return '\n'.join((' ' * i + characters[i] * (baseLen - 2 * i) + ' ' * i for i in range(len(characters) - 1, -1, -1)))

    def watch_pyramid_from_above(characters):
        if not characters:
            return characters
        baseLen = len(characters) * 2 - 1
        return '\n'.join((characters[0:min(i, baseLen - 1 - i)] + characters[min(i, baseLen - 1 - i)] * (baseLen - 2 * min(i, baseLen - 1 - i)) + characters[0:min(i, baseLen - 1 - i)][::-1] for i in range(baseLen)))

    def count_visible_characters_of_the_pyramid(characters):
        return -1 if not characters else (len(characters) * 2 - 1) ** 2

    def count_all_characters_of_the_pyramid(characters):
        return -1 if not characters else sum(((2 * i + 1) ** 2 for i in range(len(characters))))

    return {
        'from_the_side': watch_pyramid_from_the_side(characters),
        'from_above': watch_pyramid_from_above(characters),
        'visible_characters_count': count_visible_characters_of_the_pyramid(characters),
        'all_characters_count': count_all_characters_of_the_pyramid(characters)
    }