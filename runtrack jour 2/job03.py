class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True  # Initialisé par défaut à True

    # Getters
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nb_pages(self):
        return self.__nb_pages

    def get_disponible(self):
        return self.__disponible

    # Setters
    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def set_auteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur

    def set_nb_pages(self, nouveau_nb_pages):
        if isinstance(nouveau_nb_pages, int) and nouveau_nb_pages > 0:
            self.__nb_pages = nouveau_nb_pages
        else:
            print("Le nombre de pages doit être un nombre entier positif.")

    def set_disponible(self, disponibilite):
        self.__disponible = disponibilite

    # Méthode de vérification de disponibilité
    def verification(self):
        return self.__disponible

    # Méthode pour emprunter un livre
    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Livre emprunté avec succès.")
        else:
            print("Ce livre n'est pas disponible pour l'emprunt.")

    # Méthode pour rendre un livre
    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("Livre rendu avec succès.")
        else:
            print("Ce livre est déjà disponible.")

# Exemple d'utilisation
mon_livre = Livre("Harry Potter", "J.K. Rowling", 300)

# Vérification de disponibilité avant emprunt
print("Disponible avant emprunt :", mon_livre.verification())

# Emprunter le livre
mon_livre.emprunter()

# Vérification de disponibilité après emprunt
print("Disponible après emprunt :", mon_livre.verification())

# Rendre le livre
mon_livre.rendre()

# Vérification de disponibilité après rendu
print("Disponible après rendu :", mon_livre.verification())

