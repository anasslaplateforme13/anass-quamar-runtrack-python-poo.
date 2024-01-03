class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages

    # Getters
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nb_pages(self):
        return self.__nb_pages

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

# Création d'un livre avec titre, auteur et nombre de pages
mon_livre = Livre("Harry Potter", "J.K. Rowling", 300)

# Affichage des valeurs initiales
print("Titre :", mon_livre.get_titre())
print("Auteur :", mon_livre.get_auteur())
print("Nombre de pages :", mon_livre.get_nb_pages())

# Modification des valeurs
mon_livre.set_titre("Le Seigneur des Anneaux")
mon_livre.set_auteur("J.R.R. Tolkien")
mon_livre.set_nb_pages(500)  # Modification valide
mon_livre.set_nb_pages(-100)  # Tentative de modification invalide

# Vérification des modifications
print("Nouveau titre :", mon_livre.get_titre())
print("Nouvel auteur :", mon_livre.get_auteur())
print("Nouveau nombre de pages :", mon_livre.get_nb_pages())
