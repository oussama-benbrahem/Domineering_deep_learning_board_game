# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 22:18:57 2018

@author: oussama
"""

import random

"""la classe grid definie la grille (le terrain de jeu) et les régles de jeu """
class Grid():
    def __init__(self,size):
        self.size = size
        self.Grid = self.building()
        pass
    
    def __repr__(self):
        """cette fonction affichera la grille sur la console"""
        ligne = ''
        for i in range(self.size):
            for j in range(self.size):
                valeur = self.Grid[(i,j)]
                valeur = str(valeur)
                ligne =  ligne + '  ' + valeur
            ligne = ligne + '\n'
        return ligne      
    
    def building(self):
        """cette fonction crée la grille de taille spécifié dans la classe main"""        
        Grid = {}   
        for i in range(self.size):
            for j in range(self.size):
                Grid[(i,j)] = carreau(i,j)
        
        return Grid
    
    def jouer(self,i1,j1,i2,j2,player):
        """cette fonction joue les coups choisis par les 2 joueurs"""
        carreau1 = self.Grid[(i1,j1)]
        carreau2 = self.Grid[(i2,j2)]
        carreau1.label = player
        carreau2.label = player
    
    def possible_move(self,player):
        """cette fonction scan la grille est liste les coups possible pour chaque joueur"""
        liste_coups_possible = []
        if player == "horizontale":
            for i in range(self.size):
                for j in range(self.size-1):
                 if self.Grid[(i,j)].label == None and self.Grid[(i,j+1)].label == None:
                     liste_coups_possible.append([i,j,i,j+1])
        else:
            for j in range(self.size):
                for i in range(self.size-1):
                 if self.Grid[(i,j)].label == None and self.Grid[(i+1,j)].label == None:
                     liste_coups_possible.append([i,j,i+1,j])
            pass
        return liste_coups_possible    
    
    def random_move(self,player):
        """cette fonction pour chaque joueur choisi le coup a joué parmis la liste 
            des coups possible de chacun"""
        move = None        
        liste_coups_possible = self.possible_move(player)
        if(len(liste_coups_possible) != 0):
            rand = random.randint(0,len(liste_coups_possible)-1)
            move = liste_coups_possible[rand]
        else:
            move = "pass"
        return  move
    
    def jeu_finis(self,player):
        """"cette fonction définie une condition d'arrét du jeu, si l'un des joueurs joue 
            tous ces coups possible"""
        if len(self.possible_move(player)) == 0:
            return True
        else:
            return False
            
    def turn(self,player):
        """ cette fontion alterne le changement des joueurs """
        if player=="verticale":
            player="horizontale"
        else :
            player="verticale"
        return player
   
class carreau():
    def __init__(self,i,j):
        self.i = i
        self.j = j
        self.label = None
        
    def __repr__(self):
        """cette fonction represente les labels qui peut prendre chaque carreau """
        if self.label == None:
            return '.'
        elif self.label == 'verticale':
            return 'x'
        elif self.label == 'horizontale':
            return '+'


      
if __name__ == "__main__":
    
    board = Grid(8)
    player = ['verticale', 'horizontale']
    player = random.choice(player)
    while (board.jeu_finis(player)== False):
        move = board.random_move(player)
        print(board.possible_move("horizontale"))
        board.jouer(move[0],move[1],move[2],move[3],player)
        player = board.turn(player)
        print(board)
        if len(board.possible_move("horizontale")) == 0 and len(board.possible_move("verticale")) != 0:
            print("le joueur verticale win the game")
        elif len(board.possible_move("verticale")) == 0 and len(board.possible_move("horizontale")) != 0:
            print("le joueur horizontale win the game")
        elif len(board.possible_move("verticale")) == 0 and len(board.possible_move("horizontale")) == 0:
            print("No winner :draw")
        else:
            print("Please wait until the game finished ...")
    
   