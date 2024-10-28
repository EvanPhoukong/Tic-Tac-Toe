import tkinter as tk
from tkinter import ttk
import gameboard as gb
import socket


def closingsocket(p2username: str, playagain: str, p1Socket: socket.socket, Frame6: tk.Frame, p1username: str) -> None:
    """
    Depending on if the player answers yes or no, this function will either reset the gameboard or print the player's stats.

    Args:
        p2username: Username of player 2
        playagain: A string that determines if a rematch will ensue or not.
        p1Socket: The socket that connects playeer 1 to the server, player 2
        Frame6: The frame encompassing widgets that asks the user if they wanted a rematch.
        p1username: Username of player 1

    Returns:
        No value returned.
    """
    if playagain == 'Y':
        p1gameboard.resetGameBoard()
        Frame6.destroy()
        p1Socket.send(b'Play Again')
        p1gameboard.updateGamesPlayed()
        gbplay(p2username, p1username, p1Socket)
    elif playagain == 'N':
        p1Socket.send(b'Fun Times')
        p1Socket.close()
        pun, unlp, nogp, wins, losses, ties = p1gameboard.computeStats()
        Frame6.destroy()
        thanks.set(f"Thanks for playing {pun}!")
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


def disableFrame(Frame4: tk.Frame) -> None:
    """
    Prevents the user from interacting with the gameboard and updates the gameboard.

    Args:
        Frame4: The gameboard
        
    Returns:
        No value returned.
    """
    for i in Frame4.winfo_children():
        i.configure(state='disabled')
    Frame4.update()


def enableFrame(Frame4: tk.Frame) -> None:
    """
    Allows the user to interaction with the gameboard and updates the gameboard.

    Args:
        Frame4: The gameboard
        
    Returns:
        No value returned.
    """
    for i in Frame4.winfo_children():
        if i.cget('text') == '':
            i.configure(state='normal')
    Frame4.update()

    
def checkgb2(p2username: str, p1Socket: socket.socket, Frame4: tk.Frame, p1username: str) -> None:
    """
    Checks the gameboard to see if there's a winner or a tie, as well as asks the user if they would like to rematch.

    Args:
        p2username: Username of player 2
        p1Socket: The socket that connects playeer 1 to the server, player 2
        Frame4: The gameboard
        p1username: Username of player 1
        
    Returns:
        No value returned.
    """
    winorlose = p1gameboard.isWinner()
    if winorlose == True:
        Frame4.destroy()
        Frame6 = tk.Frame(root)
        Frame6.pack()
        rematch.set('You win! Would you like to rematch? (Y/N)')
        rematchlabel = tk.Label(Frame6, textvariable=rematch).pack()
        yesnolabel = tk.Entry(Frame6, textvariable=yesno).pack()
        submitButton7 = tk.Button(Frame6, text='Submit', command=lambda: closingsocket(p2username, yesno.get().upper(), p1Socket, Frame6, p1username)).pack()
        root.mainloop()
    elif winorlose == False:
        Frame4.destroy()
        Frame6 = tk.Frame(root)
        Frame6.pack()
        rematch.set('You lose. Would you like to rematch? (Y/N)')
        rematchlabel = tk.Label(Frame6, textvariable=rematch).pack()
        yesnolabel = tk.Entry(Frame6, textvariable=yesno).pack()
        submitButton7 = tk.Button(Frame6, text='Submit', command=lambda: closingsocket(p2username, yesno.get().upper(), p1Socket, Frame6, p1username)).pack()
        root.mainloop()
    else:
        pass
    if p1gameboard.boardIsFull() == True:
        Frame4.destroy()
        Frame6 = tk.Frame(root)
        Frame6.pack()
        rematch.set('You tied! Would you like to rematch? (Y/N)')
        rematchlabel = tk.Label(Frame6, textvariable=rematch).pack()
        yesnolabel = tk.Entry(Frame6, textvariable=yesno).pack()
        submitButton7 = tk.Button(Frame6, text='Submit', command=lambda: closingsocket(p2username, yesno.get().upper(), p1Socket, Frame6, p1username)).pack()
        root.mainloop()
    pass


