"""
QUESTION:
```if:csharp
## Terminal Game - Create Hero Class

In this first kata in the series, you need to define a Hero class to be used in a terminal game. The hero should have the following attributes:

attribute | type | value
---|---|---
Name | string | user argument or "Hero"
Position | string | "00"
Health | float | 100
Damage | float | 5
Experience | int | 0
```

```if-not:csharp
## Terminal Game - Create Hero Prototype

In this first kata in the series, you need to define a Hero prototype to be used in a terminal game. The hero should have the following attributes:

attribute | value
---|---
name | user argument or 'Hero'
position | '00'
health | 100
damage | 5
experience | 0
```
"""

def create_hero(name='Hero'):
    """
    Creates a Hero object with the specified attributes.

    Parameters:
    name (str): The name of the hero. Defaults to 'Hero' if not provided.

    Returns:
    Hero: An instance of the Hero class with the specified attributes.
    """
    class Hero:
        def __init__(self, name):
            self.name = name
            self.position = '00'
            self.health = 100
            self.damage = 5
            self.experience = 0
    
    return Hero(name)