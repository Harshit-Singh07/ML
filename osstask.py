

def createboard():
    return [' ' for _ in range(9)]

def print_board(board):
    print('-----------------------------------')
    print(f'| {board[0]} | {board[1]} | {board[2]} |')
    print('-----------------------------------')
    print(f'| {board[3]} | {board[4]} | {board[5]} |')
    print('-----------------------------------')
    print(f'| {board[6]} | {board[7]} | {board[8]} |')
    print('-----------------------------------')

def check(board,player):
    win_condition=[
        [0,1,2],[3,4,5],[6,7,8], #rows
        [0,3,6],[1,4,7],[2,5,8], #columns
        [0,4,8],[2,4,6] #diagonals
    ]
    for con in win_condition:
        if all(board[i]==player for i in con):
            return True
        return False
    
def check_draw(board):
    return ' ' not in board


def gmove(player):
    while True:
        try:
            move = int(input(f"Player '{player}', enter your move (1-9): "))
            if 1 <= move <= 9:
                return move - 1
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def is_valid_move(board, move):
    
    return board[move] == ' '
def play_game():
    
    board = createboard()
    player = 'X'
    print("Welcome to Tic-Tac-Toe!")
    while True:
        print_board(board)
        move = gmove(player)
        if not is_valid_move(board, move):
            print("This space is already taken. Please choose another spot.")
            continue
        board[move] = player
        if check(board, player):
            print_board(board)
            print(f"Congratulations! Player '{player}' wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        player = 'O' if player == 'X' else 'X'

if __name__ == '__main__':
    play_game()