def checkgb(p2username: str, button: int, p1Socket: socket.socket, p1username: str, Frame4: tk.Frame) -> None:
    """
    Registers player 1 and 2's moves on the board. Calls the function that checks the gameboard to see if there's a winner or a tie.

    Args:
        p2username: Username of player 2
        button: The button that was pressed by player 1
        p1Socket: The socket that connects playeer 1 to the server, player 2
        p1username: Username of player 1
        Frame4: The gameboard
        
    Returns:
        No value returned.
    """
    players.set(f"{p2username}'s turn")   
    Frame4.winfo_children()[button].configure(text='X', state='disabled')
    disableFrame(Frame4)
    p1gameboard.updateGameBoard(str((button+1)), 'player1', p1username)
    p1Socket.send((str(button)).encode())
    checkgb2(p2username, p1Socket, Frame4, p1username)
    p1Socket.setblocking(True)
    button = int(p1Socket.recv(1024).decode('ascii'))
    Frame4.winfo_children()[button].configure(text='O', state='disabled')
    Frame4.update() 
    p1gameboard.updateGameBoard(str((button+1)), 'player2', p2username)
    checkgb2(p2username, p1Socket, Frame4, p1username)
    players.set(f"{p1username}'s turn")  
    enableFrame(Frame4)

    
def gbplay(p2username:str, p1username: str, p1Socket: socket.socket) -> None:
    """
    Asks the user to input host name and port via Frame 1 on the root canvas.
            
    Args:
        p2username: Username of player 2
        p1username: Username of player 1
        p1Socket: The socket that connects playeer 1 to the server, player 2

    Returns:
        No value returned
    """
    Frame4 = tk.Frame(root)
    Frame4.pack()
    box1but = tk.Button(Frame4, text='', width = 10, height = 5, command=lambda: checkgb(p2username, 0, p1Socket, p1username, Frame4)).grid(row = 1, column = 1)
    box2but = tk.Button(Frame4, text='', width = 10, height = 5, command=lambda: checkgb(p2username, 1, p1Socket, p1username, Frame4)).grid(row = 1, column = 11)
    box3but = tk.Button(Frame4, text='', width = 10, height = 5, command=lambda: checkgb(p2username, 2, p1Socket, p1username, Frame4)).grid(row = 1, column = 21)
    box4but = tk.Button(Frame4, text='', width = 10, height = 5, command=lambda: checkgb(p2username, 3, p1Socket, p1username, Frame4)).grid(row = 3, column = 1)
    box5but = tk.Button(Frame4, text='', width = 10, height = 5, command=lambda: checkgb(p2username, 4, p1Socket, p1username, Frame4)).grid(row = 3, column = 11)
    box6but = tk.Button(Frame4, text='', width = 10, height = 5, command=lambda: checkgb(p2username, 5, p1Socket, p1username, Frame4)).grid(row = 3, column = 21)
    box7but = tk.Button(Frame4, text='', width = 10, height = 5, command=lambda: checkgb(p2username, 6, p1Socket, p1username, Frame4)).grid(row = 5, column = 1)
    box8but = tk.Button(Frame4, text='', width = 10, height = 5, command=lambda: checkgb(p2username, 7, p1Socket, p1username, Frame4)).grid(row = 5, column = 11)
    box9but = tk.Button(Frame4, text='', width = 10, height = 5, command=lambda: checkgb(p2username, 8, p1Socket, p1username, Frame4)).grid(row = 5, column = 21)
    makemove.set("Click on a square to place your 'X'")
    makemoveLabel = tk.Label(Frame4, textvariable=makemove).grid(row = 7, column = 11)
    players.set(f"{p1username}'s turn")
    playerslab = tk.Label(Frame4, textvariable=players).grid(row = 8, column = 11)
    root.mainloop()

    
def yesorno() -> None:
    """
    Check if user wanted to try and reconnect or simply end the program.
            
    Args:
        No args. taken.

    Returns:
        No value returned
    """
    if tryagainentry.get() == 'y' or tryagainentry.get() == 'Y':
        for i in Frame2.winfo_children():
            i.configure(state='disabled')
        Frame1call()
    elif tryagainentry.get() == 'n' or tryagainentry.get() == 'N':
        root.destroy()
        exit()
    pass


