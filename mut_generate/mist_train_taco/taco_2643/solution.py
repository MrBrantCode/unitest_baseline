"""
QUESTION:
# Story

John found a path to a treasure, and while searching for its precise location he wrote a list of directions using symbols `"^"`, `"v"`, `"<"`, `">"` which mean `north`, `east`, `west`, and `east` accordingly. On his way John had to try many different paths, sometimes walking in circles, and even missing the treasure completely before finally noticing it.

___

## Task

Simplify the list of directions written by John by eliminating any loops.

**Note**: a loop is any sublist of directions which leads John to the coordinate he had already visited.

___

## Examples

```
simplify("<>>")        ==  ">"
simplify("<^^>v<^^^")  ==  "<^^^^"
simplify("")           ==  ""
simplify("^< > v
    ^   v
> > C > D > >
^   ^   v
^ < B < <
    ^
    A
```

John visits points `A -> B -> C -> D -> B -> C -> D`, realizes that `-> C -> D -> B` steps are meaningless and removes them, getting this path: `A -> B -> (*removed*) -> C -> D`.

```
    ∙ ∙ ∙
    ∙   ∙
> > C > D > >
^   ∙   ∙
^ < B ∙ ∙
    ^
    A
```

Following the final, simplified route John visits points `C` and `D`, but for the first time, not the second (because we ignore the steps made on a hypothetical path), and he doesn't need to alter the directions list anymore.
"""

def simplify_directions(directions: str) -> str:
    new_p = [(0, 0)]
    new_str = ''
    x = 0
    y = 0
    
    for direction in directions:
        if direction == '<':
            x -= 1
        elif direction == '>':
            x += 1
        elif direction == '^':
            y += 1
        elif direction == 'v':
            y -= 1
        
        if (x, y) not in new_p:
            new_p.append((x, y))
            new_str += direction
        else:
            for j in new_p[::-1]:
                if j != (x, y):
                    new_p.pop()
                    new_str = new_str[:-1]
                else:
                    break
    
    return new_str