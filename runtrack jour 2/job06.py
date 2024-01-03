class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}
        self.__statut_commande = "en cours"  # Par défaut, la commande est en cours

    def ajouter_plat(self, nom_plat, prix_plat):
        self.__plats_commandes[nom_plat] = {"prix": prix_plat, "statut": "en cours"}

    def annuler_commande(self):
        self.__plats_commandes.clear()  # Vider la liste des plats pour annuler la commande
        self.__statut_commande = "annulée"

    def __calculer_total(self):
        total = sum(plat["prix"] for plat in self.__plats_commandes.values())
        return total

    def afficher_commande(self):
        total = self.__calculer_total()
        print(f"Commande #{self.__numero_commande}:")
        for nom_plat, details in self.__plats_commandes.items():
            print(f"- {nom_plat}: {details['prix']} € ({details['statut']})")
        print(f"Total à payer: {total} €")

    def calculer_tva(self):
        total = self.__calculer_total()
        tva = total * 0.20  # Calcul de la TVA (20%)
        return tva

# Exemple d'utilisation
ma_commande = Commande(101)
ma_commande.ajouter_plat("Pizza", 12)
ma_commande.ajouter_plat("Salade", 8)
ma_commande.ajouter_plat("Dessert", 5)

ma_commande.afficher_commande()

ma_commande.calculer_tva()

ma_commande.annuler_commande()
ma_commande.afficher_commande()
