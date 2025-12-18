"""
QUESTION:
Create a function `diacritic_categories` that takes a string of text as input and returns a dictionary where the keys are the morphemes in the text and the values are the frequency of characters with and without diacritic marks in each morpheme. The function should consider a morpheme to be a word separated by whitespace. The input text can contain any Unicode characters, including those with diacritic marks.
"""

from collections import Counter

def diacritic_categories(text):
    diacritics = u'ÀÁÂÃÄÅàáâãäåǼǽÈÉÊËèéêëÌÍÎÏìíîïÙÚÛÜùúûüÝŸýÿǮǯÒÓÔÕÖØòóôõöøǾǿĆćĈĉĊċČčĎďĐđĜĝĞğĠġĢģĤĥĦħÍíÎîÏïĴĵĶķĹĺĻļĽľĿŀÑñŅņŇňŉÓóÔôÕõÖöØøŔŕŖŗŘřŚśŜŝŞşŠšŤťŢţŦŧÚúÛûÜüÝýŸÿŹźŻżŽž'
    morphemes = text.split() 
    result = {morpheme: Counter(char in diacritics for char in morpheme) for morpheme in morphemes}
    return result