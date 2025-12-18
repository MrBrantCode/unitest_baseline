"""
QUESTION:
Create a function called `convert_english_number` that takes a string representation of a number in English as input and returns its numerical value. The input string may contain words like "one", "two", ..., "nineteen", "twenty", ..., "ninety", "hundred", and "thousand". The function should correctly parse the string and return the corresponding numerical value.
"""

def convert_english_number(number_string):
    word_values = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,"eleven":11,"twelve":12,"thirteen":13,"fourteen":14,"fifteen":15,"sixteen":16,"seventeen":17,"eighteen":18,"nineteen":19,"twenty":20,"thirty":30,"forty":40,"fifty":50,"sixty":60,"seventy":70,"eighty":80,"ninety":90}
    word_list = number_string.replace(" and ", " ").split()

    final_num = 0
    i=0
    while i<len(word_list): 
        if word_list[i] in word_values.keys():
            final_num += word_values[word_list[i]]
        elif word_list[i]=="hundred":
            final_num = final_num*100
        elif word_list[i]=="thousand":
            final_num *= 1000
        i+=1
    return final_num