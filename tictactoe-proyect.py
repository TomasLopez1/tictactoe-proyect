'''
Tic Tac Toe Proyect
By: Tomás lópez 
'''

 
def main():
    player = game_player("")            
    board = generate_board()
    while not (winner(board) or draw(board)):
        show_board(board)
        next_turn(player,board)
        player = game_player(player)
    show_board(board)
    print("Congratulations!")
    print("What a nice game!, You are a really good player")
    print()

def generate_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def show_board(board): 
    print()
    print("=========")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("- + - + -")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("- + - + -")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("=========")

def winner(board):
    return (board[6] == board[7] == board[8] or
            board[3] == board[4] == board[5] or
            board[0] == board[1] == board[2] or
            board[2] == board[5] == board[8] or
            board[1] == board[4] == board[7] or            
            board[0] == board[3] == board[6] or
            board[2] == board[4] == board[6] or
            board[0] == board[4] == board[8])

def draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False 
    return True 

def next_turn(player,board): 
    square = int(input(f"{player}'s turn to choose a square. Please choose a number (1-9): "))
    board[square - 1] = player 

def game_player(choosed):
    if choosed == "" or choosed == "x":
        return "o"
    elif choosed == "o":
        return "x"

if __name__ == "__main__":
    main()


