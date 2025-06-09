'''
# # # # # # # # # # # # # # # # # # # # # # #
#                                           #
#     PROGRAMME PRINCIPAL - SAE2.02 KNN     #
#                                           #
# # # # # # # # # # # # # # # # # # # # # # #
'''

# importation des modules
import random             # module de l'aléatoire
from classe import *      # import du fichier python de la classe
from math import sqrt     # foncction racine du module math


def KNN( objet:Objet, liste:list, k:int ):
    ''' @def
            KNN
        @param
            un objet de la classe Objet
            une liste d'objets de la classe Objet
            un entier k représentant les k instances à retenir 
    '''
    # création de la collection des distances
    collection_distances = dict()
    
    # initialisation des distances
    for point in liste:
        collection_distances[point] = distance(objet.get_point(),point.get_point())
    
    # tri de la collection des distances dans l'ordre croissant
    collection_trie = dict() # création d'un dictionnaire temporaire
    for _ in range(k):
        # initialisation de la variable de la plus courte distance
        distance_minimale = float("inf")
        # pour chaque point dans la collection des distances
        for point in collection_distances:
            # si le point n'est pas dans la collection et que sa distance est la plus petite
            if collection_distances[point] < distance_minimale and point not in collection_trie.keys():
                distance_minimale = collection_distances[point]
                point_proche = point
        # on enregistre la valeur dans le dictionnaire temporaire
        collection_trie[point_proche] = distance_minimale
    
    collection_distances = collection_trie
    
    # on recherche l'étiquette la plus courante parmis les valeurs
    nb_etiquette_max = 0
    etiquette = "neutre"
    for point_i in collection_distances:
        nb_etiquette = 0
        for point_j in collection_distances:
            if point_j.get_groupe() == point_i.get_groupe():
                nb_etiquette += 1
        if nb_etiquette > nb_etiquette_max:
            nb_etiquette_max = nb_etiquette
            etiquette = point_i.get_groupe()
    
    # on donne l'étiquette à l'objet qu'on enregistre dans la liste
    objet.set_groupe(etiquette)
''' Fin de la fonction KNN  '''


def Kmeans( liste:list, k:int, n:int, p:int ):
    ''' @def
            Kmeans
        @param
            une liste d'objets de la classe Objet
            un entier k représentant les k instances à retenir
            un nombre d'itération n à effectuer
            une plage de génération p des centres des groupes
    '''
    # liste des centres
    liste_centres = []
    # dictionnaire des groupes de points autours des centres
    liste_groupes = dict()
    # liste des couleurs
    liste_couleurs = [clef for clef in collection_couleurs]
    liste_couleurs.pop(0)
    random.shuffle(liste_couleurs)
    # pour k instances on créer k centres
    for i in range(k):
        centre = Objet( liste_couleurs[i], random.randint(-p,p), random.randint(-p,p), liste_couleurs[i] )
        liste_centres.append( centre )
        liste_groupes[centre] = []
    
    # pour n itération on regroupe les points et recalcul les centres des groupes
    for i in range(n):
        # pour chaque point non étiquetté
        for point in liste:
            # on créer un dictionnaire temporaire des centres les plus proche du point
            centres_proches = dict()
            # pour chaque centre on calcul et enregistre la distance entre lui et le point
            for centre in liste_centres:
                centres_proches[centre] = distance(centre.get_point(),point.get_point())
            # on regarde quel est le centre le plus proche du point
            minimum = float("inf")
            for centre in centres_proches:
                if centres_proches[centre] < minimum:
                    minimum = centres_proches[centre]
                    centre_proche = centre
            
            # on place l'étiquette du groupe au point
            point.set_groupe(centre_proche.get_groupe())
            # on ajoute le point dans la liste du groupe
            liste_groupes[centre_proche].append(point)
        
        # pour chaque centre
        for centre in liste_centres:
            # on recalcul les coordonnées du centre
            if i == 0:
                # si c'est la première itération
                # on prend les coordonnées du premier centre dans la moyenne
                sommeX = centre.get_point()._x
                sommeY = centre.get_point()._y
                diviseur = 1
            else:
                # sinon on calcul la moyenne avec juste les points du groupe
                sommeX = 0
                sommeY = 0
                diviseur = 0
            # pour chaque point dans le groupe
            for point in liste_groupes[centre]:
                # on fait la sommme des points
                sommeX += point.get_point()._x
                sommeY += point.get_point()._y
                diviseur += 1
            # on met le diviseur à 1 si il n'y a pas de point dans le groupe et que c'est une n > 1 itération
            if n == 0:
                diviseur = 1
            # on calcul le nouveau centre avec la moyenne des coordonnées des points
            centre.set_point( (sommeX/diviseur) , (sommeY/diviseur) )
            # on efface les données des groupes pour la prochaine itération
            liste_groupes[centre] = []
