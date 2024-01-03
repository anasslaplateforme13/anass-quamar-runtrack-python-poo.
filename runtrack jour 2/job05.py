class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche=False):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = 50  # Initialisation du réservoir à 50 par défaut

    # Getters
    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def get_reservoir(self):
        return self.__reservoir

    # Setters
    def set_marque(self, nouvelle_marque):
        self.__marque = nouvelle_marque

    def set_modele(self, nouveau_modele):
        self.__modele = nouveau_modele

    def set_annee(self, nouvelle_annee):
        self.__annee = nouvelle_annee

    def set_kilometrage(self, nouveau_kilometrage):
        self.__kilometrage = nouveau_kilometrage

    def set_en_marche(self, etat):
        self.__en_marche = etat

    # Méthode privée pour vérifier le niveau du réservoir
    def __verifier_plein(self):
        return self.__reservoir > 5  # La voiture peut démarrer si le réservoir est supérieur à 5 litres

    # Méthode pour démarrer la voiture en vérifiant le niveau du réservoir
    def demarrer(self):
        if self.__verifier_plein():
            self.__en_marche = True
        else:
            print("Niveau de carburant trop bas. Impossible de démarrer.")

    # Méthode pour arrêter la voiture
    def arreter(self):
        self.__en_marche = False

# Exemple d'utilisation avec une Bugatti
ma_bugatti = Voiture("Bugatti", "Veyron", 2022, 1000)

# Affichage des informations de la Bugatti
print("Marque :", ma_bugatti.get_marque())
print("Modèle :", ma_bugatti.get_modele())
print("Année :", ma_bugatti.get_annee())
print("Kilométrage :", ma_bugatti.get_kilometrage())

# Vérification de l'état initial de la voiture
print("En marche :", ma_bugatti.get_en_marche())

# Démarrage de la voiture
ma_bugatti.demarrer()
print("En marche après démarrage :", ma_bugatti.get_en_marche())

# Arrêt de la voiture
ma_bugatti.arreter()
print("En marche après arrêt :", ma_bugatti.get_en_marche())

