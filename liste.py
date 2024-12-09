nb_vie = 7

mot_mystere = 'python'

mot_public= '_' * len(mot_mystere)

while nb_vie > 0 and mot_mystere != mot_public:
    lettre =input('entrez une lettre: ')

    if lettre in mot_mystere:
        for i in range(len(mot_mystere)):
            if mot_mystere[i] == lettre:
               mot_public =mot_public[:i] + lettre + mot_public[i + 1:]
    else:
        nb_vie -= 1

    if mot_public == mot_mystere:
        print("bravo ! let mot est", mot_mystere)
    elif nb_vie == 0:
        print ("vous avez perdu")
    else:
        print("vous avez", nb_vie)
        print("le mot est :", mot_public)






