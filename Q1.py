"""
Début
Definir la fonction chiffrement_cesar():
    cle_gr5=[
        []
        []
    ]
    message =""
    Pour chaque lettre du message:
        pour chaque caractere dans le message:
            si le caractere est une lettre alors:
                trouver la position caractere dans la liste 1 du dictionnaire
                ajouter la liste 2
            sinon
                ajouter caractere
            break
    retourne message

#rotaion cesar de 5
message final = ""
 pour chaque caractere dans le message final:
    si le caractere est une lettre alors:
        trouver la position du  caractere dans la liste 2 du dictionnaire
        nouvelle position = position+5
        ajouter la liste 2 [nouvelle position] à message final
    sinon
        ajouter caractere
    break
retourne message final

FIN
"""