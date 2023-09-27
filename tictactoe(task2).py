import random

# 
Define the Tic-Tac-Toe board
board = [' ' for _ in range(9)]


# Function to display the Tic-Tac-Toe board
def display_board(board):
   
 for row in [board[i:i+3] for i in range(0, 9, 3)]:
       
 print(' | '.join(row))
       
 print('-' * 9)


# Function to check if a player has won

def check_win(board, player):
    
# Check rows, columns, and diagonals
   
 win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                       
 (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        
(0, 4, 8), (2, 4, 6)]
   
 for combo in win_combinations:
        
if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            
return True
    
return False


# Function to check if the board is full (a tie)
def check_tie(board):
   
 return ' ' not in board


# Function to make a player's move
def make_move(board, position, player):
   
 if board[position] == ' ':
       
 board[position] = player


# Function to get all available moves
def get_available_moves(board):
   
 return [i for i, spot in enumerate(board) if spot == ' ']


# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
 
   scores = {
       
 'X': 1,
       
 'O': -1,
       
 'tie': 0
  
  }

   
 if check_win(board, 'X'):
        
return scores['X']
    
if check_win(board, 'O'):
      
  return scores['O']
   
 if check_tie(board):
       
 return scores['tie']

   
 if is_maximizing:
       
 max_eval = float('-inf')
       
 for move in get_available_moves(board):
      
      board[move] = 'X'
           
 eval = minimax(board, depth + 1, False, alpha, beta)
  
          board[move] = ' '
         
   max_eval = max(max_eval, eval)
           
 alpha = max(alpha, eval)
           
 if beta <= alpha:
              
  break
      
  return max_eval
  
  else:
     
   min_eval = float('inf')
    
    for move in get_available_moves(board):
      
      board[move] = 'O'
     
       eval = minimax(board, depth + 1, True, alpha, beta)
       
     board[move] = ' '
         
   min_eval = min(min_eval, eval)
          
  beta = min(beta, eval)
         
   if beta <= alpha:
             
   break
       
 return min_eval


# Function to find the best move for the AI using Minimax with Alpha-Beta Pruning

def find_best_move(board):
    
best_move = -1
    
best_eval = float('-inf')
   
 alpha = float('-inf')
   
 beta = float('inf')

   
 for move in get_available_moves(board):
      
  board[move] = 'X'
     
   eval = minimax(board, 0, False, alpha, beta)
      
  board[move] = ' '
       
 if eval > best_eval:
          
  best_eval = eval
           
 best_move = move

   
 return best_move


# Main game loop
while True:
   
 display_board(board)

   
 # Player's move
    try:
     
   player_move = int(input("Enter your move (0-8): "))
       
 if player_move < 0 or player_move > 8 or board[player_move] != ' ':
   
         print("Invalid move. Try again.")
          
  continue
   
 except ValueError:
      
  print("Invalid input. Enter a number between 0 and 8.")
     
   continue

   
 make_move(board, player_move, 'O')

   
 # Check if the player has won
    if check_win(board, 'O'):
       
 display_board(board)
       
 print("Congratulations! You win!")
       
 break

  
  # Check for a tie
    if check_tie(board):
       
 display_board(board)
      
  print("It's a tie!")
       
 break

   
 # AI's move
  
  ai_move = find_best_move(board)
  
  make_move(board, ai_move, 'X')

    
# Check if the AI has won
   
 if check_win(board, 'X'):
       
 display_board(board)
      
  print("AI wins! You lose.")
       
 break

  
  # Check for a tie
  
  if check_tie(board):
       
 display_board(board)
       
 print("It's a tie!")
      
  break