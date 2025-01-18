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
        self.game_dict = game_dic
        self.nom_joueur = num_joueur
        self.chemin_effectue = []

        self.esquiver_bombe = False
        self.tour_bombe_posee = None

    def trouver_chemin(self, point_depart, point_arrivee, pred):
        chemin = []

        c = point_arrivee
        while c != point_depart:
            chemin.append(c)
            c = pred[c]   
        chemin.reverse()
        return chemin 

    def gestion_bombe(self, pos_joueur: tuple, pred: dict):
        """ Gestion_bombe permet de gérer les bombes lrosque l'IA pose une bombe en faisant reculer l'IA pour pas qu'elle puisse se prendre de dégâts
        Args: 
            pos_joueur (tuple): permet de connaître la position du joueur
            pred (tuple): permet de connaître les anciennes positions du joueur pendant son chemin
        """
        if self.esquiver_bombe:
            if self.tour_bombe_posee + 4 == self.game_dict['compteur_tour']:
                self.esquiver_bombe = False
                self.tour_bombe_posee = None
                return 'N'
            
            index = self.index_actuel
            if index < 0:
                self.esquiver_bombe = False
                self.tour_bombe_posee = None
                return 'N'
            
            action = self.inverse(self.chemin_effectue[index])
            self.index_actuel -= 1

            return action

        else:
            self.esquiver_bombe = True
            self.tour_bombe_posee = self.game_dict['compteur_tour']
            self.index_actuel = len(self.chemin_effectue) - 1
            return 'X'

    def trouver_position_destination(self, position_actuelle: tuple, position_souhaitee: tuple) -> str:
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

        mouvement = 'N'
        if diff_x == 1 and diff_y == 0 and not self.verifier_danger_bombe((position_actuelle[0] + 1, position_actuelle[1])):
            mouvement = 'D'
        if diff_x == -1 and diff_y == 0 and not self.verifier_danger_bombe((position_actuelle[0] - 1, position_actuelle[1])):
            mouvement = 'G'
        if diff_y == -1 and diff_x == 0 and not self.verifier_danger_bombe((position_actuelle[0], position_actuelle[1] - 1)):
            mouvement = 'H'
        if diff_y == 1 and diff_x == 0 and not self.verifier_danger_bombe((position_actuelle[0], position_actuelle[1] + 1)):
            mouvement = 'B'
        
        return mouvement
        
    def verifier_danger_bombe(self, pos):
        """Vérifie si une position est dans la zone de danger d'une bombe"""
        if not pos:
            return True
            
        for bombe in self.game_dict['bombes']:
            bombe_x = bombe['position'][0]
            bombe_y = bombe['position'][1]
            portee = bombe['portée']
            
            # Même ligne ou colonne que la bombe
            if pos[0] == bombe_x:
                if abs(pos[1] - bombe_y) <= portee:
                    return True
            if pos[1] == bombe_y:
                if abs(pos[0] - bombe_x) <= portee:
                    return True

        return False

    #def doit_poser_bombe(self, map:dict)

    def parcours_largeur(self, map: dict, sommet_depart: tuple):
        """
        parcours_largeur est une fonction permettant de trouver le chemin le plus rapide vers une position
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



    def analyse_position(self, distance: dict):
        for v in distance:
            voisins_possibles = [(v[0]+1,v[1]), (v[0]-1,v[1]), (v[0],v[1]+1), (v[0],v[1]-1)]
            for j in voisins_possibles:
                if self.game_dict['map'][j[1]][j[0]] == 'M':
                    return v
        return None #dans le cas où y'a rien
    
    def inverse(self, action: str):
        if action == "H":
            return "B"
        if action == "B":
            return "H"
        if action == "G":
            return "D"
        if action == "D":
            return "G"
        return "N"
    
    def debug_game_dict(self):
        print("---- DEBUG GAME DICT ----")
        print(self.game_dict)
        print("---- DEBUG GAME DICT ----")
        

    def action(self, game_dict : dict) -> str:
        """Appelé à chaque décision du joueur IA

        Args:
            game_dict (dict) : décrit l'état actuel de la partie au moment
            où le joueur doit décider son action

        Returns:
            str : une action 
        """

        self.debug_game_dict()

        #############################################################
        #ICI il FAUT compléter/remplacer et faire votre version !   #
        #############################################################

        #exemple d'IA basique
        #ici pour prescrire une suite d'actions fixes au début si on veut
        self.game_dict = game_dict
        pos_joueur = game_dict['bombers'][self.nom_joueur]['position']
        distance, pred = self.parcours_largeur(game_dict['map'], pos_joueur)
        cible = self.analyse_position(distance)
        print(cible)
        if cible is not None:

            action_choisie = None
            if cible == pos_joueur or self.esquiver_bombe:
                print("--- GESTION DE LA BOMBE")
                action_choisie = self.gestion_bombe(pos_joueur, pred)
            else:
                print("--- GESTION DU CHEMIN")
                chemin = self.trouver_chemin(pos_joueur, cible, pred)
                if chemin:
                    action_choisie = self.trouver_position_destination(pos_joueur, chemin[0])
            
            self.chemin_effectue.append(action_choisie)
            print("Action choisie : ", action_choisie)
            print(self.chemin_effectue)
            return action_choisie
                   
        return "N"
