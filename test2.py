age = int(input("veuillez entrer votre age : "))
a_carte = int(input("avoir la carte : 1 - oui , 2- non "))

if age == 25 and a_carte == 1 :
    print("acces autorisé")
elif age == 19 and a_carte == 1 :
    print("acces refusé")
elif age == 25 and a_carte == 2 :
    print("acces refusé")
else :
    print("acces refusé")