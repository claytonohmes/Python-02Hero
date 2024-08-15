#: Define the board
blank = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' ',}
board = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' ',}
Game_on = True
winner = ' '

#function to print out the board
def display_board(board):
    print('\n'*50)
    print(f' {board[7]} | {board[8]} | {board[9]} ')
    print('-----------')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print('-----------')
    print(f' {board[1]} | {board[2]} | {board[3]} ')

#function to get a users input
def get_postion_choice():
    #initial
    choice = 'WRONG'
    acceptablerange = range(1,10)
    within_range = False
    
    #two conditions to check
    while choice.isdigit() == False or within_range == False:
        choice = input("The board follows a numpad. Please select position (1-9): ")
        #digit check
        if choice.isdigit() == False:
            print('what you entered as not a digit.')

        if choice.isdigit() == True:
            if int(choice) in acceptablerange:
                within_range = True
            else:
                print('out of range. Please choose a positon based on your numpad.')
                within_range = False

    return int(choice)

#: Write a fuction to replace the empty sting
def replacement(board,choice):
    replace = 'wrong'
    
    while replace.lower() not in ['x','o']:
        replace = input('Take your turn > ')

        if replace.lower() not in ['x','o']:
            print("Please choose X or O > ")

    board[choice] = replace.upper()
    return board


#: Write a function to check for a winning condition
def check_winning(board):
    for i in range(1,8,3):
        if board[i] == board[i+1] == board[i+2]:
            if board[i] != ' ':
                return board[i]
            else:
                pass
    for i in range(1,4):
        if board[i] == board[i+3] == board[i+6]:
            if board[i] != ' ':
                return board[i]
            else:
                pass
    for i in [1]:
        if board[i] == board[i+4] == board[i+8]:
            if board[i] != ' ':
                return board[i]
            else:
                pass
        elif board[i+2] == board[i+4] == board[i+6]:
            if board[i+2] != ' ':
                return board[i+2]
            else:
                pass

def check_for_space(board):
    return ' ' in board.values()

def game_on_choice():
    choice = 'Wrong'
    while choice.lower() not in ['y','n']:
        choice = input('Keep Playing? (Y,N): ')

        if choice.lower() not in ['y','n']:
            print('sorry, invalid choice!')

    if choice.lower() == 'y':
        return True
    else:
        return False
            
        
#: Write a game on loop
while Game_on and winner == ' ':
    display_board(board)
    choice = get_postion_choice()
    print(choice)
    replacement(board,choice)
    winner = check_winning(board)
    if winner == None:
        winner = ' '

    if winner.lower() in ['x','o']:
        print('You are the winner ' + winner + '!')
        Game_on = game_on_choice()
        if Game_on:
            board = blank
    elif not check_for_space(board):
        print('Game over!')
        Game_on = game_on_choice()
        if Game_on:
            board = blank

print('Thanks for playing!')
