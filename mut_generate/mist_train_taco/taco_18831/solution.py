"""
QUESTION:
There is no single treatment that works for every phobia, but some people cure it by being gradually exposed to the phobic situation or object. In this kata we will try curing arachnophobia by drawing primitive spiders.
 
Our spiders will have legs, body, eyes and a mouth. Here are some examples:
```
/\((OOwOO))/\

/╲(((0000w0000)))╱\

^(oWo)^
```
You will be given four values:  
1) `leg size` where each value stands for its own leg type: `1 for "^ ^", 2 for "/\ /\", 3 for "/╲ ╱\", 4 for "╱╲ ╱╲"`  
2) `body size` where each value stands for its own body type: `1 for "( )", 2 for "(( ))", 3 for "((( )))"`  
3) `mouth` representing the spider's mouth  
4) `eye` representing the spider's eye

**Note:** the eyes are symmetric, and their total amount is `2 to the power of body size`.
  
You will also be given only valid data. That's it for the instructions, you can start coding!
"""

def draw_spider(leg_size, body_size, mouth, eye):
    # Define the legs based on the leg_size
    lleg = ['', '^', '/\\', '/╲', '╱╲'][leg_size]
    rleg = ['', '^', '/\\', '╱\\', '╱╲'][leg_size]
    
    # Define the body based on the body_size
    lbody = '(' * body_size
    rbody = ')' * body_size
    
    # Calculate the number of eyes
    eye *= 2 ** (body_size - 1)
    
    # Construct the spider string
    return f'{lleg}{lbody}{eye}{mouth}{eye}{rbody}{rleg}'