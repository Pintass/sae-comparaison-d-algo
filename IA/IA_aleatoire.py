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
        self.map = game_dic
        self._bombe_pose = None
        self.chemin_effectue = []

    #TODO
    pass

    def action(self, map : dict):
        """
        action permet à l'IA d'agir quand on lui demande
        Args: 
        map (dict): représente la map sous forme de dict.
        sommet_depart(tuple): représente les coordonnées de départ sur l'axe x et y du joueur. 
        """


    def trouver_position_destination(self, map: dict, position_actuelle: tuple, position_souhaitee: tuple) -> str:
        """trouver_position_destination permet d'obtenir l'action que l'IA doit effectuer pour se déplacer dans une position souhaitée
        Args: 
            map(dict): représente la map sous forme de dictionnaire donnant l'état du jeu actuel.
            position_actuelle(dict): permet de connaître le point de départ du déplacement.
            position_souhaitee(dict): permet de connaître le point final du déplacement.
        Returns: 
            (str) 
        """
        diff_x = position_souhaitee[0] - position_actuelle[0]
        diff_y = position_souhaitee[1] - position_actuelle[1]
        touche_resultat = None

        if diff_x == 1 and diff_y == 0:
            touche_resultat = "D"
            return touche_resultat
        if diff_x == -1 and diff_y == 0:
            touche_resultat = "G"
            return touche_resultat
        if diff_y == -1 and diff_x == 0:
            touche_resultat = "H"
            return touche_resultat
        if diff_y == 1 and diff_x ==0:
            touche_resultat = "B"
            return touche_resultat
        else: 
            touche_resultat = "N"
            return touche_resultat


    def doit_poser_bombe(self, map:dict)

        

    def parcours_largeur(self, map: dict, sommet_depart: tuple):
        """
        parcours_largeur est une fonction permettant de trouver le chemin le plus rapide vers une position donnée
        Args: 
        map (dict): représente la map sous forme de dict.
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
                if map[v[1]][v[0]] == ' ' : #si c'est une case vide
                    if v not in distance :  #si v est encore inconnu
                        # dans ce cas v est une case voisine vide et inconnue
                        distance[v] = distance[courant] + 1
                        pred[v] = courant
                        attente.append(v)  #v devra devenir courant plus tard
              
    
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


