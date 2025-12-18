"""
QUESTION:
Design a database schema to store a comprehensive lexicon with linked synonyms and antonyms for each linguistic term. The schema should include tables for storing unique linguistic terms, their synonyms, and antonyms. Consider a design that can be improved to accommodate additional attributes such as part of speech and multiple meanings of a word.
"""

class Lexicon:
    def __init__(self, word):
        self.word = word
        self.synonyms = []
        self.antonyms = []

    def add_synonym(self, synonym):
        self.synonyms.append(synonym)

    def add_antonym(self, antonym):
        self.antonyms.append(antonym)

    def get_synonyms(self):
        return self.synonyms

    def get_antonyms(self):
        return self.antonyms

    def add_relationship(self, word, relationship_type):
        if relationship_type == 'synonym':
            self.add_synonym(word)
        elif relationship_type == 'antonym':
            self.add_antonym(word)

    def get_relationships(self, relationship_type):
        if relationship_type == 'synonym':
            return self.get_synonyms()
        elif relationship_type == 'antonym':
            return self.get_antonyms()

def lexicon_entry(word, synonyms=None, antonyms=None):
    lexicon = Lexicon(word)
    if synonyms:
        for synonym in synonyms:
            lexicon.add_synonym(synonym)
    if antonyms:
        for antonym in antonyms:
            lexicon.add_antonym(antonym)
    return lexicon