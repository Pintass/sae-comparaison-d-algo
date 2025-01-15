##############################################################################
# votre IA : à vous de coder
# Rappel : ne pas changer les paramètres des méthodes
# vous pouvez ajouter librement méthodes, fonctions, champs, ...
##############################################################################

import random

class IA_Bomber:
    def __init__(self, num_joueur : int, game_dic : dict, timerglobal : int, timerfantôme: int) -> None:
        """génère l'objet de la classe IA_Bomber

        Args:
            num_joueur (int): numéro de joueur attribué à l'IA
            game_dic (dict): descriptif de l'état initial de la partie
        """

    #TODO
    pass


    def parcours_largeur(self, map: list, sommet_depart: tuple):
        """
        parcours_largeur est une fonction permettant de trouver le chemin le plus rapide vers une position donnée

        ##A CHANGER ##A CHANGER ##A CHANGER ##A CHANGER ##A CHANGER 
        Args: 
        self (class)
        map (list): représente la map sous forme de list.
        sommet_depart(tuple): représente les coordonnées de départ sur l'axe x et y du joueur. 
        """
        distance = {}
        distance[sommet_depart] = 0
        pred = {}
        attente = []  #file d'attente
        attente.append(sommet_depart)
        
        while len(attente) > 0:
            courant = attente.pop(0) #sommet dont on va chercher les voisins
            
            #chercher les voisins de courant
            voisins_possibles = [(courant[0]+1,courant[1]), (courant[0]-1,courant[1]), (courant[0],courant[1]+1), (courant[0],courant[1]-1) ]
            for v in voisins_possibles:
                if map[v[0]][v[1]] == ' ' : #si c'est une case vide
                    if v not in distance :  #si v est encore inconnu
                        # dans ce cas v est une case voisine vide et inconnue
                        distance[v] = distance[courant] + 1
                        pred[v] = courant
                        attente.append(v)  #v devra devenir courant plus tard
        """ATTENTION : actuellement la fonction ne trouve pas le point que l'on souhaite mais le fait de parcourir toute la map le plus rapidement possible, il faudrait adapter cela : 
        
        chemin = []
        arrivée = (3,19)

        c = arrivée
        while c != (1,1):
            chemin.append(c)
            c = pred[c]
        chemin.append((1,1))
        print(chemin)
        permettant de définir notre arrivée cependant ATTENTION UNE FONCTION NE DOIT PAS FAIRE PLUS DE 15-20 LIGNES"""                
    
    return distance, pred

    def action(self, game_dict : dict) -> str:
        """Appelé à chaque décision du joueur IA

        Args:
            game_dict (dict) : décrit l'état actuel de la partie au moment
            où le joueur doit décider son action

        Returns:
            str : une action 
        """

        #############################################################
        #ICI il FAUT compléter/remplacer et faire votre version !   #
        #############################################################

        #exemple d'IA basique
        #ici pour prescrire une suite d'actions fixes au début si on veut
        t = game_dict['compteur_tour']
        suite = ['D','D','D','X','G','G','G']
        if t < len(suite):
            return suite[t]

        #puis choisir des actions au hasard
        actions = ['D', 'G', 'H', 'B','X','N']
        return random.choice(actions)


