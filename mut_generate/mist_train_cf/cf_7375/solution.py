"""
QUESTION:
Write a function `categorize_sentence(sentence)` that categorizes a given sentence into one of four classes: "Positive Weather Description", "Negative Weather Description", "Neutral Weather Description", or "Weather Description with Emotion". The function should handle sentences that contain both positive and negative weather descriptions, as well as sentences with words or phrases that imply a strong emotional tone.
"""

def categorize_sentence(sentence):
    positive_words = ["sunny", "beautiful", "great", "good", "nice", "lovely", "wonderful", "pleasant", "clear"]
    negative_words = ["rainy", "cloudy", "stormy", "bad", "terrible", "awful", "hate", "badly"]
    emotion_words = ["love", "hate", "lovely", "wonderful", "terrible", "awful"]

    sentence = sentence.lower()
    words = sentence.split()

    positive_count = sum(1 for word in words if word in positive_words)
    negative_count = sum(1 for word in words if word in negative_words)
    emotion_count = sum(1 for word in words if word in emotion_words)

    if positive_count > 0 and negative_count > 0:
        return "Weather Description with Emotion"
    elif emotion_count > 0:
        return "Weather Description with Emotion"
    elif positive_count > 0:
        return "Positive Weather Description"
    elif negative_count > 0:
        return "Negative Weather Description"
    else:
        return "Neutral Weather Description"