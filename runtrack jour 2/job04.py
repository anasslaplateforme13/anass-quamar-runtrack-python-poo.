class Student:
    def __init__(self, nom, prenom, numero_etudiant, credits=0):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = credits

    @property
    def nom(self):
        return self.__nom

    @property
    def prenom(self):
        return self.__prenom

    @property
    def numero_etudiant(self):
        return self.__numero_etudiant

    @property
    def credits(self):
        return self.__credits

    @credits.setter
    def credits(self, nombre_credits):
        if nombre_credits > 0:
            self.__credits += nombre_credits
        else:
            print("Le nombre de crédits ajouté doit être supérieur à zéro.")

# Instanciation de l'objet représentant John Doe
john_doe = Student("Doe", "John", 145)

# Ajout de crédits à John Doe trois fois
john_doe.credits += 5
john_doe.credits += 10
john_doe.credits += 7

# Impression du total de crédits de John Doe
print(f"Total de crédits de {john_doe.nom} {john_doe.prenom} : {john_doe.credits}")
class Student:
    def __init__(self, nom, prenom, numero_etudiant, credits=0):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = credits
        self.__level = self.__studentEval()  # Évaluation initiale du niveau

    @property
    def nom(self):
        return self.__nom

    @property
    def prenom(self):
        return self.__prenom

    @property
    def numero_etudiant(self):
        return self.__numero_etudiant

    @property
    def credits(self):
        return self.__credits

    @credits.setter
    def credits(self, nombre_credits):
        if nombre_credits > 0:
            self.__credits += nombre_credits
            self.__level = self.__studentEval()  # Mettre à jour le niveau après ajout de crédits
        else:
            print("Le nombre de crédits ajouté doit être supérieur à zéro.")

    # Méthode privée pour évaluer le niveau de l'étudiant
    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    # Méthode pour afficher les informations de l'étudiant
    def studentInfo(self):
        print(f"Informations de l'étudiant :")
        print(f"Nom : {self.__nom}")
        print(f"Prénom : {self.__prenom}")
        print(f"Identifiant : {self.__numero_etudiant}")
        print(f"Niveau : {self.__level}")

# Instanciation de l'objet représentant John Doe
john_doe = Student("Doe", "John", 145)

# Ajout de crédits à John Doe trois fois
john_doe.credits += 5
john_doe.credits += 10
john_doe.credits += 7

# Affichage des informations de John Doe
john_doe.studentInfo()
