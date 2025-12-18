"""
QUESTION:
Créer une fonction `encode_ascii` qui prend une liste de chaînes de caractères en entrée et renvoie une nouvelle liste de chaînes où tous les caractères non ASCII (ASCII > 127) sont remplacés par leur équivalent Unicode décimal, encodé par la forme `&#xXXXX;` où XXXX est le code point utf8 du caractère.
"""

def encode_ascii(input_list):
    output_list = []
    for s in input_list:
        output_str = ""
        for c in s:
            if ord(c) > 127:
                output_str += "&#x{0:x};".format(ord(c))
            else:
                output_str += c
        output_list.append(output_str)
    return output_list