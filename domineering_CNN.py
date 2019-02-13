# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 16:46:21 2018

@author: oussama
"""

import domineering_random as domineering
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.layers.core import Dense, Activation, Flatten
from keras.layers.convolutional import Convolution2D
from keras.optimizers import SGD , Adam
import copy


# Data augmentation : generate the positions for the four symmetries of a board.
def transform(board):
    '''
    we should first transform the board in an array
    if the grid is not null, the value is 1, otherwise, is 0 
    '''
    board = []
    for i in range(board.size):
        temp = []
        for j in range(board.size):
            if board.Grid[(i,j)].label == None:
                temp.append(0)
            else:
                temp.append(1)
        board.append(temp)
        
    return board
    

def flipped_board(board):
    """this function transform the board if a case in board 
        take the value 1 it will be assigned to 0 in flipped board and vice verca	"""
    board_flipped_board = []
    for i in range(len(board)):
        temp = []
        for j in range(len(board[0])):
            if board[i][j] == 1:
                temp.append(0)
            else:
                temp.append(1)
        board_flipped_board.append(temp)
        
    return board_flipped_board
           
            
def symmetry_up_down(board):
    """this function generate the positions for two symmetries of a 
	board up/down"""
    n = len(board)
    for i in range(int(n/2)):
        for j in range(n):
            board[i][j], board[n-i-1][j] = board[n-i-1][j], board[i][j]
    return board
    
    
def symmetry_left_right(board):
    """this function generate the positions for two symmetries of a 
	board left/right"""
    n = len(board)
    for i in range(n):
        for j in range(int(n/2)):
            board[i][j], board[i][n-j-1] = board[i][n-j-1], board[i][j]
    return board

    
def affiche(board):
    """this function display the board"""
    for i in range(len(board)):
        print(board[i])
    print("\n")
    
def Convnets(inp):
    ''' this function train the model to predict the next best move correctlty
    we can assign one of the created data above to train the model '''
    inp='domineering.csv'
    dataset = pd.read_csv(inp, sep=',')
    X = dataset.iloc[:, 0:192].values
    y = dataset.iloc[:, 192:256].values
    dataset = pd.read_csv(inp, sep=',')
    X = dataset.iloc[:, 0:192].values
    y = dataset.iloc[:, 192:256].values
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
    X_train = X_train.reshape(X_train.shape[0],3, 8, 8)
    X_test = X_test.reshape(X_test.shape[0],3,8, 8)
    print("Now we build the model")
    model = Sequential()
    #  - Convolution
    model.add(Convolution2D(64,3,8,border_mode='same',activation='relu', input_shape=(3,8,8)))
    model.add(Flatten())
    #  - Full connection
    model.add(Dense(output_dim = 128, activation = 'relu'))
    model.add(Dense(output_dim = 64, activation = 'softmax'))
    k=model.compile(loss='mse',optimizer='rmsprop', metrics=['accuracy'])
    print("We finish building the model") 
    #  Fit model on training data
    sc=model.fit(X_train, y_train,batch_size=20, nb_epoch=5, verbose=1)
    #  Evaluate model on test data
    # Score trained model.
    scores = model.evaluate(X_test, y_test, verbose=1)
    print('Test loss:', scores[0])
    print('Test accuracy:', scores[1])   
    out=model.predict_proba(X_test)
    return out,sc

def predict_best_move(board, player):
    '''this function predict the next best move using CNN'''
    retour = None
    board_copy = copy.deepcopy(board)  
    net = Convnets(inp)
    #inputs = prepare_inputs(board,player)
    player = 'horizontale'
    liste_coups_possible = board_copy.possible_move(player)
    if not liste_coups_possible:
        retour = "pass"
    else:
        possiblite = []
        N_possible_Moves = len(liste_coups_possible)
        for i in range(N_possible_Moves):
            coup = liste_coups_possible[i]
            i, j = coup[0], coup[1]
            possiblite.append(out[i][j])
        best_choice = possiblite.index(max(possiblite))
        retour = liste_coups_possible[best_choice]
    return retour
   
if __name__ == '__main__':    
    board = domineering.Grid(8)
    player = "verticale"
    carry_on = True
    inp='domineering.csv'
    while carry_on:
        print(board)
        print(player)
        if player=='verticale':
            retour = board.random_move("verticale")
            board.jouer(retour[0],retour[1],retour[2],retour[3],"verticale")
            coup=[]
            if retour == 'pass' and coup != 'pass':
                carry_on = False
                print("horizontale win")
                break 
        else:
            coup = predict_best_move(board,'horizontale')
            board.jouer(coup[0],coup[1],coup[2],coup[3],'horizontale')
            if len(coup) == 'pass' and len(retour) != 'pass':
                carry_on = False
                print("verticale win")
                break
           
        if coup == 'pass' and retour == 'pass':
            carry_on = False
            print("draw")
            break
       
        else: 
           carry_on = True
           print("Please wait until the game finished")
        
        
        player = board.turn(player)
        
        
    print(board)
    
