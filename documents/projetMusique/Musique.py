# VERSION 1.2 DE LA CLASSE MUSIQUE

import pygame
import time
import threading
import pygame.midi

# faire fonctionner pygame midi
pygame.midi.init()
music = pygame.midi.Output(0)
music.set_instrument(0,1)


# dictionnaires des notes
dico_note = {
            # note -Do- (60) et ses accords majeurs, mineurs et suspendus
            'Cb':59 , 'C':60 , 'C#':61 ,
            'Cbma':['Cb',0,4,7] , 'Cma':['C',0,4,7] , 'C#ma':['C#',0,4,7] ,
            'Cbmi':['Cb',0,3,7] , 'Cmi':['C',0,3,7] , 'C#mi':['C#',0,2,7] ,
            'Cbsus2':['Cb',0,2,7] , 'Csus2':['C',0,2,7] , 'C#sus2':['C#',0,2,7] ,
            'Cbsus4':['Cb',0,5,7] , 'Csus4':['C',0,5,7] , 'C#sus4':['C#',0,5,7] ,

            # note -Ré- (62) et ses accords majeurs et mineurs
            'Db':61 , 'D':62 , 'D#':63 ,
            'Dbma':['Db',0,4,7] , 'Dma':['D',0,4,7] , 'D#ma':['D#',0,4,7] ,
            'Dbmi':['Db',0,3,7] , 'Dmi':['D',0,3,7] , 'D#mi':['D#',0,3,7] ,
            'Dbsus2':['Db',0,2,7] , 'Dsus2':['D',0,2,7] , 'D#sus2':['D#',0,2,7] ,
            'Dbsus4':['Db',0,5,7] , 'Dsus4':['D',0,5,7] , 'D#sus4':['D#',0,5,7] ,

            # note -Mi- (64) et ses accords majeurs et mineurs
            'Eb':63 , 'E':64 , 'E#':65 ,
            'Ebma':['Eb',0,4,7] , 'Ema':['E',0,4,7] , 'E#ma':['E#',0,4,7] ,
            'Ebmi':['Eb',0,3,7] , 'Emi':['E',0,3,7] , 'E#mi':['E#',0,3,7] ,
            'Ebsus2':['Eb',0,2,7] , 'Esus2':['E',0,2,7] , 'E#sus2':['E#',0,2,7] ,
            'Ebsus4':['Eb',0,5,7] , 'Esus4':['E',0,5,7] , 'E#sus4':['E#',0,5,7] ,

            # note -Fa- (65) et ses accords majeurs et mineurs
            'Fb':64 , 'F':65 , 'F#':66 ,
            'Fbma':['Fb',0,4,7] , 'Fma':['F',0,4,7] , 'F#ma':['F#',0,4,7] ,
            'Fbmi':['Fb',0,3,7] , 'Fmi':['F',0,3,7] , 'F#mi':['F#',0,3,7] ,
            'Fbsus2':['Fb',0,2,7] , 'Fsus2':['F',0,2,7] , 'F#sus2':['F#',0,2,7] ,
            'Fbsus4':['Fb',0,5,7] , 'Fsus4':['F',0,5,7] , 'F#sus4':['F#',0,5,7] ,

            # note -Sol- (67) et ses accords majeurs et mineurs
            'Gb':66 , 'G':67 , 'G#':68 ,
            'Gbma':['Gb',0,4,7] , 'Gma':['G',0,4,7] , 'G#ma':['G#',0,4,7] ,
            'Gbmi':['Gb',0,3,7] , 'Gmi':['G',0,3,7] , 'G#mi':['G#',0,3,7] ,
            'Gbsus2':['Gb',0,2,7] , 'Gsus2':['G',0,2,7] , 'G#sus2':['G#',0,2,7] ,
            'Gbsus4':['Gb',0,5,7] , 'Gsus4':['G',0,5,7] , 'G#sus4':['G#',0,5,7] ,

            # note -La- (69) et ses accords majeurs et mineurs
            'Ab':68 , 'A':69 , 'A#':70 ,
            'Abma':['Ab',0,4,7] , 'Ama':['A',0,4,7] , 'A#ma':['A#',0,4,7] ,
            'Abmi':['Ab',0,3,7] , 'Ami':['A',0,3,7] , 'A#mi':['A#',0,3,7] ,
            'Absus2':['Ab',0,2,7] , 'Asus2':['A',0,2,7] , 'A#sus2':['A#',0,2,7] ,
            'Absus4':['Ab',0,5,7] , 'Asus4':['A',0,5,7] , 'A#sus4':['A#',0,5,7] ,

            # note -Si- (71) et ses accords majeurs et mineurs
            'Bb':70 , 'B':71 , 'B#':72 ,
            'Bbma':['Bb',0,4,7] , 'Bma':['B',0,4,7] , 'B#ma':['B#',0,4,7] ,
            'Bbmi':['Bb',0,3,7] , 'Bmi':['B',0,3,7] , 'B#mi':['B#',0,3,7] ,
            'Bbsus2':['Bb',0,2,7] , 'Bsus2':['B',0,2,7] , 'B#sus2':['B#',0,2,7] ,
            'Bbsus4':['Bb',0,5,7] , 'Bsus4':['B',0,5,7] , 'B#sus4':['B#',0,5,7] ,
            }


