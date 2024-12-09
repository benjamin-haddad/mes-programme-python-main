



# LES CHOSES A CONNAITRE EN PYTHON !!!


#les conditions 
1. Structures de contrôle de flux (conditions)
if : pour exécuter un bloc de code si une condition est vraie.
elif (else if) : pour vérifier une condition supplémentaire si la condition précédente est fausse.
else : pour exécuter un bloc de code si aucune des conditions if ou elif n'est vraie.
assert : une instruction de débogage qui vérifie si une condition est vraie, sinon elle lance une exception AssertionError.
match (depuis Python 3.10) : pour effectuer un "pattern matching" (correspondance de motifs), semblable à un switch/case dans d'autres langages.
 
( exemple :)
x = 10
if x > 5:
    print("x est plus grand que 5")
elif x == 5:
    print("x est égal à 5")
else:
    print("x est inférieur à 5")

# les boucles
2. Boucles
for : utilisé pour itérer sur des séquences (listes, tuples, dictionnaires, ensembles, etc.) ou des objets itérables.
while : utilisé pour exécuter un bloc de code tant qu'une condition est vraie.
break : pour interrompre une boucle prématurément.
continue : pour passer à l'itération suivante de la boucle sans exécuter le reste du code dans la boucle.
else (avec for ou while) : un bloc qui s'exécute après la boucle, sauf si la boucle a été interrompue par un break.

# Boucle for
for i in range(5):
    print(i)

# Boucle while
x = 0
while x < 5:
    print(x)
    x += 1

# Utilisation de break et continue
for i in range(5):
    if i == 2:
        continue  # Passe à l'itération suivante
    if i == 4:
        break  # Interrompt la boucle
    print(i)

#fonction 

3. Fonctions en Python
Déclaration de fonction : à l'aide du mot-clé def.
Arguments de fonction : peuvent être positionnels, nommés, avec des valeurs par défaut, ou des arguments variables.
Retour de valeur : avec le mot-clé return.
Fonctions lambda : des fonctions anonymes ou des fonctions lambda.
Fonctions intégrées : Python offre de nombreuses fonctions intégrées comme len(), range(), type(), str(), int(), etc.
Fonctions de haut niveau : comme map(), filter(), reduce() (dans le module functools), zip().

# Déclaration de fonction
def saluer(nom):
    return f"Bonjour, {nom}!"

print(saluer("Alice"))

# Fonction lambda
carre = lambda x: x ** 2
print(carre(5))

#structures 

4. Structures de contrôle avancées
try...except : pour gérer les exceptions.
try...except...else : le bloc else s'exécute si aucune exception n'est levée.
finally : un bloc qui s'exécute toujours, que l'exception soit levée ou non.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division par zéro!")
else:
    print("Aucune exception n'a été levée.")
finally:
    print("Ce bloc s'exécute toujours.")

 #instructions

    5. Instructions supplémentaires
pass : une instruction qui ne fait rien, souvent utilisée comme un espace réservé.
yield : utilisé dans les fonctions génératrices pour produire un élément à la fois.
return : pour renvoyer une valeur d'une fonction.
break et continue : comme mentionné dans les boucles, ces instructions contrôlent le flux de la boucle.

def compteur():
    for i in range(5):
        yield i  # Produit l'élément i, mais conserve l'état de la fonction

for valeur in compteur():
    print(valeur)

#fonctions avancées 

6. Fonctions intégrées utiles
Python propose un grand nombre de fonctions intégrées qui facilitent la manipulation des données et la gestion de différentes tâches courantes :

print() : pour afficher du texte à l'écran.
len() : retourne la longueur d'une séquence (chaîne, liste, etc.).
type() : retourne le type de l'objet passé en argument.
int(), float(), str() : pour convertir des types de données.
input() : pour obtenir des entrées de l'utilisateur.
range() : génère une séquence d'entiers.
sorted() : retourne une liste triée.
sum() : calcule la somme des éléments d'une séquence.
min(), max() : retourne respectivement le minimum et le maximum d'une séquence.
map(), filter(), reduce() (dans le module functools) : pour appliquer des fonctions sur des séquences.

