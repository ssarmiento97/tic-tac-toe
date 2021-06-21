game_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def display_board(current_board):
    print(f' {current_board[6]} | {current_board[7]} | {current_board[8]} ')
    print('------------')
    print(f' {current_board[3]} | {current_board[4]} | {current_board[5]} ')
    print('------------')
    print(f' {current_board[0]} | {current_board[1]} | {current_board[2]} ')

display_board(game_board)