# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 22:21:35 2018

@author: oussama
"""

import domineering_random
import copy 

def coup_alea(board,player):
    """joué des coups aléatoire jusqu'a la fin de partie"""  
    board_copy = copy.deepcopy(board)    
    
    carry_on = True
    player_IA = player
        
    while carry_on:
        move = board_copy.random_move(player)
        if move == "pass":  # Si l'un des deux players passe, on arrête  la partie
            carry_on = False
        else:
            board_copy.jouer(move[0],move[1],move[2],move[3],player)
            player = board.turn(player)
    
    if player == player_IA:
        score = 0 # si le joueur perd il gagne rien
    else:
        score = 1 # si le joueur gagne on lui affecte une récompense 
    
    return score

def playouts(board, player):
    '''cette fonction simule 100 partie aléatoire est calcul la récompense'''
    playout_number = 100
    total_score = 0
    board_copie = copy.deepcopy(board)
    
    i = 0
    while i < playout_number:
        total_score += coup_alea(board_copie,player)
        i = i+1
    return total_score
    
def meilleur_coup(board, player):
    '''cette fonction détermine le prochain meilleur coup possible'''
    move = None
    board_copy = copy.deepcopy(board)     
    liste_coups_possible = board_copy.possible_move(player)
    if not liste_coups_possible:
        move = "pass"
    else:
        scores_liste = []
        nb_possible = len(liste_coups_possible) 
        for i in range(nb_possible):
            coup = liste_coups_possible[i]
            board_copy.jouer(coup[0],coup[1],coup[2],coup[3],player)
            scores_liste.append(playouts(board_copy,player))
        meilleur_coup = scores_liste.index(max(scores_liste))
        move = liste_coups_possible[meilleur_coup]
    return move


if __name__ == '__main__':
    board = domineering_random.Grid(8)
    player = "horizontale"
    carry_on = True
    
    while carry_on:
        print(board)
        print(player)
        coup = meilleur_coup(board,player)
        print()
        
        if coup == "pass":
            carry_on = False
        else:
            board.jouer(coup[0],coup[1],coup[2],coup[3],player)
            player = board.turn(player)
        if len(board.possible_move("horizontale")) == 0 and len(board.possible_move("verticale")) != 0:
            print("le joueur verticale win the game")
        elif len(board.possible_move("verticale")) == 0 and len(board.possible_move("horizontale")) != 0:
            print("le joueur horizontale win the game")
        elif len(board.possible_move("verticale")) == 0 and len(board.possible_move("horizontale")) == 0:
            print("No winner :draw")
        else:
            print("Please wait until the game finished ...")
        
    print(board) 
    

         

        