def sendingname(p1Socket: socket.socket) -> None:
    """
    Acquires the usernames of player1 and 2, registering them on the gameboard. Calls the function that creates the gameboard.
            
    Args:
        p1Socket: The socket that connects player 1 to the server, player 2.

    Returns:
        No value returned
    """
    p1username = name.get()
    p1gameboard.set_name(p1username)
    p1Socket.send(p1username.encode())
    Frame3.destroy()
    p1gameboard.set_name(p1username)
    p1gameboard.updateGamesPlayed()
    p2username = p1Socket.recv(1024).decode('ascii')
    p1gameboard.set_name2(p2username)
    gbplay(p2username, p1username, p1Socket)

    
def createserver() -> None:
    """
    Attemps to create the server.
            
    Args:
        No args. taken.

    Returns:
        No value returned
    """
    try:
        serveraddress = host.get()
        finalport = int(port.get())
        p1Socket.connect((serveraddress, finalport))
        Frame1.destroy()
        Frame2.destroy()
        choosename.set('What would you like your username to be? ')
        namelabel = tk.Label(Frame3, textvariable=choosename).grid(row = 1, column = 1)
        nameentry = tk.Entry(Frame3, textvariable=name).grid(row = 1, column = 3)
        submitButton2 = tk.Button(Frame3, text='Send', command=lambda: sendingname(p1Socket)).grid(row = 2, column = 3)
        root.mainloop()
        
    except:
        for i in Frame1.winfo_children():
            i.configure(state='disabled')
        tryagain.set('Host could not be connected to. Would you like to try again? Enter "y" for yes and "n" for no: ')
        tryagainlabel = tk.Label(Frame2, textvariable=tryagain).grid(row = 1, column = 1)
        tryagainentryfield = tk.Entry(Frame2, textvariable=tryagainentry).grid(row = 1, column = 3)
        submitButton2 = tk.Button(Frame2, text='Submit', command=yesorno).grid(row = 2, column = 3)
        root.mainloop()


def Frame1call() -> None:
    """
    Asks the user to input host name and port via Frame 1 on the root canvas.
            
    Args:
        No args. taken.

    Returns:
        No value returned
    """
    hostprint.set("Please input the host name/IP address of the person you would like to play with: ")
    hostprintLabel = tk.Label(Frame1, textvariable=hostprint).grid(row = 1, column = 1)
    hostbut = tk.Entry(Frame1, textvariable=host).grid(row = 1, column = 3)
    portprint.set("Please input the specific port you would like to connect to: ")
    portprintLabel = tk.Label(Frame1, textvariable=portprint).grid(row = 2, column = 1)
    portbut = tk.Entry(Frame1, textvariable=port).grid(row = 2, column = 3)
    submitButton = tk.Button(Frame1, text='Submit', command=createserver).grid(row = 3, column = 3)
    root.mainloop()

    
if __name__ == "__main__":
    """
    The main block. Creates the root window and intiizalies the variables and frames that will be used.
    """
    p1gameboard = gb.BoardClass()
    root = tk.Tk()
    Frame1 = tk.Frame(root)
    Frame2 = tk.Frame(root)
    Frame3 = tk.Frame(root)
    Frame5 = tk.Frame(root)
    Frame1.pack()
    Frame2.pack()
    Frame3.pack()
    Frame5.pack()
    root.title("Tic-Tac-Toe") 
    root.geometry('700x500') 
    root.configure(background='grey')
    root.resizable(0,0)
    host = tk.StringVar()
    port = tk.StringVar()
    hostprint = tk.StringVar()
    portprint = tk.StringVar()
    tryagain = tk.StringVar()
    tryagainentry = tk.StringVar()
    choosename = tk.StringVar()
    name = tk.StringVar()
    makemove = tk.StringVar()
    rematch = tk.StringVar()
    yesno = tk.StringVar()
    players = tk.StringVar()
    thanks = tk.StringVar()
    results = tk.StringVar()
    recent = tk.StringVar()
    gamesplayed = tk.StringVar()
    wins2 = tk.StringVar()
    losses2 = tk.StringVar()
    ties2 = tk.StringVar()
    p1Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Frame1call()
    root.mainloop()
