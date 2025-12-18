"""
QUESTION:
Write a function called `analyze_story` that takes a string story and lists of heteronyms, synonyms, and homophones as input, and returns the count of heteronyms, synonyms, and homophones used in the story. The lists of heteronyms, synonyms, and homophones should be lists of tuples or lists, where each tuple or list contains words that are heteronyms, synonyms, or homophones of each other. The function should also construct a simple story using the given lists of words.

Restrictions: The input lists should not be empty and should only contain strings. The input story should not be empty and should be a string. The function should return a dictionary with the counts of heteronyms, synonyms, and homophones. 

Example input: 
- heteronyms = [("lead", "lead"), ("read", "read")]
- synonyms = [["happy", "joyful", "cheerful"], ["sad", "unhappy", "downcast"]]
- homophones = [("here", "hear"), ("knight", "night")]
- story = "lead lead. read read. happy joyful cheerful. sad unhappy downcast. here hear. knight night."
"""

def analyze_story(story, heteronyms, synonyms, homophones):
    def construct_sentence(word_list):
        return ' '.join(word_list)

    def count_words(story, word_list):
        count = 0
        for words in word_list:
            for word in words:
                count += story.count(word)
        return count

    constructed_story = ''
    for heteronym in heteronyms:
        constructed_story += construct_sentence(heteronym) + ". "
    for synonym in synonyms:
        constructed_story += construct_sentence(synonym) + ". "
    for homophone in homophones:
        constructed_story += construct_sentence(homophone) + ". "
    
    heteronym_count = count_words(story, heteronyms)
    synonym_count = count_words(story, synonyms)
    homophone_count = count_words(story, homophones)
    
    return {
        "heteronyms": heteronym_count,
        "synonyms": synonym_count,
        "homophones": homophone_count
    }