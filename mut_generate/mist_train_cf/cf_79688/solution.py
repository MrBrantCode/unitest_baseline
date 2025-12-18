"""
QUESTION:
Create a function `EncryptionDecryption` that contains a configurable codebook of 20 uncommon symbols with their corresponding complex actions or statuses. The function should include two methods: `encrypt(message)` to encrypt a given message using the codebook and `decrypt(message)` to decrypt a message back to its original text. The function should handle exceptions by tracking missing words not found in the codebook during encryption and replacing unknown symbols with "[UNKNOWN SYMBOL]" during decryption.
"""

def EncryptionDecryption(codebook):
    def encrypt(message):
        missing_words = []
        encrypted_message = ""
        words = message.split(' ')
        for word in words:
            found = False
            for symbol, action in codebook.items():
                if word.lower() == action:
                    encrypted_message = encrypted_message + " " +  symbol
                    found = True
                    break
            if not found:
                missing_words.append(word)
        return encrypted_message, missing_words

    def decrypt(message):
        decrypted_message = ""
        symbols = message.split(' ')
        for symbol in symbols:
            if symbol in codebook.keys():
                decrypted_message = decrypted_message + " " + codebook[symbol]
            else:
                decrypted_message = decrypted_message + " " + "[UNKNOWN SYMBOL]"
        return decrypted_message

    return encrypt, decrypt

codebook = {
    '@':'play',
    '#':'pause', 
    '$':'stop', 
    '%':'run', 
    '^':'fetch', 
    '&':'save',
    '*':'delete', 
    '(':'upload', 
    ')':'download', 
    '-':'end',
    '+':'start',
    '=':'equivalent',
    '_':'under', 
    '[':'left', 
    ']':'right',
    '{':'open', 
    '}':'close', 
    ':':'speak',
    ';':'listen',
    '<':'decrease',
    '>':'increase'
}

encrypt, decrypt = EncryptionDecryption(codebook)