game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
keep_playing = True
current_player = 1

print("The board will be numbered as follows:")
display_board(['1', '2', '3 ', '4', '5', '6', '7', '8', '9'])
input("Welcome players. Press ENTER to start game.")
print('\n'*5)

while keep_playing:

    print('Player 1 = X | Player 2 = O')
    display_board(game_board)
    game_board = get_input(current_player, game_board)

    break


    

def display_board(current_board):
    print(f' {current_board[6]} | {current_board[7]} | {current_board[8]} ')
    print('------------')
    print(f' {current_board[3]} | {current_board[4]} | {current_board[5]} ')
    print('------------')
    print(f' {current_board[0]} | {current_board[1]} | {current_board[2]} ')

def play_on():
    # ask the user if they would like to play again

    user_choice = 'c'

    # make sure user is selecting a valid option
    while user_choice not in ['Y', 'N']:
        user_choice = input("Would you like to play again? (Y/N): ").upper()

        if user_choice not in ['Y', 'N']:
            print("Invalid choice. Please input Y or N.")

    if user_choice == 'Y':
        return True
    else:
        return False

def get_input(player, current_board):
    selection = "Invalid"
    acceptable_range = range(1, 10)

    if player % 2 == 1:
        while not selection.isdigit() and selection not in acceptable_range:
            selection = input("Player 1 please select where you would like to place your 'X' (1-9): ")