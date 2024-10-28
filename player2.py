import tkinter as tk
from tkinter import ttk
import gameboard as gb
import socket


def closingsocket(p1Socket: socket.socket, p1username: str) -> None:
    """
    Depending on if player 1 answers yes or no, this function will either reset the gameboard or print the player's stats.

    Args:
        p1Socket: The socket that connects playeer 1 to the server, player 2
        p1username: Username of player 1

    Returns:
        No value returned.
    """
    response = p1Socket.recv(1024).decode('ascii')
    if response == 'Play Again':
        p2gameboard.updateGamesPlayed()
        p2gameboard.resetGameBoard()
        for i in Frame4.winfo_children():
            i.configure(text='', state='normal')
        firstmove = int(p1Socket.recv(1024).decode('ascii'))
        Frame4.winfo_children()[firstmove].configure(text='X', state='disabled')
        p2gameboard.updateGameBoard(str((firstmove+1)), 'player1', p1username)
        players.set(f"{nameentry.get()}'s turn")
        Frame4.update()
        root.mainloop()
    else:
        pun, unlp, nogp, wins, losses, ties = p2gameboard.computeStats()
        p2Socket.close()
        Frame4.destroy()
        thanks.set(f"Thanks for playing {nameentry.get()}!")
        results.set('Results: ')
        recent.set(f'Most recent player to make a move: {unlp}')
        gamesplayed.set(f'Number of Games Played: {nogp}')
        wins2.set(f'Number of Wins: {wins}')
        losses2.set(f'Number of Losses: {losses}')
        ties2.set(f'Number of Ties: {ties}')
        thankslabel = tk.Label(Frame5, textvariable=thanks).pack()
        resultslabel = tk.Label(Frame5, textvariable=results).pack()
        recentlabel = tk.Label(Frame5, textvariable=recent).pack()
        gamesplayedlabel = tk.Label(Frame5, textvariable=gamesplayed).pack()
        wins2label = tk.Label(Frame5, textvariable=wins2).pack()
        losses2label = tk.Label(Frame5, textvariable=losses2).pack()
        ties2label = tk.Label(Frame5, textvariable=ties2).pack()
        root.mainloop()

        
def disableFrame() -> None:
    """
    Prevents the user from interacting with the gameboard and updates the gameboard.

    Args:
        No args. taken.
        
    Returns:
        No value returned.
    """
    for i in Frame4.winfo_children():
        i.configure(state='disabled')
    Frame4.update()


def enableFrame() -> None:
    """
    Allows the user to interaction with the gameboard and updates the gameboard.

    Args:
        No args. taken.
        
    Returns:
        No value returned.
    """
    for i in Frame4.winfo_children():
        if i.cget('text') == '':
            i.configure(state='normal')
    Frame4.update()

    
def checkgb2(p1Socket: socket.socket, p1username: str) -> None:
    """
    Checks the gameboard to see if there's a winner or a tie.

    Args:
        p1Socket: The socket that connects player 2 to the client, player 1.
        p1username: Username of player 1

    Returns:
        No value returned.
    """
    winorlose = p2gameboard.isWinner()
    if winorlose == True or winorlose == False:
        closingsocket(p1Socket, p1username)
    if p2gameboard.boardIsFull() == True:
        closingsocket(p1Socket, p1username)
    pass

       
def checkgb(p2username, button, p1Socket: socket.socket, p1username) -> None:
    """
    Registers player 1 and 2's moves on the board. Calls the function that checks the gameboard to see if there's a winner or a tie.

    Args:
        p2username: Username of player 2
        button: The button that was pressed by player 2
        p1Socket: The socket that connects player 2 to the client, player 1.
        p1username: Username of player 1
        
    Returns:
        No value returned.
    """
    players.set(f"{p1username}'s turn")
    Frame4.winfo_children()[button].configure(text='O', state='disabled')
    disableFrame()
    p2gameboard.updateGameBoard(str((button+1)), 'player2', p2username)
    p1Socket.send(str(button).encode())
    checkgb2(p1Socket, p1username)
    p1Socket.setblocking(True)
    button = int(p1Socket.recv(1024).decode('ascii'))
    Frame4.winfo_children()[button].configure(text='X', state='disabled')
    Frame4.update() 
    p2gameboard.updateGameBoard(str((button+1)), 'player1', p1username)
    checkgb2(p1Socket, p1username)
    players.set(f"{p2username}'s turn")
    enableFrame()

    
