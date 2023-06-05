def chiffrer_message(message, key):
    """
    Chiffre un message en utilisant le chiffre de César.

    Args:
        message (str): Le message à chiffrer.
        key (int): Le décalage à appliquer.

    Returns:
        str: Le message chiffré.
    """
    message_chiffre = ""
    for caractere in message:
        if caractere.isalpha():
            if caractere.isupper():
                code_ascii = ord(caractere)
                code_ascii = (code_ascii - 65 + key) % 26 + 65
                message_chiffre += chr(code_ascii)
            else:
                code_ascii = ord(caractere)
                code_ascii = (code_ascii - 97 + key) % 26 + 97
                message_chiffre += chr(code_ascii)
        else:
            message_chiffre += caractere

    return message_chiffre


def dechiffrer_message(message_chiffre, decalage):
    """
    Déchiffre le message chiffré 
    Args:
        message_chiffre (str): Le message chiffré.
        key (int): idem que pour le chiffrement.

    Returns:
        str: Le message déchiffré.
    """
    message_dechiffre = ""
    for caractere in message_chiffre:
        if caractere.isalpha():
            if caractere.isupper():
                code_ascii = ord(caractere)
                code_ascii = (code_ascii - 65 - decalage) % 26 + 65
                message_dechiffre += chr(code_ascii)
            else:
                code_ascii = ord(caractere)
                code_ascii = (code_ascii - 97 - decalage) % 26 + 97
                message_dechiffre += chr(code_ascii)
        else:
            message_dechiffre += caractere

    return message_dechiffre


# Exemple d'utilisation
message_original = input('Entrez le message à chiffrer : ')
key = 2

message_chiffre = chiffrer_message(message_original, key)
print("Message chiffré:", message_chiffre)

message_dechiffre = dechiffrer_message(message_chiffre, key)
print("Message déchiffré:", message_dechiffre)