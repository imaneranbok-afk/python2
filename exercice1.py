# age = int(input("veuillez entrer votre age :"))

# if age < 12 :
#     print("vous etes encore enfant")
# elif age >13 and age <17 :
#     print("vous etes une Adolescent")
# elif age >18 and age <64 :
#     print("vous etes Adulte")
# else :
#     print("vous etes Senoir")
#exercice 2 :
# contacts = ["bouchra" , "Imane" , "Nadia","ranbok"]
# while True :
#     print("veuillez choisis votre option :")
#     print("--Menu -- ")
#     x = int(input(" 1- ajouter un contact :" \
#     "2- afficher vos contacts :" \
#     "3- quitter le programme : "))
#     if x == 1 :
#         contact = input("veuillez entrer le contact a ajouter : ")
#         contacts.append(contact)
#         continue
#     elif x == 2 :
#         y = enumerate(contacts)
#         print(list(y))
#     else :
#         print("vous avec quittez le programme")
#         break
#exercice 3 :
# mot_pass = "python123"
# while True :
#     mot_saisie = input("veuillez entrer le mot_de_passe :")
#     if mot_saisie == mot_pass :
#         print("mot_de_pass correct . vous etes connecter !")
#     else :
#         print("mot de pass incorrect , veuillez saiasie a nouveau")
#exercice 4 :
N1 = int(input("veuillez entrer le premier nombre : "))
N2 = int(input("veuillez entrer le deusieme nombre :"))
while True :
    print(" ===Menu :  ===")
    print("1- addition: " \
    "2- soustraction : " \
    "3-multiplication : " \
    "4-division : " )
    option = input("option de 1 a 4 :")
    if option == "1" :
        result = N1+N2
        print(f"resultat :{N1}+{N2} = {result}")
    elif option == "2" :
        result = N1-N2
        print(f"résultat : {N1} - {N2} = {result}")
    elif option == "3" :
        result = N1*N2
        print(f"résultat : {N1} * {N2} = {result}")
    elif option == "4" :
        if N2 == 0 :
            print("inmpossible la division sur 0 ")
        else :
            result = int(N1/N2)
            print(f"résultat : {N1} / {N2} = {result}")
    else :
        print("veuilliez choisis une option disponilbe") 
    