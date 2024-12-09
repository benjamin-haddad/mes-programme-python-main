import pygame
import random

# Initialisation de pygame
pygame.init()

# Configuration de la fenêtre du jeu
largeur, hauteur = 800, 600
screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Attrape l'objet")

# Couleurs
blanc = (255, 255, 255)
rouge = (255, 0, 0)
bleu = (0, 0, 255)

# Paramètres de l'objet à attraper
largeur_objet, hauteur_objet = 50, 50
x_objet = random.randint(0, largeur - largeur_objet)
y_objet = 0
vitesse_objet = 5

# Paramètres du joueur
largeur_joueur, hauteur_joueur = 100, 20
x_joueur = (largeur - largeur_joueur) // 2
y_joueur = hauteur - hauteur_joueur
vitesse_joueur = 10

# Horloge pour contrôler la fréquence de la boucle
clock = pygame.time.Clock()

# Score du joueur
score = 0

# Boucle principale du jeu
en_cours = True
while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

    # Gestion des touches pour le mouvement du joueur
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT] and x_joueur > 0:
        x_joueur -= vitesse_joueur
    if touches[pygame.K_RIGHT] and x_joueur < largeur - largeur_joueur:
        x_joueur += vitesse_joueur

    # Mise à jour de la position de l'objet
    y_objet += vitesse_objet
    if y_objet > hauteur:
        y_objet = 0
        x_objet = random.randint(0, largeur - largeur_objet)
        score += 1  # Augmente le score lorsqu'un objet est raté

    # Vérification de la collision
    if (x_joueur < x_objet + largeur_objet and
        x_joueur + largeur_joueur > x_objet and
        y_joueur < y_objet + hauteur_objet and
        y_joueur + hauteur_joueur > y_objet):
        print("Vous avez attrapé l'objet !")
        score += 1
        y_objet = 0
        x_objet = random.randint(0, largeur - largeur_objet)

    # Remplissage de l'écran et dessin des objets
    screen.fill(blanc)
    pygame.draw.rect(screen, rouge, (x_objet, y_objet, largeur_objet, hauteur_objet))
    pygame.draw.rect(screen, bleu, (x_joueur, y_joueur, largeur_joueur, hauteur_joueur))

    # Affichage du score
    font = pygame.font.SysFont(None, 35)
    texte = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(texte, (10, 10))

    # Mise à jour de l'affichage
    pygame.display.flip()

    # Limitation de la fréquence de la boucle
    clock.tick(30)

pygame.quit()
