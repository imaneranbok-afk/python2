#exercice 1
age = int(input("veuillez saisie votre age : "))
print(age)
if age <= 12 :
    print("vous etes encore enfant")
elif age >=13 and age<=17 :
    print("vous etes Adolescent")
elif age >=18 and age <=64 :
    print("vous etes Adulte")
else :
    print("vous etes Senior")

#exercice 2
# Programme de gestion de carnet d'adresses
contacts = []  # Liste initialisée en dehors de la boucle

while True:
    print("\n=== MENU CARNET D'ADRESSES ===")
    print("1. Ajouter un contact")
    print("2. Afficher tous les contacts")
    print("3. Quitter le programme")
    choix = input("Votre choix (1-3) : ")
    
    if choix == "1":
        nom = input("Entrez le nom du contact : ")
        contacts.append(nom)
        print(f"Contact '{nom}' ajouté avec succès!")
        
    elif choix == "2":
        if not contacts:  # Vérifie si la liste est vide
            print("Aucun contact dans le carnet.")
        else:
            print("\nListe des contacts :")
            for index, contact in enumerate(contacts):
                print(f"{index}. {contact}")
                
    elif choix == "3":
        print("Au revoir!")
        break
        
    else:
        print("Choix invalide. Veuillez entrer 1, 2 ou 3.") 

#exercice 3
mot_de_passe_correct = "python123"

while True:
    mot_de_passe = input("Veuillez saisir votre mot de passe : ")
    
    if mot_de_passe == mot_de_passe_correct:
        print("Mot de passe correct. Accès autorisé!")
        break
    else:
        print("Mot de passe incorrect. Veuillez réessayer.")

#exercice 4
print("=== CALCULATRICE SIMPLE ===")

try:
    nombre1 = float(input("Entrez le premier nombre : "))
    nombre2 = float(input("Entrez le deuxième nombre : "))
    
    # Affichage du menu des opérations
    print("\nChoisissez une opération :")
    print("1. Addition (+)")
    print("2. Soustraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    choix = input("Votre choix (1-4) : ")
    
    if choix == "1":
        resultat = nombre1 + nombre2
        print(f"Résultat : {nombre1} + {nombre2} = {resultat}")
        
    elif choix == "2":
        resultat = nombre1 - nombre2
        print(f"Résultat : {nombre1} - {nombre2} = {resultat}")
        
    elif choix == "3":
        resultat = nombre1 * nombre2
        print(f"Résultat : {nombre1} * {nombre2} = {resultat}")
        
    elif choix == "4":
        if nombre2 == 0:
            print("Erreur : Division par zéro impossible!")
        else:
            resultat = nombre1 / nombre2
            print(f"Résultat : {nombre1} / {nombre2} = {resultat}")
            
    else:
        print("Choix invalide. Veuillez entrer un nombre entre 1 et 4.")
        
except ValueError:
    print("Erreur : Veuillez entrer des nombres valides.")