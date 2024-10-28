import tkinter as tk
from tkinter import ttk
class BoardClass():
    """
    Boardclass object, when created, is designed to
    replicate the tkinter tic-tac-toe board move by move.

    Attributes:
        pun: Player's user name
        pun2: Other player's user name
        unlp: User name of the last player to make a move
        wins: Number of wins
        ties: Number of ties
        losses: Number of losses
        nogp: Number of games played
        gbstring: the board/grid of the tkinter interface in string form
    """
    
    pun = ''
    pun2 = ''
    unlp = '' 
    wins = 0 
    ties = 0 
    losses = 0 
    nogp = 0
    gbstring = "+---+---+---+\n| 1 | 2 | 3 |\n+---+---+---+\n| 4 | 5 | 6 |\n+---+---+---+\n| 7 | 8 | 9 |\n+---+---+---+"

    
    def __init__(self) -> None:
        """
        Creates the board class object

        Args:
            No args. taken.

        Returns:
            No value returned.
        """


    def set_name(self, player) -> None:
        """
        Sets the player name.

        Args:
            Takes the player name as an argument and storing it in the pun attribute/variable

        Returns:
            No value returned.
        """
        self.pun = player

    def set_name2(self, player) -> None:
        """
        Sets the other player's name.

        Args:
            Takes the player name as an argument and storing it in the pun2 attribute/variable

        Returns:
            No value returned.
        """
        self.pun2 = player

    
    def updateGamesPlayed(self) -> None:
        """
        Increments the nogp(number of games played) by 1
        
        Args:
            No args. taken

        Returns:
            No value returned.
        """
        self.nogp += 1


    def resetGameBoard(self) -> None:
        """
        Reset gbstring to original grid/board

        Args:
            No args. taken

        Returns:
            No value returned.
        """
        self.gbstring = "+---+---+---+\n| 1 | 2 | 3 |\n+---+---+---+\n| 4 | 5 | 6 |\n+---+---+---+\n| 7 | 8 | 9 |\n+---+---+---+"

        
    def updateGameBoard(self, move: str, player: str, name: str) -> None:
        """
        Updates the gameboard when a player makes a move, as well as update the local
        variable unlp(user name of the last player to make a move)

        Args:
            move: the player's desired move on the gameboard/grid
            player: Can either be 'player1' 'or player2', use to dictate whether an 'O' or 'X'
                    should be added to the board
            name: name of the last player to make a move

        Returns:
            No value returned.
        """
        if player == 'player2':
            self.gbstring = self.gbstring.replace(move, 'O')
            self.unlp = name
        else:
            self.gbstring = self.gbstring.replace(move, 'X')
            self.unlp = name


    def isWinner(self) -> True or False or None:
        """
        Conditional statements that check the board for a winner,
        indicated by having three X's or O's in a row
        
        Args:
            No args. taken

        Returns:
            True: boolean value
            False: boolean value
        """
        if [self.gbstring[16], self.gbstring[20], self.gbstring[24]] == ['X', 'X', 'X'] or [self.gbstring[16], self.gbstring[20], self.gbstring[24]] == ['O', 'O', 'O']:  
            self.resetGameBoard()
            if self.pun == self.unlp:
                self.wins += 1
                return True
            else:
                self.losses += 1
                return False
        elif [self.gbstring[44], self.gbstring[48], self.gbstring[52]] == ['X', 'X', 'X'] or [self.gbstring[44], self.gbstring[48], self.gbstring[52]] == ['O', 'O', 'O']:  
            self.resetGameBoard()
            if self.pun == self.unlp:
                self.wins += 1
                return True
            else:
                self.losses += 1
                return False
        elif [self.gbstring[72], self.gbstring[76], self.gbstring[80]] == ['X', 'X', 'X'] or [self.gbstring[72], self.gbstring[76], self.gbstring[80]] == ['O', 'O', 'O']:  
            self.resetGameBoard()
            if self.pun == self.unlp:
                self.wins += 1
                return True
            else:
                self.losses += 1
                return False
        elif [self.gbstring[16], self.gbstring[48], self.gbstring[80]] == ['X', 'X', 'X'] or [self.gbstring[16], self.gbstring[48], self.gbstring[80]] == ['O', 'O', 'O']:  
            self.resetGameBoard()
            if self.pun == self.unlp:
                self.wins += 1
                return True
            else:
                self.losses += 1
                return False
        elif[self.gbstring[24], self.gbstring[48], self.gbstring[72]] == ['X', 'X', 'X'] or [self.gbstring[24], self.gbstring[48], self.gbstring[72]] == ['O', 'O', 'O']:  
            self.resetGameBoard()
            if self.pun == self.unlp:
                self.wins += 1
                return True
            else:
                self.losses += 1
                return False
        elif[self.gbstring[16], self.gbstring[44], self.gbstring[72]] == ['X', 'X', 'X'] or [self.gbstring[16], self.gbstring[44], self.gbstring[72]] == ['O', 'O', 'O']:  
            self.resetGameBoard()
            if self.pun == self.unlp:
                self.wins += 1
                return True
            else:
                self.losses += 1
                return False
        elif[self.gbstring[20], self.gbstring[48], self.gbstring[76]] == ['X', 'X', 'X'] or [self.gbstring[20], self.gbstring[48], self.gbstring[76]] == ['O', 'O', 'O']:  
            self.resetGameBoard()
            if self.pun == self.unlp:
                self.wins += 1
                return True
            else:
                self.losses += 1
                return False
        elif[self.gbstring[24], self.gbstring[52], self.gbstring[80]] == ['X', 'X', 'X'] or [self.gbstring[24], self.gbstring[52], self.gbstring[80]] == ['O', 'O', 'O']:  
            self.resetGameBoard()
            if self.pun == self.unlp:
                self.wins += 1
                return True
            else:
                self.losses += 1

                return False
        return None


    def boardIsFull(self) -> True or False:
        """
        Checks to see if the board is full.
            
        Args:
            No args. taken

        Returns:
            True: boolean value
            False: boolean value
        """
        count = 0
        if '1' in self.gbstring:
            count += 1
        if '2' in self.gbstring:
            count += 1
        if '3' in self.gbstring:
            count += 1
        if '4' in self.gbstring:
            count += 1
        if '5' in self.gbstring:
            count += 1
        if '6' in self.gbstring:
            count += 1
        if '7' in self.gbstring:
            count += 1
        if '8' in self.gbstring:
            count += 1
        if '9' in self.gbstring:
            count += 1
        if count == 0:
            self.ties += 1
            self.resetGameBoard()
            return True
        return False

    
    def computeStats(self) -> None:
        """
        Returns the stats of the player
        
        Args:
            No args. taken

        Returns:
            No value returned
        """
        return (self.pun, self.unlp, self.nogp, self.wins, self.losses, self.ties)
        
