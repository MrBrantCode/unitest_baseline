"""
QUESTION:
Design a Python function called `categorize_text` that categorizes input text into four categories: 'deep learning', 'traditional AI', 'real-time systems', or 'handling ambiguous data'. The function should take a string as input and return the corresponding category as a string.
"""

def categorize_text(input_text):
    categories = {
        'deep learning': ['deep learning', 'neural network', 'machine learning', 'AI', 'pattern recognition'],
        'traditional AI': ['rule-based systems', 'decision trees', 'support vector machines', 'expert systems', 'inference engines'],
        'real-time systems': ['real-time', 'control systems', 'robotics', 'traffic management', 'self-driving cars'],
        'handling ambiguous data': ['ambiguous data', 'noisy data', 'incomplete data', 'adversarial examples']
    }

    input_text = input_text.lower()

    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in input_text:
                return category

    return 'unknown category'