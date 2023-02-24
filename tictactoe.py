from tkinter import *
import random

def next_turn(row, column): #defining a function to alternate turns between the players of the game.

    global player #getting access to player

    if buttons[row][column]['text'] == "" and check_winner() is False: #checking if buttons are empty, so that can be filled in the game.

        if player == players[0]: #first player as player[0]

            buttons[row][column]['text'] = player #taking input from player[0] for the button.

            if check_winner() is False: #checking if there is a winner after a button has been filled and if not then switches players.
                player = players[1] #switches turn from player[0] to player[1]
                label.config(text=(players[1]+" Turn")) #creating a label to indicate whose turn it is in the game.

            elif check_winner() is True: #checking if there is a winner after a button has been filled
                label.config(text=(players[0]+" Wins :)")) #creating a label to indicate which player won the game.

            elif check_winner() == "Tie": #checking if there is a tie
                label.config(text="It's a Tie :(") #creating a label to display the status of the game.

        else: #if it is not the player[0] turn then it is player[1] turn.

            buttons[row][column]['text'] = player #taking input from player[1] for the button.

            if check_winner() is False: #checking if there is a winner after a button has been filled and if not then switches players.
                player = players[0] #switches turn from player[1] to player[0]
                label.config(text=(players[0]+" Turn")) #creating a label to indicate whose turn it is in the game.

            elif check_winner() is True: #checking if there is a winner after a button has been filled
                label.config(text=(players[1]+" Wins :)")) #creating a label to indicate which player won the game.

            elif check_winner() == "Tie": #checking if there is a tie
                label.config(text="It's a Tie :(") #creating a label to display the status of the game.

def check_winner(): #defining a function to check the winner of the game.

    for row in range(3): #using for loop to check the different win conditions of the game in this case horizontal
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")  #assigning color to the button for the winning combination
            buttons[row][1].config(bg="green")  #assigning color to the button for the winning combination
            buttons[row][2].config(bg="green")  #assigning color to the button for the winning combination
            return True #returns true if any player wins the game.

    for column in range(3): #using for loop to check the different win conditions of the game in this case vertical
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green") #assigning color to the button for the winning combination
            buttons[2][column].config(bg="green") #assigning color to the button for the winning combination
            return True #returns true if any player wins the game.

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "": #using if condition to check the different win conditions of the game in this case diagonal
        buttons[0][0].config(bg="green") #assigning color to the button for the winning combination
        buttons[1][1].config(bg="green") #assigning color to the button for the winning combination
        buttons[2][2].config(bg="green") #assigning color to the button for the winning combination
        return True #returns true if any player wins the game.

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "": #using if condition to check the different win conditions of the game in this case diagonal
        buttons[0][2].config(bg="green") #assigning color to the button for the winning combination
        buttons[1][1].config(bg="green") #assigning color to the button for the winning combination
        buttons[2][0].config(bg="green") #assigning color to the button for the winning combination
        return True #returns true if any player wins the game.

    elif empty_spaces() is False: #checking if there are empty spaces on the board in the game.

        for row in range(3): #
            for column in range(3):
                buttons[row][column].config(bg="yellow") #assigning color to the button for the tie combination
        return "Tie"

    else: #if there is no win or tie
        return False #then it returns False indicating there is no winner of the game.


def empty_spaces(): #defining a function to check if there are empty spaces left on the board in the game.

    spaces = 9 #defining a local variable containg the total number of empty spaces.

    for row in range(3): #checks horizontally for empty spaces
        for column in range(3): #checks vertically for empty spaces
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0: #if there are no empty spaces
        return False #returns False indicating there are empty spaces.
    else:
        return True #returns True indicating there are no empty spaces.

def new_game(): #defining a function to start a new game after the game ends.

    global player #getting access to player

    player = random.choice(players) #allows a random player to start the game

    label.config(text=player+" Turn") #creating a label to indicate whose turn it is in the game.

    for row in range(3): #for rows in this range
        for column in range(3): #for columns in this range
            buttons[row][column].config(text="",bg="#F0F0F0") #setting the color of the buttons background to white.


window = Tk() #creating a window as a board to play the game.
window.title("Tic Tac Toe") #assigning a name to the window for the game.
players = ["X","O"] #defining the players in the game.
player = random.choice(players) #defining a to make a random player begin the game.
buttons = [[0,0,0], #creating a 2D list of buttons named buttons with 3 rows.
           [0,0,0],
           [0,0,0]]

label = Label(text=player + " Turn", font=('consolas',40)) #creating a label to know whose turn it is in the game.
label.pack(side="top") #packing the label and setting the side.

restart_button = Button(text="Restart", font=('consolas',20), command=new_game) #creating a button to restart the game by giving it a command to call our previous function to start a new game.
restart_button.pack(side="top") #packing the button and setting the side.

frame = Frame(window) #creating a frame to hold all the buttons.
frame.pack()

for row in range(3): #creating a nested for loop to assign buttons to each available spot for rows and columns.
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,
                                      command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)

window.mainloop()