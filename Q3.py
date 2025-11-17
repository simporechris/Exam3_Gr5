import hashlib
messages_gr5 = {
    "pseudo" : "IronCode",
    "messages" : ["Le monstre est au niveau 7", "Code 9 activé demain", "La réponse est 142"],
    "signatures" : ["fresea", "odivai", "nses14"]
}

def hasher_mots():
    """
    Fonction qui hash la liste message
    message : la liste de mot a hasher
    :return: le hashe
    """
    for messages in messages_gr5:
        signature = messages_gr5["messages"]
        signature = messages.encode()
        hash_md5 = hashlib.md5(signature).hexdigest()
        # Référence : documentation module hashlib
        # https://docs.python.org/3/library/hashlib.html#usage
        messages_gr5["messages"] = hash_md5

    return hash_md5




if __name__ == '__main__':
    hasher_mots()
    print(f"Messages avec signatures validées : \n {hasher_mots()}" )
    print("--"*20)
    print(f"Messages altérés, signatures non valides :\n {hasher_mots()} ")