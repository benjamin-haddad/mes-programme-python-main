class Pizza :
  def __init__(self, base, prix, diametre, style, ingredients):
    self.base = base
    self.prix = prix
    self.diametre = diametre
    self.style = style
    self.ingredients = ingredients

  def ajouter_ingredients(self, nouvel_ingredients):
    if nouvel_ingredients == "ananas":
     raise TypeError("les ananas ne vont pas sur les pizzas")
    self.ingredients.append(nouvel_ingredients)
    self.prix =self.prix + 1

  def servir(self, table):
    print("J'ammene la pizza à la table :", table)

  def servir(self, adresse):
    print("Je livre la pizza à l'adresse :", adresse)


base = input("quelle base voulez-vous ? (tomate/blanche) ")
taille =input("quelle taille voulez-vous ? (moyenne/grande) ")
style = input("quelle style voulez-vous ? (classique calzone stromb) ")
ingredients = input("quels ingrédients voulez-vous ? ")

diametre = 30
if taille == 'grande':
   diametre = 34

ingredients = ingredients.split(', ')

prix = 5 + len(ingredients)

pizza = Pizza(
base =base,
diametre =diametre,
style =style,
ingredients =ingredients,
prix =prix
)

print (pizza.ingredients, pizza.prix)
pizza.ajouter_ingredients("olives")
print (pizza.ingredients, pizza.prix)
pizza.livre("9 rue du bois")
pizza.servir(13)
ananas = input("voulez-vous ajouter des ananas ? (oui, non) ")

if ananas == "oui":
  pizza.ajouter_ingredients("ananas")



    