def gbplay(p2username: str, p1Socket: socket.socket, p1username: str, firstmove: int) -> None:
    """
    Creates the gameboard.
            
    Args:
        p2username: Username of player 2
        p1Socket: The socket that connects player 2 to the client, player 1.
        p1username: Username of player 1
        firstmove: Player 1's first move

    Returns:
        No value returned
    """
    box1but = tk.Button(Frame4, text='', width = 10, height = 5, command=lambda: checkgb(p2username, 0, p1Socket, p1username)).grid(row = 1, column = 1)
    box2but = tk.Button(Frame4, text='', width = 10, height = 5, command=lambda: checkgb(p2username, 1, p1Socket, p1username)).grid(row = 1, column = 11)
    box3but = tk.Button(Frame4, text='', width = 10, height = 5, command=lambda: checkgb(p2username, 2, p1Socket, p1username)).grid(row = 1, column = 21)
    box4but = tk.Button(Frame4, text='', width = 10, height = 5, command=lambda: checkgb(p2username, 3, p1Socket, p1username)).grid(row = 3, column = 1)
    box5but = tk.Button(Frame4, text='', width = 10, height = 5, command=lambda: checkgb(p2username, 4, p1Socket, p1username)).grid(row = 3, column = 11)
    box6but = tk.Button(Frame4, text='', width = 10, height = 5, command=lambda: checkgb(p2username, 5, p1Socket, p1username)).grid(row = 3, column = 21)
    box7but = tk.Button(Frame4, text='', width = 10, height = 5, command=lambda: checkgb(p2username, 6, p1Socket, p1username)).grid(row = 5, column = 1)
    box8but = tk.Button(Frame4, text='', width = 10, height = 5, command=lambda: checkgb(p2username, 7, p1Socket, p1username)).grid(row = 5, column = 11)
    box9but = tk.Button(Frame4, text='', width = 10, height = 5, command=lambda: checkgb(p2username, 8, p1Socket, p1username)).grid(row = 5, column = 21)
    makemove.set("Click on a square to place your 'O'")
    makemoveLabel = tk.Label(Frame4, textvariable=makemove).grid(row = 7, column = 11)
    playerslab = tk.Label(Frame4, textvariable = players).grid(row = 8, column = 11)
    Frame4.winfo_children()[firstmove].configure(text='X', state='disabled')
    p2gameboard.updateGameBoard(str((firstmove+1)), 'player1', p1username)
    root.mainloop()


def startgb(p1Socket: socket.socket) -> None:
    """
   Acquires the usernames of player1 and 2, registering them on the gameboard. Calls the function that creates the gameboard.
            
    Args:
        p1Socket: The socket that connects player 2 to the client, player 1.

    Returns:
        No value returned
    """
    p2username = nameentry.get()
    Frame2.destroy()
    Frame2.update()
    p1Socket.send(p2username.encode())
    players.set(f"{p2username}'s turn")
    p1username = p1Socket.recv(1024).decode('ascii')
    p2gameboard.set_name(p2username)
    p2gameboard.set_name2(p1username)
    p2gameboard.updateGamesPlayed()
    firstmove = int(p1Socket.recv(1024).decode('ascii'))
    gbplay(p2username, p1Socket, p1username, firstmove)


def createserver() -> None:
    """
    Asks the user to input the host name of their computer and the port they would like to use via Frame 1 on the root canvas.
    Also asks what username the player would lie.
            
    Args:
        No args. taken.

    Returns:
        No value returned
    """
    serveraddress = host.get()
    finalport = port.get()
    p2Socket.bind((serveraddress, int(finalport)))
    p2Socket.listen(1)
    p1Socket, p1Address = p2Socket.accept()
    Frame1.destroy()
    Frame1.update()
    if True:
        name.set('What would you like your username to be? ')
        namelabel = tk.Label(Frame2, textvariable=name).grid(row = 1, column = 1)
        nameentrylab = tk.Entry(Frame2, textvariable=nameentry).grid(row = 1, column = 3)
        submitButton2 = tk.Button(Frame2, text='Send', command=lambda: startgb(p1Socket)).grid(row = 2, column = 3)
        root.mainloop()
    
    
if __name__ == "__main__":
    """
    The main block. Creates the root window and intiizalies the variables and frames that will be used.
    """
    p2Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    p2gameboard = gb.BoardClass()
    root = tk.Tk()
    Frame1 = tk.Frame(root)
    Frame1.pack()
    Frame2 = tk.Frame(root)
    Frame2.pack()
    Frame4 = tk.Frame(root)
    Frame4.pack()
    Frame5 = tk.Frame(root)
    Frame5.pack()
    root.title("Tic-Tac-Toe") 
    root.geometry('700x500') 
    root.configure(background='grey')
    root.resizable(0,0)
    host = tk.StringVar()
    port = tk.StringVar()
    hostprint = tk.StringVar()
    portprint = tk.StringVar()
    makemove = tk.StringVar()
    players = tk.StringVar()
    name = tk.StringVar()
    nameentry = tk.StringVar()
    thanks = tk.StringVar()
    results = tk.StringVar()
    recent = tk.StringVar()
    gamesplayed = tk.StringVar()
    wins2 = tk.StringVar()
    losses2 = tk.StringVar()
    ties2 = tk.StringVar()
    hostprint.set("Please input the host name/IP address of your machine.")
    hostprintLabel = tk.Label(Frame1, textvariable=hostprint).grid(row = 1, column = 1)
    hostbut = tk.Entry(Frame1, textvariable=host).grid(row = 1, column = 3)
    portprint.set("Please input the specific port you would like to use: ")
    portprintLabel = tk.Label(Frame1, textvariable=portprint).grid(row = 2, column = 1)
    portbut = tk.Entry(Frame1, textvariable=port).grid(row = 2, column = 3)
    submitButton = tk.Button(Frame1, text='Submit', command=createserver).grid(row = 3, column = 3)
    root.mainloop()
