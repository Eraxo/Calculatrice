# Variables
a = b = ""

# Boucle, tant qu'a et b ne sont pas des nombres
while not (a.isdigit() and b.isdigit()):

    # Récupération des saisies de l'utilisateur
    a = input("Entrez le premier nombre : ")
    b = input("Entrez le deuxième nombre : ")

    # Affichage d'erreur saisie autre que des nombres
    if not (a.isdigit() and b.isdigit()):
        print("Veuillez saisir des nombres valides")

# Affichage résultat de l'addition
print(f"Le résultat de l'addition de {a} avec {b} est égal à {int(a) + int(b)}")