''' Fin de la fonction Kmeans '''

# fonction pour calculer une distances euclidienne entre deux points
def distance(A,B):
    return sqrt( (A._x-B._x)*(A._x-B._x) + (A._y-B._y)*(A._y-B._y) )

# procédure pour afficher les options
def options():
    print("(-1) - lister les options")
    print("(1)  - (re)initialiser le plan")
    print("(2)  - afficher les objets du plan")
    print("(3)  - effacer le plan")
    print("(4)  - créer un point en particulier")
    print("(5)  - créer plusieurs points")
    print("(6)  - afficher la liste des points")
    print("(7)  - utiliser la fonction KNN sur un point en particulier")
    print("(8)  - utiliser la fonction KNN sur plusieurs points")
    print("(9)  - utiliser la fonction KNN sur tous les points de la liste")
    print("(10) - utiliser la fonction Kmeans sur un plan neutre")
    print("(11) - ajouter un point au plan")
    print("(12) - ajouter plusieurs points au plan")
    print("(13) - ajouter tous les points de la liste au plan")
    print("(0)  - quitter le programme.\n")

# procédure pour initialiser un plan avec des points étiquettés.
def initPlan(plan):
    for color in collection_couleurs:
        plan.ajouter(Objet(color[:2].upper(),random.randint(-20,20),random.randint(-20,20),color))

# fonction pour créer un point
def initPoint():
    x = int(input("  entrez la coordonnées x du point : "))
    y = int(input("  entrez la coordonnée y du point : "))
    nom = input("  entrez le nom du point : ")
    print()
    point = Objet(nom,x,y)
    return point

#procédure pour créer plusieurs points
def initPlusieursPoints():
    nbPoints = int(input("  Combien de points voulez vous créer : "))
    plage = int(input("  Donner un rayon de génération des points à partir de l'origine : "))
    for i in range(len(liste_points),len(liste_points)+nbPoints):
        nom = 'p'+str(i)
        x = random.randint(-plage,plage)
        y = random.randint(-plage,plage)
        liste_points.append(Objet(nom,x,y))
        
# fonction qui retourne une valeur pour k instances
def demande_k():
    k = int(input("  entrez le nombre k d'instances à retenir : "))
    while k < 1:
        print()
        print("  Le nombre de k instance doit être minimum à 1 !")
        k = int(input("  entrez le nombre k d'instances à retenir : "))
    return k

def demande_indice():
    indice = int(input("  entrez l'indice du point à étiquetter de la liste : "))
    while indice < 0 or indice >= len(liste_points):
        print()
        print("  L'indice du point doit être compris entre 0 et",len(liste_points)-1," !")
        indice = int(input("  entrez l'indice du point à ajouter de la liste : "))
    return indice

def demande_debut():
    debut = int(input("  entrez l'indice du point de départ à étiquetter de la liste : "))
    while debut < 0 or debut >= len(liste_points):
        print()
        print("  L'indice du point doit être compris entre 0 et",len(liste_points)-1," !")
        debut = int(input("  entrez l'indice du point de départ à ajouter de la liste : "))
    return debut

