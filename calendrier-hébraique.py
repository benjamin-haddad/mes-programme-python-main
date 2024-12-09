from convertdate import hebrew
import datetime

# Liste des mois hébraïques
hebrew_months = [
    "Tichri", "Hechvan", "Kislev", "Tevet", "Chvat", 
    "Adar", "Nissan", "Iyar", "Sivan", "Tamouz", "Av", "Eloul"
]

# Obtenir la date actuelle
today = datetime.date.today()

# Convertir la date actuelle en date hébraïque
hebrew_date = hebrew.from_gregorian(today.year, today.month, today.day)

# Afficher la date hébraïque
print(f"Date actuelle en calendrier grégorien : {today}")
print(f"Date actuelle en calendrier hébraïque : {hebrew_date[2]} {hebrew_months[hebrew_date[1] - 1]} {hebrew_date[0]}")

# Demander à l'utilisateur s'il veut une conversion pour une autre date
choice = input("Voulez-vous convertir une autre date ? (oui/non) : ").strip().lower()

if choice == "oui":
    # Demander à l'utilisateur d'entrer une date grégorienne
    day = int(input("Entrez le jour de la date grégorienne (1-31) : "))
    month = int(input("Entrez le mois de la date grégorienne (1-12) : "))
    year = int(input("Entrez l'année de la date grégorienne : "))
    
    # Convertir la date grégorienne en date hébraïque
    hebrew_date = hebrew.from_gregorian(year, month, day)

    # Afficher la date hébraïque pour la date entrée
    print(f"Date grégorienne : {day}/{month}/{year}")
    print(f"Correspondant à : {hebrew_date[2]} {hebrew_months[hebrew_date[1] - 1]} {hebrew_date[0]}")
else:
    print("Merci d'utiliser ce programme. À bientôt !")
