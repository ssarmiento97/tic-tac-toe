game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
keep_playing = True

input("Welcome players. Press ENTER to start game.")

while keep_playing:
    display_board(game_board)


    

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
