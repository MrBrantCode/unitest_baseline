"""
QUESTION:
Write a function `detect_scene_change` that identifies potential scene changes in a given text. The function should take a text as input and return a list of indices where a scene change is likely to have occurred. The input text is a novel or story with multiple scenes and may not have a list of character names. There may be nameless NPCs. The function should use Natural Language Processing (NLP) techniques to detect scene changes.
"""

def detect_scene_change(text):
    # Implement your chosen NLP technique(s) here.
    # This is a placeholder for your actual implementation.
    # For example, using a simple approach based on transition phrases:
    transition_phrases = ["meanwhile", "later", "the next day"]
    scene_changes = []
    sentences = text.split(". ")
    for i, sentence in enumerate(sentences):
        for phrase in transition_phrases:
            if phrase in sentence.lower():
                scene_changes.append(i)
    return scene_changes