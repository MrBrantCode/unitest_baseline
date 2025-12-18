"""
QUESTION:
Design a function named `language_info` that takes a programming language name as input and returns its key features, use cases, and drawbacks. The function should support at least five popular programming languages: Python, JavaScript, Java, C++, and Ruby.
"""

def language_info(language):
    """
    Returns key features, use cases, and drawbacks of a given programming language.

    Args:
    language (str): The name of the programming language.

    Returns:
    dict: A dictionary containing the language's key features, use cases, and drawbacks.
    """

    languages = {
        "Python": {
            "key_features": "Simplicity, readability, large standard library, versatility, supports multiple paradigms",
            "use_cases": "Web development, scientific computing, data analysis, AI, ML, automation",
            "drawbacks": "Slower than lower-level languages, limited for real-time applications, Global Interpreter Lock (GIL) limitations"
        },
        "JavaScript": {
            "key_features": "Versatility, event-driven, functional, and object-oriented paradigms, runs in the browser",
            "use_cases": "Web development, creating web applications, mobile apps, server-side applications",
            "drawbacks": "Limited capabilities outside web development, lacks robust multi-threading support, cross-browser compatibility issues"
        },
        "Java": {
            "key_features": "Platform independence, statically-typed, object-oriented, write-once-run-anywhere (WORA) capability",
            "use_cases": "Building large-scale enterprise applications, Android app development, server-side applications",
            "drawbacks": "Steeper learning curve, verbose, garbage collection may lead to performance issues"
        },
        "C++": {
            "key_features": "Low-level system programming, high-performance computing, procedural and object-oriented paradigms, direct memory manipulation",
            "use_cases": "System software, game engines, embedded systems, resource-intensive applications",
            "drawbacks": "Complex and error-prone, manual memory management, potential for undefined behavior"
        },
        "Ruby": {
            "key_features": "Dynamic, object-oriented, scripting language, simplicity, expressiveness, readability",
            "use_cases": "Web development, building web applications, APIs, dynamic websites, scripting, automation",
            "drawbacks": "Slower execution speed, high memory usage, fewer libraries and tools compared to other languages"
        }
    }

    return languages.get(language, "Language not supported")