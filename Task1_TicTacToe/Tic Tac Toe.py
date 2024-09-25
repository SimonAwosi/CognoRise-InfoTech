import math

# Create an empty Tic Tac Toe board
board = [' ' for _ in range(9)]  # A 3x3 board represented as a list

# Function to display the Tic Tac Toe board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")  # Enclosed in quotation marks
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")  # Enclosed in quotation marks
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if a player has won
def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                      (0, 4, 8), (2, 4, 6)]  # diagonals
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

# Function to check if the board is full (i.e., a draw)
def check_draw(board):
    return ' ' not in board

# Minimax algorithm to choose the best move for AI
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    elif check_winner(board, 'X'):
        return -1
    elif check_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# Function for the AI to make its move
def ai_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'

# Main game loop for human vs AI
def play_game():
    current_player = 'X'  # Player X always starts
    game_over = False

    while not game_over:
        print_board(board)

        if current_player == 'X':  # Human move
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = 'X'
                if check_winner(board, 'X'):
                    print_board(board)
                    print("You win!")
                    game_over = True
                elif check_draw(board):
                    print_board(board)
                    print("It's a draw!")
                    game_over = True
                else:
                    current_player = 'O'
            else:
                print("Invalid move. Try again.")
        else:  # AI move
            print("AI is making a move...")
            ai_move()
            if check_winner(board, 'O'):
                print_board(board)
                print("AI wins!")
                game_over = True
            elif check_draw(board):
                print_board(board)
                print("It's a draw!")
                game_over = True
            else:
                current_player = 'X'

# Run the game
if __name__ == "__main__":
    play_game()
