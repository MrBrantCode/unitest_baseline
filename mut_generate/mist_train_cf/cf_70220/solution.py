"""
QUESTION:
Write a program that compares the four primary programming paradigms: Imperative, Declarative, Functional, and Object-Oriented. Provide a brief description of each paradigm, an instance where it would be most effective, an instance where it would be least effective, and an example of a programming language that uses this paradigm. Additionally, evaluate these paradigms against each other in terms of learnability, expressiveness, and efficiency.
"""

def compare_paradigms(paradigm):
    """
    Compare the four primary programming paradigms: Imperative, Declarative, Functional, and Object-Oriented.

    Args:
        paradigm (str): The name of the paradigm to compare.

    Returns:
        dict: A dictionary containing the description, most effective use case, least effective use case, and example language for the specified paradigm.
    """
    paradigms = {
        "Imperative": {
            "description": "A sequence of instructions that change the state of the computer.",
            "most_effective": "Applications where time is a significant factor, such as video games or GUI based applications.",
            "least_effective": "Higher-level or business problems which demand abstraction.",
            "example_language": "C"
        },
        "Declarative": {
            "description": "Specifies what the program must do, not how it should do it.",
            "most_effective": "Data-focused applications or programs, such as database management and data analysis tools.",
            "least_effective": "If you need complete control over the program’s flow and state.",
            "example_language": "SQL"
        },
        "Functional": {
            "description": "Functions are first-class entities, taking inputs & producing outputs without internal state.",
            "most_effective": "Manipulating data and concurrent programming.",
            "least_effective": "If the problem requires stateful or imperative model.",
            "example_language": "Haskell"
        },
        "Object-Oriented": {
            "description": "Uses instances of classes, known as objects, to carry out tasks.",
            "most_effective": "Building large, complex systems where re-usability of code and abstraction is necessary.",
            "least_effective": "Simple, straight-forward programs and data-intensive tasks that don't map naturally to objects.",
            "example_language": "Java"
        }
    }

    return paradigms.get(paradigm, {})

# Example usage:
print(compare_paradigms("Imperative"))