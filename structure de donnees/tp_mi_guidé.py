from abc import ABC, abstractmethod
from dataclasses import dataclass

# -------------------------
# Partie 1 : Classe abstraite Boisson
# -------------------------

class Boisson(ABC):

    @abstractmethod
    def cout(self):
        pass

    @abstractmethod
    def description(self):
        pass

    # combinaison de boissons
    def __add__(self, other):
        return BoissonCombinee(self, other)


# -------------------------
# Partie 2 : Boissons concretes
# -------------------------

class Cafe(Boisson):

    def cout(self):
        return 2.0

    def description(self):
        return "Cafe simple"


class The(Boisson):

    def cout(self):
        return 1.8

    def description(self):
        return "The"


# -------------------------
# Partie 3 : 
# -------------------------

class Ingredient(Boisson):

    def __init__(self, boisson):
        self.boisson = boisson


class Lait(Ingredient):

    def cout(self):
        return self.boisson.cout() + 0.5

    def description(self):
        return self.boisson.description() + ", Lait"


class Sucre(Ingredient):

    def cout(self):
        return self.boisson.cout() + 0.2

    def description(self):
        return self.boisson.description() + ", Sucre"


# Travail demande : nouvel ingrédient
class Caramel(Ingredient):

    def cout(self):
        return self.boisson.cout() + 0.7

    def description(self):
        return self.boisson.description() + ", Caramel"


# -------------------------
# Partie 4 : Combinaison de boissons
# -------------------------

class BoissonCombinee(Boisson):

    def __init__(self, b1, b2):
        self.b1 = b1
        self.b2 = b2

    def cout(self):
        return self.b1.cout() + self.b2.cout()

    def description(self):
        return self.b1.description() + " + " + self.b2.description()


# -------------------------
# Partie 5 : Client (dataclass)
# -------------------------

@dataclass
class Client:
    nom: str
    numero: int
    points: int = 0


# -------------------------
# Partie 7 : Commandes
# -------------------------

class Commande:

    def __init__(self, client):
        self.client = client
        self.boissons = []

    def ajouter_boisson(self, boisson):
        self.boissons.append(boisson)

    def prix_total(self):
        total = 0
        for b in self.boissons:
            total += b.cout()
        return total

    def afficher(self):
        print("Client :", self.client.nom)
        print("Boissons :")

        for b in self.boissons:
            print("-", b.description())

        print("Prix total :", self.prix_total(), "MAD")


# -------------------------
# Types de commandes
# -------------------------

class CommandeSurPlace(Commande):

    def afficher(self):
        print("Commande sur place")
        super().afficher()


class CommandeEmporter(Commande):

    def afficher(self):
        print("Commande à emporter")
        super().afficher()


# -------------------------
# Programme fidélité
# -------------------------

class Fidelite:

    def ajouter_points(self, client, montant):
        points = int(montant) 
        client.points += points



class CommandeFidele(Commande, Fidelite):

    def valider(self):
        total = self.prix_total()
        self.ajouter_points(self.client, total)
        print("Commande valide")


# -------------------------
# Test Systeme :
# -------------------------

if __name__ == "__main__":

    # creation client
    client1 = Client("Imane", 1)
    client2 = Client("khadija",11)

    # creation boissons
    cafe = Cafe()
    cafe = Lait(cafe)
    cafe = Sucre(cafe)

    the = The()
    the = Caramel(the)

    # combinaison
    menu = cafe + the

    # commande
    commande = CommandeFidele(client1)

    commande.ajouter_boisson(cafe)
    commande.ajouter_boisson(the)
    commande.ajouter_boisson(menu)

    commande.afficher()

    commande.valider()

    print("Points fidelite du client :", client1.points)