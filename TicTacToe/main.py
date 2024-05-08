"""
Purpose: The purpose of TicTacToe.py(PerformanceTaskDay4.py) is to use PG Zero to create the classic TicTacToe game. It uses various algorythms and modules needed to create a interactive game where it registers clicks to fill squares on the gameboard in hopes to get 3 in a row to ultimately beat the opponent. The main purpose of creating the code is for the final performance task but can also be used for leisure purposes  

Author: Saubaan Hasan
Creation Date: 15/06/2021
"""

#Imports the PG Zero module.
import pgzrun

#Sets the dimentions of the game window.
B_WIDTH = 300
HEIGHT = 310
WIDTH = 350

#Identifies the color code for white under the variable name WHITE.
WHITE = (255, 255, 255)

#Holds the collumn and row value of an inputted position.
clickedSquare = [-1, -1]

#Holds the value for the current players turn (defaulted to start with x).
turn = "x"

#Holds the x and o values for every square on the grid 
board = ["","","","","","","","",""]

#variables to contain all the end outcomes (P1 win, P2 win and tie).
winnerP1 = 0
winnerP2 = 0
tie = 0

#Variables to contain the status of each box on the board.
boxFilled1 = 0
boxFilled2 = 0
boxFilled3 = 0
boxFilled4 = 0
boxFilled5 = 0
boxFilled6 = 0
boxFilled7 = 0
boxFilled8 = 0
boxFilled9 = 0

