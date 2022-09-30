import random

chiffre_aleatoire = random.randint(1, 100)
print("deviner un nombre entre 1 et 100")

while True:
    user_number = int(input("entrer le nombre deviner :"))
    if user_number == chiffre_aleatoire:
        print("bravo vous avez reussi a trouver le bon numero")
        break
    elif user_number < chiffre_aleatoire:
        print("votre nombre est plus petit le que le nombre choisi")
    else:
        print("votre nombre est plus grand que le nombre choisi")


