#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 21:50:30 2023

@author: javeriajalil
"""

#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

#Partner's name: Madeline Wong
#Partner's email:mwong20@bu.edu
    

from board import Board

# write your class below.

class Player:
    """ a data type for a Connect Four player
    """
    def __init__(self, checker):
        """ Initializes a Player object using the specified checker and keeping track of the number of moves used
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
       
    def __repr__(self):
        """ Returns a string that represents a Player object.
        """
        s = 'Player ' + self.checker
        return s
   
    def opponent_checker(self):
        """ Returns the string representing the opponent player's checker
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
       
    def next_move(self, b):
        """ Adds the player's checker to the specified valid column and returns the number of that column
        """
        while True:
            col = int(input("Enter a column: "))
            if b.can_add_to(col) == True:
                break
            else:
                print("Try again!")
       
        self.num_moves += 1
        return col 
       
       
       
      
        