def demande_fin():
    fin = int(input("  entrez l'indice du point final à étiquetter de la liste : "))
    while fin < 0 or fin >= len(liste_points):
        print()
        print("  L'indice du point final doit être compris entre 0 et",len(liste_points)-1," !")
        fin = int(input("  entrez l'indice du point final à ajouter de la liste : "))
    return fin

# PROGRAMME PRINCIPAL
print("*****************************************")
print("***                KNN                ***")
print("*****************************************\n")
plan_objets = Liste_objets()
liste_points = []
options()
entree = input(">>> ")
print()

while( entree != "0" or entree == "stop" ):
    
    # initialiser le plan
    if entree == "1" or entree == "initPlan":
        initPlan(plan_objets)
        print("plan initialisé\n")
        print("Voulez-vous l'afficher ? (2)\n")
        
    # afficher le plan
    elif entree == "2" or entree == "affPlan":
        plan_objets.afficher()
        print()
        print("Voulez-vous l'effacer ? (3)")
        print("Voulez-vous utiliser KNN() sur un point de la liste ? (7)")
        print("Voulez-vous utiliser KNN() sur plusieurs points de la liste ? (8)")
        print("Voulez-vous utiliser KNN() sur tout les points de la liste ? (9)")
        print("Voulez-vous utiliser Kmeans() sur le plan ? (10)\n")
    
    elif entree == "3" or entree == "effPlan":
        plan_objets.effacer()
        print("plan effacé\n")
        print("Voulez-vous le réinitialisé ? (1)\n")
    
    # créer un point particulier
    elif entree == "4" or entree == "initPoint":
        print("Création d'un point")
        liste_points.append(initPoint())
        print("Voulez-vous l'afficher ? (6)\n")
    
    # créer plusieurs points
    elif entree == "5" or entree == "initPoints":
        initPlusieursPoints()
        print()
        print("Voulez-vous les affichers ? (6)\n")
    
    # lister les points créés
    elif entree == "6" or entree == "affPoints":
        if liste_points:
            print("Liste des points :")
            for i in range(len(liste_points)):
                print(" ",i,":",liste_points[i])
            print()
            print("Voulez-vous placer un point sur le plan ? (11)")
            print("Voulez-vous placer quelques points sur le plan ? (12)")
            print("Voulez-vous tous les placers sur le plan ? (13)\n")
            print("Voulez-vous utiliser KNN() sur un point de la liste ? (7)")
            print("Voulez-vous utiliser KNN() sur plusieurs points de la liste ? (8)")
            print("Voulez-vous utiliser KNN() sur tout les points de la liste ? (9)")
        else:
            print("Il n'y a pas de points dans la liste\n")
            print("Voulez-vous créer un point ? (4)")
            print("Voulez-vous créer plusieurs points ? (5)")
        
    
    # utilisation de la fonction KNN sur un point en particulier
    elif entree == "7" or entree == "KNN(1)":
        if len(liste_points) == 0:
            print("Il n'y a pas de points dans la liste\n")
            print("Voulez-vous créer un point ? (4)")
            print("Voulez-vous créer plusieurs points ? (5)")
        elif plan_objets.get_nb_objets() == 0:
            print("Il n'y a pas de points sur le plan\n")
        else:
            indice = demande_indice()
            k = demande_k()
            KNN( liste_points[indice], plan_objets.get_liste(), k )
        print("Voulez-vous afficher les points ? (6)\n")
        print("Voulez-vous placer un point sur le plan ? (11)")
        print("Voulez-vous placer quelques points sur le plan ? (12)")
        print("Voulez-vous tous les placers sur le plan ? (13)\n")
            
    
    # utilisation de la fonction KNN sur plusieurs points
    elif entree == "8" or entree == "KNN(*)":
        if len(liste_points) == 0:
            print("Il n'y a pas de points dans la liste\n")
            print("Voulez-vous créer un point ? (4)")
            print("Voulez-vous créer plusieurs points ? (5)")
        elif plan_objets.get_nb_objets() == 0:
            print("Il n'y a pas de points sur le plan\n")
        else:
            debut = demande_debut()
            fin = demande_fin()
            while debut > fin:
                print("  l'indice du point de départ doit être plus petit que celui de fin !")
                debut = demande_debut()
                fin = demande_fin()
            k = demande_k()
            for i in range(debut,fin+1):
                KNN( liste_points[i], plan_objets.get_liste(), k )
        print()
        print("Voulez-vous afficher les points ? (6)\n")
        print("Voulez-vous placer un point sur le plan ? (11)")
        print("Voulez-vous placer quelques points sur le plan ? (12)")
        print("Voulez-vous tous les placers sur le plan ? (13)\n")
    
    # utilisation de la fonction KNN sur tout les points
    elif entree == "9" or entree == "KNN(all)":
        if len(liste_points) == 0:
            print("Il n'y a pas de points dans la liste\n")
            print("Voulez-vous créer un point ? (4)")
            print("Voulez-vous créer plusieurs points ? (5)")
        elif plan_objets.get_nb_objets() == 0:
            print("Il n'y a pas de points sur le plan\n")
        else:
            k = demande_k()
            for i in range(len(liste_points)):
                KNN( liste_points[i], plan_objets.get_liste(), k )
        print()
        print("Voulez-vous afficher les points ? (6)\n")
        print("Voulez-vous placer un point sur le plan ? (11)")
        print("Voulez-vous placer quelques points sur le plan ? (12)")
        print("Voulez-vous tous les placers sur le plan ? (13)\n")
    
    # utilisation de la fonction Kmeans
    elif entree == "10" or entree == "Kmeans()":
        if len(plan_objets.get_liste()):
            k = demande_k()
            iteration = int(input("  entrez le nombre d'itération à effectuer : "))
            plage = int(input("  entrez le rayon de génération des centres : "))
            Kmeans( plan_objets.get_liste(), k, iteration, plage )
        else:
            print("Le plan est vide")
        print()
        print("Voulez-vous afficher le plan ? (2)\n")
    
    # ajouter un point particulier au plan
    elif entree == "11" or entree == "ajoutPoint":
        indice = demande_indice()
        plan_objets.ajouter( liste_points[indice] )
        liste_points.remove( liste_points[indice] )
        print()
        print("Voulez-vous afficher le plan ? (2)")
        print("Voulez-vous afficher les points ? (6)\n")
        
    
    # ajouter plusieurs point au plan
    elif entree == "12"  or entree == "ajoutPoints":
        debut = demande_debut()
        fin = demande_fin()
        
        while debut > fin:
            print("  l'indice du point de départ doit être plus petit que celui de fin !")
            debut = demande_debut()
            fin = demande_fin()
        
        for i in range(debut,fin+1):
            plan_objets.ajouter( liste_points[i] )
        for _ in range(debut,fin+1):
            liste_points.remove( liste_points[debut] )
        
        print()
        print("Voulez-vous afficher le plan ? (2)")
        print("Voulez-vous afficher les points ? (6)\n")
    
    # ajouter tout les points au plan
    elif entree == "13" or entree == "ajoutPoints":
        for _ in range(len(liste_points)):
            plan_objets.ajouter( liste_points[0] )
            liste_points.remove( liste_points[0] )
        
        print()
        print("Voulez-vous afficher le plan ? (2)")
        print("Voulez-vous afficher les points ? (6)\n")
       
    # lister les différents options
    elif entree == "-1" or entree == "aide":
        options()
    
    # test de validité de la valeur d'entrée
    else:
        print("erreur : l'option choisi n'est pas valide\n")
    
    entree = input(">>> ")
    print()

print("Fin du programme.")