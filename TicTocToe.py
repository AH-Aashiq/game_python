import random
from colorama import Fore

print(Fore.GREEN + ''' 
   Alachi Presents
--------------''' + Fore.CYAN + '''  
      =================================================
=        ==========        =============        =============
====  ================  ===================  ================
====  ================  ===================  ================
====  ====  ==   =====  =====   ===   =====  =====   ===   ==
====  =======  =  ====  ====     =  =  ====  ====     =  =  =
====  ====  =  =======  ====  =  =  =======  ====  =  =     =
====  ====  =  =======  ====  =  =  =======  ====  =  =  ====
====  ====  =  =  ====  ====  =  =  =  ====  ====  =  =  =  =
====  ====  ==   =====  =====   ===   =====  =====   ===   ==
=============================================================
                                                                 ''' + Fore.WHITE + '''Customize by Alachi
        ''')
print("")
#Step 1: Write a function that can print out a board.Set up your board as a list, where each index 1-9 conroosponds with number pad,so you get a 3 by 3 board representation.
def display_board(board):
    
#     clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

# board = ['anythings','x','x','x','o','o','o','x','x','x']
# display_board(board)


#step 2: write a function that can take a player input and assing their makrker as "X" or "O". Think about using while loops to continually ask until you get a correct ansawer.

def player_input():

     marker = ' '
     while not (marker == 'O' or marker == 'X'):
          marker = input(Fore.RED+'Player 1: Do you want to be x or o?').upper()

          if marker == 'X':
               return ('X','O')
          else:
               return ('O','X')
# print(player_input())

#Step 3: write a function that can takees , In the board list objects, a makrer ("X or "0 ), and a desired postion (number 1-9) and assigns it to the board.

def place_marker(board,marker,position):

    board[position] = marker



#Step 4: Write a function that takes in a board and mark (X or O) and then cehck to see if thar mark has won

def win_check(board,mark):

     return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top 
     (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
     (board[7] == mark and board[8] == mark and board[9] == mark) or # across the bottom
     (board[7] == mark and board[4] == mark and board[1] == mark) or # down themarkft side
     (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
     (board[9] == mark and board[6] == mark and board[3] == mark) or #down the right side
     (board[7] == mark and board[5] == mark and board[3] == mark) or #diagonal
     (board[9] == mark and board[5] == mark and board[1] == mark)) #diagonal


#Step 5: Write a fucntion that uses the random module to randomly decide wich player goes first.You may want to lookup random.randint(),Return a string of which palyer went first.

def choose_first():
     if random.randint(0,1) == 0:
          return 'Player 1'
     else:
         return 'Player 2'

# print(choose_first())

#Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.

def space_check(board,position):
     return board[position] == ' '

#Step 7: Write a function that checks if the board is full and returns boolean value . True if full, False otherwise.

def full_board_check(board):
     for i in range (1,10):
          if space_check(board,i):
               return False
     return True

#Step 8: Write a function that ask for a player's  next postion (as a number 1-9) and then uses the function from step 6 to check if is is a free postion. if it is, then return the position for later use.

def player_choice(board):

     position = ' '

     while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
          position = input(Fore.RED+'Choose your next position: (1-9) ')
     return int(position)

#Step 9: Write a fucntion that ask the palyer if they want to palye again and return a boolean . True if they do want to play again.

def replay():

     return input(Fore.WHITE+'Do your want to play again?Enter Yes or NO').lower().startswith('y')

#Step 10: Here comes the hard part! Use while loops and the function you're made to run the game!

print('Welcome to Tic Tac Toe!!')

while True:
     #set the game up here 
     theBoard = [' ']*10
     player1_marker, player2_marker = player_input()

     turn = choose_first()
     print (turn + 'Will go first!')

     game_on = True

     while game_on:
          if turn == "Player 1":
               display_board(theBoard)
               position = player_choice(theBoard)
               place_marker(theBoard,player1_marker,position)

               if win_check(theBoard,player1_marker):
                    display_board(theBoard)
                    print(Fore.YELLOW+'Congratulations! Player 1 has won the game!!')

                    game_on = False
               
               else:
                    if full_board_check(theBoard):
                         display_board(theBoard)
                         print('The is a draw!!')

                         break
                    else:
                         turn = 'Player 2'

          else:
               #player 2 turns
               display_board(theBoard)
               position = player_choice(theBoard)
               place_marker(theBoard,player2_marker,position)

               if win_check(theBoard,player2_marker):
                    display_board(theBoard)
                    print('Congratulations! Player 2 has won the game!!')

                    game_on = False
               
               else:
                    if full_board_check(theBoard):
                         display_board(theBoard)
                         print('The is a draw!!')

                         break
                    else:
                         turn = 'Player 1'

     if not replay():
          break
