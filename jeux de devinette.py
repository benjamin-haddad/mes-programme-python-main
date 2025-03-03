import random

# Fonction pour démarrer le jeu de devinette
def jeu_devinette():
    print("Bienvenue dans le jeu de devinette !")
    
    # Choisir un niveau de difficulté
    print("Choisissez un niveau de difficulté :")
    print("1. Facile (entre 1 et 50)")
    print("2. Moyen (entre 1 et 100)")
    print("3. Difficile (entre 1 et 500)")

    try:
        niveau = int(input("Entrez votre choix (1, 2, ou 3) : "))
        if niveau == 1:
            plage_max = 50
            tentatives_max = 10
        elif niveau == 2:
            plage_max = 100
            tentatives_max = 8
        elif niveau == 3:
            plage_max = 500
            tentatives_max = 6
        else:
            print("Choix invalide. Le niveau facile sera sélectionné par défaut.")
            plage_max = 50
            tentatives_max = 10
    except ValueError:
        print("Choix invalide. Le niveau facile sera sélectionné par défaut.")
        plage_max = 50
        tentatives_max = 10

    # Nombre à deviner
    nombre_secret = random.randint(1, plage_max)

    print(f"\nLe jeu a commencé ! Vous devez deviner un nombre entre 1 et {plage_max}.")
    print(f"Vous avez {tentatives_max} tentatives pour trouver le bon nombre.\n")

    # Compteur de tentatives
    tentatives = 0

    while tentatives < tentatives_max:
        try:
            # Demander à l'utilisateur de deviner
            devinette = int(input(f"Tentative {tentatives + 1}/{tentatives_max}: Votre devinette : "))
            
            # Vérification de la devinette
            if devinette < nombre_secret:
                print("Trop bas ! Essayez un nombre plus grand.")
            elif devinette > nombre_secret:
                print("Trop élevé ! Essayez un nombre plus petit.")
            else:
                print(f"Bravo ! Vous avez trouvé le nombre {nombre_secret} en {tentatives + 1} tentatives.")
                break  # Fin du jeu si l'utilisateur a deviné le nombre correctement

            tentatives += 1
            print(f"Il vous reste {tentatives_max - tentatives} tentatives.\n")

        except ValueError:
            print("Veuillez entrer un nombre valide.\n")

    if tentatives == tentatives_max:
        print(f"\nDommage, vous n'avez pas trouvé le nombre. Le nombre était {nombre_secret}.")
    
    # Rejouer ou quitter
    rejouer = input("\nVoulez-vous rejouer ? (oui/non) : ").strip().lower()
    if rejouer == "oui":
        jeu_devinette()  # Relancer le jeu
    else:
        print("Merci d'avoir joué ! À bientôt.")

# Lancer le jeu
jeu_devinette()
