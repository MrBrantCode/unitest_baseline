"""
QUESTION:
If you have ever interacted with a cat, you have probably noticed that they are quite particular about how to pet them. Here is an approximate map of a normal cat.

<image>

However, some cats won't tolerate this nonsense from the humans. Here is a map of a grumpy cat.

<image>

You have met a cat. Can you figure out whether it's normal or grumpy?

Interaction

This is an interactive problem. Initially you're not given any information about the cat. Instead, the cat is divided into ten areas, indexed from 0 to 9. 

In one query you can choose which area you'll pet and print the corresponding index to standard out. You will get the cat's response, as depicted on the corresponding map, via standard in. For simplicity all responses are written in lowercase.

Once you're certain what type of cat you're dealing with, output "normal" or "grumpy" to standard out.

Note

Please make sure to use the stream flushing operation after each query in order not to leave part of your output in some buffer.
"""

def determine_cat_type(response: str) -> str:
    """
    Determines whether the cat is normal or grumpy based on its response to a petting query.

    Parameters:
    response (str): The cat's response to a petting query.

    Returns:
    str: "normal" if the cat is normal, "grumpy" if the cat is grumpy.
    """
    return 'grumpy' if response[-2:] in ['s?', 'le', 'se', 'ay', 'en'] else 'normal'