# Utilisation de quelques fonctions intégrées
numbers = [1, 2, 3, 4, 5]
print("La somme est:", sum(numbers))  # Affiche "La somme est: 15"

# Utilisation de `map()` pour doubler chaque élément
doubled = map(lambda x: x * 2, numbers)
print(list(doubled))  # Affiche [2, 4, 6, 8, 10]

# dictionnaires 
7. Compréhensions de listes, ensembles et dictionnaires
Les compréhensions sont un moyen compact et lisible de créer des listes, des ensembles et des dictionnaires.

# Créer une liste des carrés des nombres de 0 à 4
squares = [x**2 for x in range(5)]
print(squares)  # Affiche [0, 1, 4, 9, 16]

*# Créer un dictionnaire avec des clés de 0 à 4 et des valeurs les carrés
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)  # Affiche {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Créer un ensemble des carrés uniques
unique_squares = {x**2 for x in range(-2, 3)}
print(unique_squares)  # Affiche {0, 1, 4}

# fonctions avancées 

8. Fonctions avancées
Fonctions récursives : appel à soi-même pour résoudre des problèmes de manière répétée.

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Affiche 120

Fonctions génératrices : créent des objets générateurs qui produisent des valeurs à la demande.

def generate_numbers():
    yield 1
    yield 2
    yield 3

for number in generate_numbers():
    print(number)  # Affiche 1, 2, 3


 # fonctions anonymes 
    9. Fonctions anonymes (lambda)
Les fonctions lambda sont des fonctions sans nom utilisées principalement pour des opérations simples.

Syntaxe : lambda arguments: expression
Exemple :

# Fonction lambda pour additionner deux nombres
add = lambda a, b: a + b
print(add(5, 3))  # Affiche 8

# Utilisation de lambda avec `sorted()` pour trier par la deuxième lettre
words = ["apple", "banana", "cherry"]
sorted_words = sorted(words, key=lambda word: word[1])
print(sorted_words)  # Affiche ['banana', 'cherry', 'apple']

# Fonction lambda pour additionner deux nombres
add = lambda a, b: a + b
print(add(5, 3))  # Affiche 8

# Utilisation de lambda avec `sorted()` pour trier par la deuxième lettre
words = ["apple", "banana", "cherry"]
sorted_words = sorted(words, key=lambda word: word[1])
print(sorted_words)  # Affiche ['banana', 'cherry', 'apple']



10. Fonctions de plus haut niveau
map(function, iterable) : applique function à chaque élément de iterable et retourne un itérateur.
filter(function, iterable) : filtre les éléments de iterable pour lesquels function retourne True.
reduce(function, iterable, initial) (dans le module functools) : applique function cumulativement à chaque élément de iterable, de gauche à droite, pour réduire la séquence à une seule valeur.
Exemple de reduce() :


from functools import reduce

# Multiplie tous les éléments de la liste
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Affiche 24


11. Gestion des exceptions
Les exceptions permettent de gérer les erreurs de manière élégante et de garder le programme en marche.

try...except...else...finally

try:
    value = int("abc")  # Provoque une exception
except ValueError:
    print("Erreur de conversion")
else:
    print("Conversion réussie")
finally:
    print("Bloc finally exécuté")


12. Instructions with pour la gestion des contextes
L'instruction with est utilisée pour gérer les ressources de manière sécurisée (par exemple, la gestion de fichiers).

Exemple :

with open("fichier.txt", "r") as file:
    content = file.read()
    print(content)
# Le fichier est automatiquement fermé à la fin du bloc `with`

13. Modules et bibliothèques
Python est livré avec une bibliothèque standard riche (comme os, sys, math, random, datetime, etc.).
Les modules tiers, tels que numpy, pandas, requests ou matplotlib, ajoutent de nombreuses fonctionnalités pour les applications de calcul scientifique, la manipulation de données, le réseau, etc.
Exemple d'utilisation de module :

import math

print(math.sqrt(16))  # Affiche 4.0
print(math.pi)  # Affiche la valeur de pi




