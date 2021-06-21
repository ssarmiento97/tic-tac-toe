game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
current_player = 1
game_state = "Play"


def display_board(current_board):
    print(f' {current_board[6]} | {current_board[7]} | {current_board[8]} ')
    print('------------')
    print(f' {current_board[3]} | {current_board[4]} | {current_board[5]} ')
    print('------------')
    print(f' {current_board[0]} | {current_board[1]} | {current_board[2]} ')

def play_on():

    user_choice = 'c'

    # ask the user if they would like to play again
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
    acceptable_range = [1,2,3,4,5,6,7,8,9]
    in_range = False

    if player % 2 == 1:
        while not selection.isdigit() or in_range:
            selection = input("Player 1 please select where you would like to place your 'X' (1-9): ")

            if not selection.isdigit():
                print("Please enter a number between 1-9!")
            elif int(selection) in acceptable_range:
                in_range = True
        
        current_board[selection - 1] = 'X'
    else:
        while not selection.isdigit() or in_range:
            selection = input("Player 2 please select where you would like to place your 'O' (1-9): ")

            if not selection.isdigit():
                print("Please enter a number between 1-9!")
            elif int(selection) in acceptable_range:
                    in_range = True

        current_board[selection - 1] = 'O'

    return current_board
    
def check_board(current_board):
    # check if anyone has won
    if current_board[0] == current_board[1] == current_board[2]:
        return current_board[0]
    elif current_board[3] == current_board[4] == current_board[5]:
        return current_board[3]
    elif current_board[6] == current_board[7] == current_board[8]:
        return current_board[6]
    elif current_board[0] == current_board[4] == current_board[8]:
        return current_board[0]
    elif current_board[2] == current_board[4] == current_board[6]:
        return current_board[2]
    else:
        # verify if there are any moves left
        for move in current_board:
            if move == ' ':
                return 'Play'
        return 'Draw'



print("The board will be numbered as follows:")
display_board(['1', '2', '3 ', '4', '5', '6', '7', '8', '9'])
print('Player 1 = X | Player 2 = O')
input("Welcome players. Press ENTER to start game.")
print('\n'*5)

while True:
    print("Current Board: ")
    display_board(game_board)
    game_board = get_input(current_player, game_board)
    current_player += 1
    game_state = check_board(game_board)

    if game_state == "Play":
        continue
    elif game_state == "Draw":
        print("It looks like this one's a draw!")
        if play_on():
            game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            current_player = 1
            game_state = "Play"
            print('\n'*5)
        else:
            break
    elif game_state == "X":
        print("Congratulations Player 1! You are the winner!")
        if play_on():
            game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            current_player = 1
            game_state = "Play"
            print('\n'*5)
        else:
            break
    elif game_state == "O":
        print("Congratulations Player 2! You are the winner!")
        if play_on():
            game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            current_player = 1
            game_state = "Play"
            print('\n'*5)
        else:
            break
    else:
        print(f"Error. Invalid game_state: {game_state}")
        break