# dico des silence
dico_pause = { '/*':0.25 , '/':0.5 , '&':1 , '-':2 , '--':4 }


# dico des volumes ( inutulisable -> problème de décalage lors de la lecture )
dico_volume = { 's':10 , 'pp':20 , 'p':40 , 'mp':60 , 'm':70 , 'mf':80 , 'f':100 , 'ff':120 }


'''
La Classe Musique consiste à convertire une chaine de caractère ( partition )
en une liste qui sera lus et jouer en meme temps.
'''

# La Classe Musique
class Musique():

    ''''''''''''''''''

    # constructeur
    def __init__(self , fichier:str , instrument:int , volume:int , tempo:int):
        # la partition a lire sous forme de chaine de caractère
        self.partition = fichier
        # la note ( valeur de la note )
        self.n = 0
        # la fréquence ( hauteur de la note )
        self.f = 0
        # le ton ( longueure de la note )
        self.t = 0
        # le tempo ( 1 -> 240 , probleme quand le tempo est à 0 et trop haut )
        self.tempo = tempo
        # le volume ( 0 -> 127 )
        self.v = volume
        # l'instrument ( 0 -> 127 , voire liste des instruments >non_mis_à_jours< )
        self.i = instrument

    ''''''''''''''''''''''''''''''''''''

    # methode qui reconnait la note
    def set_note(self , n):
        try:
            # si la note ( simple ou accord ) est déjà dans le dictionnaire
            self.n = dico_note[n]
        except:
            # sinon il enregistre la valeur lus directement en espérent que se soit ( 1 -> 127 ) ou ( [{note},{valeur_au_dessus}...,] )
            self.n = n

    ''''''''''''''''''''''''''''''''''''

    # methode pour chosir la fréquence de la note
    def set_frequence(self, f):
        # verifie si la fréquence lus n'est ni trop basse ou trop haute ( on l'entendra pas )
        if -5 <= f <= 5:
            # si la note est simple
            if type(self.n) == int:
                # on augmente d'un octave en dessus ou en dessous
                self.n += 12*f
            # si la note est un accord ( une liste  )
            else:
                # pour chaque aumentation dans la liste
                for i in range(1,len(self.n)):
                    self.n[i] += dico_note[self.n[0]]+(12*f)
        # on retourne la valeur e la note diminué ou aumenté
        return self.n

    ''''''''''''''''''''''''''''''''''''

    # methode qui corrige un probleme d'accumulation sur une variable (flemme de faire plus propre)
    def reset(self,f):
        for i in range(1,len(self.n)):
            # on rénitialise les valeurs
            self.n[i] -= dico_note[self.n[0]]+(12*f)

    ''''''''''''''''''''''''''''''''''''

    # methode pour choisir le ton de la note ( noir, croche, double croche )
    def set_ton(self, t):
        numerateur = int(t[0])
        denominateur = int(t[-1])
        if type(numerateur) and type(denominateur) == int:
            # division des deux entiers pou la longueur de la note
            self.t = round(numerateur/(denominateur),2)
            # on verifie si le tempo est entre 1 et 240
            if 0 < self.tempo <= 240:
                # on modifie le ton selon le tempo
                self.t = self.t*(60/self.tempo)
                # on retourne le ton modifié
                return self.t

    ''''''''''''''''''''''''''''''''''''

    # methode principale qui joue la partition avec les valeurs stocker
    def jouer(self):
        # choix de l'instrument
        music.set_instrument(self.i,1)
        # si la note est simple on utilise la methode go
        if type(self.n) == int:
            self.go()
        # si la note est un accord on utilise alors la methode chord
        else:
            self.chord()
            # probleme de valeurs qu'on doit remettre à zero
            self.reset(self.f)

    ''''''''''''''''''''''''''''''''''''

    # seconde methode princpipale qui lis une liste et stock les valeurs des sous listes
    def lire(self):
        # utilise la methode conversion pour transformer la chaine de caractère en liste
        liste_note = self.conversion()
        # pour chaque élements dans la liste
        for elements in liste_note:
            # si l'élément est une liste soit une note
            if type(elements) == list:
                # la première valeur de la sous liste est la valeur de la note ( dico_note )
                self.set_note(elements[0])
                # la deuxième valeur de la sous liste est la hauteur de la note ( entre -4 octave et +4 octave )
                self.set_frequence(elements[1])
                # la troisième et dernière valeur de la sous liste est la longueur de la note
                self.set_ton(elements[2])
                # on joue la note en utilisant la methode jouer()
                self.jouer()
            # en revanche si l'élément n'est pas une note mais qu'il appartient au dico des volumes...
            if type(elements) != list and elements in dico_volume:
                # on change le volume selon la valeur de l'élément
                self.v = dico_volume[elements]
            # sinon si l'élément n'est pas une note mais qu'il appartient au dico des pauses...
            elif type(elements) != list and elements in dico_pause:
                # on fait une pause selon la valeurs de l'élément et le tempo
                time.sleep(dico_pause[elements]*(60/self.tempo))

    ''''''''''''''''''''''''''''''''''''

    # troisième methode principale qui convertis une chaine de caractère en liste de liste
    def conversion(self):
        # on rajoute un caractère espace pour l'algorithme nul qui en a besoins pour s'arreter
        chaine = self.partition + ' '
        # on fait un parcour de la chaine une première fois ( vous êtes pas prêt... )
        for i in range(len(chaine)):
            # si on rencontre un "saut de page"
            if chaine[i] == '\n':
                # on le remplace par un espace ( soit chaine[i] = ' ' )
                chaine = chaine[:i] + ' ' + chaine[i+1:]
        # cette liste sera celle retournée et contiendra toutes la valeurs reconnnus et enregistrée à partir de chaine
        liste_note = []
        # une sorte d'enregistreur de passage qui sera append() à la liste
        element = ''
        # cette fois on fait une conversion brute en parcourant une seconde fois la chaine de caractère
        for i in range(len(chaine)):
            # si element n'est pas vide alors on a enregistrée des valeurs et si on rencontre un espace alors il n'y a plus de suite à l'élément a enregistré
            if len(element)>0 and chaine[i] == ' ':
                # on ajoute l'élément à la liste
                liste_note.append(element)
                # on vide la variable pour le prochain élément
                element = ''
            # si le caractère lus n'est ni un espace ni un saut de page
            elif chaine[i] not in [' ','\n']:
                # on l'ajoute à la variable et on continu la lecture
                element += chaine[i]

        '''
        ici on à fait une lecture brute et dans la liste de note tous les éléments sont en str
        il ne reste plus qu'à la reparcourir mais cette fois ci de manière plus intélligente en reconnaissant si l'élément est une note
        soit une chaine de caractère avec des petits éléments entourés de paranthèse.
        '''

        # On termine avec une conversion des notes en sous listes en parcourant un troisième fois

        # on créer une pile pour savoir ensuite dans quelle "sousliste" nous somme
        pile = []

        # donc pour chaque élément dans la grande liste de note
        for i in range(len(liste_note)):
            # si le premier caractère de l'element i est une paranthèse alors on a rencontré une note
            if liste_note[i][0] == '(':
                # on refait la meme chose qu'avant
                liste = []
                sous_liste = []
                element = ''
                # mais cette fois ci la chaine est l'élément
                chaine = liste_note[i]
                # et on ajoute une paranthèse a la pile pour dire qu'on se trouve dans la note
                pile.append('(')
                # donc pour chaque caractère dans la chaine en partant de 1 puisqu'on ne prend pas les paranthèse
                for j in range(1,len(chaine)):
                    # si le car est un crochet on rentre alors dans une sousliste d'élément qui est un accord ( la deuximème condition est pour la suite si on est toujours dans la sous liste )
                    if chaine[j] == '[' or pile[-1]=='[':
                        # on ajoite un crochet a la pile si on rentre pour la première fois dans la sous liste
                        if '[' not in pile:
                            pile.append('[')
                        # si on rencontre un crochet fermé c'est qu'on a finis avec la sous liste
                        elif chaine[j] == ']':
                            # on ajoute le dernier élément
                            try:sous_liste.append(int(element))
                            except:sous_liste.append(element)
                            # et on ajoute la sous liste à la liste
                            liste.append(sous_liste)
                            # on vide les variales
                            sous_liste = []
                            element = ''
                            # on depile le crochet pour ne plus rentrer dans la condition actuelle
                            pile.pop()
                        # si on rencontre une virgule alors on va passer à un autre élément de la sous liste
                        elif chaine[j] == ',':
                            # donc si notre variable n'est pas vide (en cas de probleme)
                            if element != '':
                                # on l'ajoute a la sous liste
                                try:sous_liste.append(int(element))
                                except:sous_liste.append(element)
                                # on rénitialise la variable
                                element = ''
                        # sinon si on ne rencontre ni un crochet fermant ou une virgule on est toujours sur l'élément à enregistrée
                        else:
                            # et on enregistre les données lus
                            element += chaine[j]
                    # On arrive aux conditions où nous ne sommes pas sur une sous liste pour ceux qui sont perdus
                    # si on rencontre une paranthèse fermée c'est qu'on a finis avec la liste
                    elif chaine[j] == ')':
                        # on ajoute le dernier élément
                        try:liste.append(int(element))
                        except:liste.append(element)
                        # et on remplace l'ancienne chaine de caractère par la liste (note)
                        liste_note[i] = liste
                        # on vide les variales
                        liste = []
                        element = ''
                        pile.pop()
                    # si on rencontre une virgule alors on va passer à un autre élément de la sous liste
                    elif chaine[j] == ',':
                        # si notre variable n'est pas vide (en cas de probleme)
                        if element != '':
                            # on l'ajoute a la liste
                            try:liste.append(int(element))
                            except:liste.append(element)
                            # on rénitialise la variable
                            element = ''
                    # encore une fois si on ne rencontre ni un crochet fermant ou une virgule on est toujours sur l'élément à enregistrée
                    else:
                        # donc on enregistre les données lus
                        element += chaine[j]
        # on retourne enfin la partition convertis de chaine de caractère en liste
        # elle pourrais etre lus par la fonction lire
        return liste_note

    ''''''''''''''''''''''''''''''''''''

    # methode qui joue une note
    def go(self):
        # on lance la note avec sa valeur et son volume
        music.note_on(self.n, self.v,1)
        # on arrete le programme pendant un instant t pour la longueur de la note
        time.sleep(self.t)
        # on ferme la note
        music.note_off(self.n, self.v,1)

    ''''''''''''''''''''''''''''''''''''

    # methode qui joue un accord
    def chord(self):
        # pour chaque augmentation de la note pour un accord
        for i in range(1,len(self.n)):
            # on lance l'accord avec sa valeur et son volume
            music.note_on(self.n[i],self.v,1)
        # on arrete le programme pendant un instant t pour la longueur de l'accord
        time.sleep(self.t)
        # pour chaque augmentation de la note pour un accord
        for i in range(1,len(self.n)):
            # on ferme la note
            music.note_off(self.n[i],self.v,1)

''''''''''''''''''''''''''''''''''''



def test():
    test = Musique("(Bbma,1,3/1) (Bbmi,1,3/1) (Bbsus4,1,3/1)",0,120,120)
    print(test.conversion())
    test.lire()

def arpege():
    for i in range(12,84):
        arpege = Musique(f"({i},{(i//12)-3},1/4)",1,120,120)
        arpege.lire()