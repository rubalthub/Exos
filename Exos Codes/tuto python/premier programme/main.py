from re import S


def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input(f"Quel est ton nom {user} ? ")

    return reponse_nom


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input("Quel est ton age " + nom_personne + " ? ")
        try:
            age_int = int(age_str)
        except:
            print("Veuillez rentrer un nombre pour l'age svp")
    return age_int


def afficher_informations_personne(nom, age):
    print()
    print("Tu t'appelle " + nom +
          ", tu as " + str(age) + " ans !")
    # print(f"Tu t'appelle {nom}, tu as {age} ans !")
    # print("Tu t'appelle %s, tu as %s ans !" % (nom, age))
    if age == 17:
        print("Tu es presque majeur !")
    elif 12 <= age < 18:
        print("Tu es un adolescent !")
    elif age == 1 or age == 2:
        print("Tu es un bébé !")
    elif age == 18:
        print("Tu es juste majeur: Bravo !")
    elif age <= 10:
        print("Tu es un enfant.")
    elif age >= 60:
        print("Tu es un sénior.")
    elif age > 18:
        print("Tu es majeur !")
    else:
        print("Tu es mineur !")

    print("L'an prochain tu auras " + str(age + 1) + " ans !")
    print()


# nom1 = demander_nom()
# nom2 = demander_nom()

# age1 = demander_age(nom1)
# age2 = demander_age(nom2)

# print()

# afficher_informations_personne(nom1, age1)
# afficher_informations_personne(nom2, age2)


# commentaire

# """ commentaire aussi
# mais possible sur plusieurs lignes """


# n = 0
# while n < 10:
#     print("Valeur de n = " + str(n))

nb_user_int = ""
while nb_user_int == "":
    nb_user_str = input("Combien de personne(s) êtes vous ? ")
    try:
        nb_user_int = int(nb_user_str)
    except:
        print()
        print("Veuillez saisir un nombre svp")
        print()

if nb_user_int == 0:
    print()
    print("""Vous ne pouvez pas être zéro !!!
Merci de sair une valeur au moins égale à 1 svp !""")
    print()

else:
    for i in range(0, nb_user_int):
        user = "personne " + str(i+1)
        nom = demander_nom()
        age = demander_age(nom)
        afficher_informations_personne(nom, age)
