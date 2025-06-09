'''
# # # # # # # # # # # # # # # # # # # # # # #
#                                           #
#     FICHIER DES CLASSES - SAE2.02 KNN     #
#                                           #
# # # # # # # # # # # # # # # # # # # # # # #
'''

# dictionnaire des couleurs
# afficher les groupes en couleurs sur le terminal
collection_couleurs = {
    "neutre" : '\033[0m',
    "rouge"  : '\033[91m',
    "orange" : '\033[33m',
    "jaune"  : '\033[93m',
    "vert"   : '\033[92m',
    "foret"  : '\033[32m',
    "jade"   : '\033[36m',
    "cyan"   : '\033[96m',
    "bleu"   : '\033[94m',
    "mauve"  : '\033[95m',
    "violet" : '\033[35m'
}

class Point:
    '''
    @class Point
        un objet qui est composé de coordonnées sur un plan
    @var
        une coordonnée d'abscisse {x}
        une coordonnée d'ordonnée {y}
    '''
    # constructeur de la classe
    def __init__(self, x:float, y:float):
        # coordonnée de l'abscisse
        self._x = x
        # coordonnée de l'ordonnée
        self._y = y
    # affichage d'un objet de la classe
    def __str__(self):
        # retourne les coordonnées sous forme de chaine de caractères
        return f"({self._x},{self._y})"

class Objet:
    '''
    @class Objet
        un objet qui est composé d'un nom,
        d'un point sur un plan et un groupe associé à une couleur
    @var
        un nom {nom_objet}
        des coordonnées {x} et {y} pour un point {point_objet}
        un groupe {groupe_objet}
        une couleur associé au groupe {couleur_objet}
    '''
    # constructeur de la classe
    def __init__(self, n:str, x:float, y:float, g="neutre"):
        # nom de l'objet
        self._nom_objet = n
        # point sur un plan de l'objet
        self._point_objet = Point(x,y)
        # "étiquette" de l'objet
        self._groupe_objet = g
        # couleur de l'objet si la couleur se trouve dans le dictionnaire
        if g in collection_couleurs:
            self._couleur_objet = collection_couleurs[g]
        else:
            self._couleur_objet = collection_couleurs["neutre"]
            
    # affichage d'un objet de la classe
    def __str__(self):
        # retourne le nom, la couleur et le point de l'objet sous la forme d'une chaine de caractères
        return f"{self._nom_objet} '"+self._couleur_objet+f"{self._groupe_objet}"+collection_couleurs['neutre']+f"' {self._point_objet}"
    
    # méthode d'affichage
    def afficher(self):
        print("===== Point '"+self._nom_objet+"' =====")
        print("coordonnées : ",self._point_objet())
        print("groupe : "+self._couleur_objet+f"{self._groupe_objet}"+collection_couleurs['neutre'])
    
    # getters pour obtenir le nom de l'objet
    def get_nom(self):
        return self._nom_objet
    
    # getters pour obtenir le point de l'objet
    def get_point(self):
        return self._point_objet
    
    # getters pour obtenir le groupe de l'objet
    def get_groupe(self):
        return self._groupe_objet
    
    # setters pour modifier le nom de l'objet
    def set_nom(self, n:str):
        self._nom_objet = n
    
    # setters pour modifier le point de l'objet
    def set_point(self, x, y):
        self._point_objet = Point(x,y)
    
    # setters pour modifier le groupe de l'objet
    def set_groupe(self, g:str):
        self._groupe_objet = g
        if g in collection_couleurs:
            self._couleur_objet = collection_couleurs[g]
        else:
            self._couleur_objet = collection_couleurs["neutre"]

class Liste_objets:
    '''
    @class ListeDobjet
        une collection qui est composé d'une liste d'objets
    @var
        une liste d'objets {liste_objets}
    '''
    # constructeur de la classe
    def __init__(self):
        # liste des objets
        self._liste_objets = list()
    
    # méthode d'affichage de la liste d'objet
    def afficher(self):
        if self._liste_objets: # si la liste n'est pas vide
            for objet in self._liste_objets:
                print(objet)
        else:
            # on renvoie un message à l'utilisateur
            print("-- Il n'y a pas d'objet dans la liste --")
    
    # getters de la liste d'objets
    def get_liste(self):
        return self._liste_objets
    
    # getters pour le nombre d'objets dans la liste
    def get_nb_objets(self):
        return len(self._liste_objets)
    
    # méthode d'ajout d'un objet dans la liste
    def ajouter(self, objet):
        if type(objet) != Objet:
            print("-- Le type de l'objet ne correspond pas --")
        elif objet.get_nom() == "":
            print("-- L'objet ne possède pas de nom --")
        else:
            self._liste_objets.append(objet)
    
    # méthode pour effacer la liste d'objet
    def effacer(self):
        self._liste_objets = []