# This function deals with all the drawing to the game screen.
def draw():
    #Clears the screen and draws lines in the format of the typical tictactoe grid. 
    screen.clear()
    screen.draw.line((0, HEIGHT/3), (B_WIDTH, HEIGHT/3), WHITE)
    screen.draw.line((0, 2*HEIGHT/3), (B_WIDTH, 2*HEIGHT/3), WHITE)
    screen.draw.line((B_WIDTH/3, 0), (B_WIDTH/3, HEIGHT), WHITE)
    screen.draw.line((2*B_WIDTH/3, 0), (2*B_WIDTH/3, HEIGHT), WHITE)

    #Takes the value in turn to display a symbol of the current turn on the sideboard.
    screen.draw.text(turn, (B_WIDTH+20,HEIGHT/2-15), color="orange", fontsize=50)
    
    #Uses the values from board and pos to identify where there x and o markers need to be as well as what their color is.
    pos = 0
    for cell in board:
        #Uses an algorythm to pinpoint an x and y location to print the respective marker. 
        xPos = 40 + pos % 300
        yPos = 30 + (pos // 300) * 100

        #Checks for the value inside the index of the list to assign the respective color.
        if cell == "x":
            c = "red"
        else:
            c = "blue"
        # Takes the cell value (x or o), the (x,y) coordinates and the marker color from above to display the marker on the grid square clicked.
        screen.draw.text(cell, (xPos,yPos), color=c, fontsize=50)
        pos += 100
    
    #Displays the end game message by the outcome of the game.
    if winnerP1 == 1:
      screen.draw.text("Player 1 Wins!", (105,145), color="yellow", fontsize=20) #Displays P1 Win
    if winnerP2 == 1:
      screen.draw.text("Player 2 Wins!", (105,145), color="yellow", fontsize=20) #Displays P2 Win
    if tie == 1:
      screen.draw.text("Its a Tie!", (125,140), color="yellow", fontsize=20) #Displays tie game

#Processes the turn by using the value inside the board after each registered click. 
def processTurn(r, c):
    #Calls all necessary variables needed in the function.
    global turn
    i = r * 3 + c
    if board[i] == "":
        board[i] = turn
        
        if turn == "x":
            turn = "o"
        else:
            turn = "x"   

#Constantly updates to clear info no longer needed within variables and to check the status for the game result.
def update():
    #Calls all necessary variables needed in the function
    global clickedSquare, board, winnerP1, winnerP2, boxFilled1, boxFilled2, boxFilled3, boxFilled4, boxFilled5, boxFilled6, boxFilled7, boxFilled8, boxFilled9, tie

    #Constantly refreshes to see if any row/column values have been added to clickedSquare.
    if clickedSquare[0] < 0 or clickedSquare[1] < 0:
        return
    
    #Inputs the coordinate points on the game grid to the processTurn procedure to determine the next turn.
    processTurn(clickedSquare[0], clickedSquare[1])

    #Resets the holder for the coordinates so new points can be implemented without any issues.
    clickedSquare = [-1, -1]

    #Checks for all possible win combinations for Player 1
    if board[0] == "x" and board[1] == "x" and board[2] == "x":
      winnerP1 = 1
    if board[3] == "x" and board[4] == "x" and board[5] == "x":
      winnerP1 = 1
    if board[6] == "x" and board[7] == "x" and board[8] == "x":
      winnerP1 = 1
    if board[0] == "x" and board[3] == "x" and board[6] == "x":
      winnerP1 = 1
    if board[1] == "x" and board[4] == "x" and board[7] == "x":
      winnerP1 = 1
    if board[2] == "x" and board[5] == "x" and board[8] == "x":
      winnerP1 = 1
    if board[0] == "x" and board[4] == "x" and board[8] == "x":
      winnerP1 = 1
    if board[2] == "x" and board[4] == "x" and board[6] == "x":
      winnerP1 = 1

    #Checks for all possible win combinations for Player 2.
    if board[0] == "o" and board[1] == "o" and board[2] == "o":
      winnerP2 = 1
    if board[3] == "o" and board[4] == "o" and board[5] == "o":
      winnerP2 = 1
    if board[6] == "o" and board[7] == "o" and board[8] == "o":
      winnerP2 = 1
    if board[0] == "o" and board[3] == "o" and board[6] == "o":
      winnerP2 = 1
    if board[1] == "o" and board[4] == "o" and board[7] == "o":
      winnerP2 = 1
    if board[2] == "o" and board[5] == "o" and board[8] == "o":
      winnerP2 = 1
    if board[0] == "o" and board[4] == "o" and board[8] == "o":
      winnerP2 = 1
    if board[2] == "o" and board[4] == "o" and board[6] == "o":
      winnerP2 = 1
    
    #Checks and marks the grid pieces that are filled.
    if board[0] == "x" or board[0] == "o":
      boxFilled1 = 1
    if board[1] == "x" or board[1] == "o":
      boxFilled2 = 1
    if board[2] == "x" or board[2] == "o":
      boxFilled3 = 1
    if board[3] == "x" or board[3] == "o":
      boxFilled4 = 1
    if board[4] == "x" or board[4] == "o":
      boxFilled5 = 1
    if board[5] == "x" or board[5] == "o":
      boxFilled6 = 1
    if board[6] == "x" or board[6] == "o":
      boxFilled7 = 1
    if board[7] == "x" or board[7] == "o":
      boxFilled8 = 1
    if board[8] == "x" or board[8] == "o":
      boxFilled9 = 1

    #Checks if all grids are filled with no winner to set it as a tie game.
    if boxFilled1 == 1 and boxFilled2 == 1 and boxFilled3 == 1 and boxFilled4 == 1 and boxFilled5 == 1 and boxFilled6 == 1 and boxFilled7 == 1 and boxFilled8 == 1 and boxFilled9 == 1 and winnerP1 == 0 and winnerP2 == 0:
      tie = 1


    

#Handles the logistics of a click in a given section of the board to then translate it as a specific button pressed.
def on_mouse_up(pos, button): 
    #Calls all necessary variables needed in the function
    global clickedSquare, rct, winnerP1, winnerP2

    # Checks if there is an outcome to run the code, causing the game to be unresponsive when the game has ended.
    if winnerP1 == 0 and winnerP2 == 0 and tie == 0:

      #Uses the width values of the board to divide it into 3 equal columns. Using that, it assigns a column value (0, 1, 2).
      if pos[0] < B_WIDTH/3:
          c = 0
      elif pos[0] < 2*B_WIDTH/3:
          c = 1
      else:
          c = 2

      #Uses the height values of the board to divide it into 3 equal rows. Using that, it assigns a row value (0, 1, 2).
      if pos[1] < HEIGHT/3:
          r = 0
      elif pos[1] < 2*HEIGHT/3:
          r = 1
      else:
          r = 2

      #Returns the row and column values to the clickedSquare holder.
      clickedSquare = [r, c]

pgzrun.go()