import random

def tic_toe_game():

    moves_dictionary = {
    "tl" : " ",
    "tm" : " ",
    "tr" : " ",
    "ml" : " ",
    "mm" : " ",
    "mr" : " ",
    "bl" : " ",
    "bm" : " ",
    "br" : " "
    }
    game_on = True

    def board():
        tl = moves_dictionary["tl"]
        tm = moves_dictionary["tm"]
        tr = moves_dictionary["tr"]
        ml = moves_dictionary["ml"]
        mm = moves_dictionary["mm"]
        mr = moves_dictionary["mr"]
        bl = moves_dictionary["bl"]
        bm = moves_dictionary["bm"]
        br = moves_dictionary["br"]
        return F" {tl} | {tm} | {tr} \n-----------\n {ml} | {mm} | {mr} \n-----------\n {bl} | {bm} | {br} "

    def start_game():
        looping = True

        while looping:
            user_input = input("Would you like to be X or O \n")
            user_input = user_input.upper()
            if user_input != "X" and user_input != "O":
                print("Please make a valid selection: X or O")
            else:
                looping = False
                return user_input

    def user_move(user_choice):
        moves_list = ["tl", "tm", "tr", "ml", "mm", "mr", "bl", "bm", "br"]
        print("Top left = tl, Top middle = tm, Top right = tr   Middle left = ml, Middle middle = mm, Middle right = mr   Bottom left = bl, Bottom middle = bm, Bottom right = br")
        move_choice = input("Please select from the following options where you'd like to move. \n"
                            "tl,tm,tr,ml,mm,mr,bl,bm,br\n")
        move_choice = move_choice.lower()
        if move_choice not in moves_list:
            print(board())
            user_move(user_choice)
        elif moves_dictionary[move_choice] == "X" or moves_dictionary[move_choice] == "O":
            print(board())
            user_move(user_choice)
        else:
            moves_dictionary[move_choice] = user_choice
            print(board())

    def computer_move(comp_choice):
        game_on = False

        moves_list = ["tl","tm","tr","ml","mm","mr","bl","bm","br"]
        random_number = random.randint(0,8)
        start_spot = moves_list[random_number] #Chooses a starting position

        if moves_dictionary[start_spot] == " ":
            moves_dictionary[start_spot] = comp_choice #Sets starting position to X or O
            print(board())
        else:
            computer_move(comp_choice)

    def check_winner(dictionary):
        #Rows
        if dictionary["tl"] == dictionary["tm"] and dictionary["tm"] == dictionary["tr"]:
            if dictionary["tl"] == "X":
                print("X wins")
                return False
            elif dictionary["tl"] == "O":
                print("O wins")
                return False
        elif dictionary["ml"] == dictionary["mm"] and dictionary["mm"] == dictionary["mr"]:
            if dictionary["ml"] == "X":
                print("X wins")
                return False
            elif dictionary["ml"] == "O":
                print("O wins")
                return False
        elif dictionary["bl"] == dictionary["bm"] and dictionary["bm"] == dictionary["br"]:
            if dictionary["bl"] == "X":
                print("X wins")
                return False
            elif dictionary["bl"] == "O":
                print("O wins")
                return False
        #Columns
        elif dictionary["tl"] == dictionary["ml"] and dictionary["ml"] == dictionary["bl"]:
            if dictionary["tl"] == "X":
                print("X wins")
                return False
            elif dictionary["tl"] == "O":
                print("O wins")
                return False
        elif dictionary["tm"] == dictionary["mm"] and dictionary["mm"] == dictionary["bm"]:
            if dictionary["tm"] == "X":
                print("X wins")
                return False
            elif dictionary["tm"] == "O":
                print("O wins")
                return False
        elif dictionary["tr"] == dictionary["mr"] and dictionary["mr"] == dictionary["br"]:
            if dictionary["tr"] == "X":
                print("X wins")
                return False
            elif dictionary["tr"] == "O":
                print("O wins")
                return False
        #Diagnols
        elif dictionary["tl"] == dictionary["mm"] and dictionary["mm"] == dictionary["br"]:
            if dictionary["tl"] == "X":
                print("X wins")
                return False
            elif dictionary["tl"] == "O":
                print("O wins")
                return False
        elif dictionary["tr"] == dictionary["mm"] and dictionary["mm"] == dictionary["bl"]:
            if dictionary["tr"] == "X":
                print("X wins")
                return False
            elif dictionary["tr"] == "O":
                print("O wins")
                return False
        else:
            return True

##Main
    while game_on == True:
        user_input = start_game()

        if user_input == "X":

            computer_move("O")
            user_move(user_input)
            computer_move("O")
            user_move(user_input)
            computer_move("O")
            game_on = check_winner(moves_dictionary)
            if game_on == False:
                break
            user_move(user_input)
            game_on = check_winner(moves_dictionary)
            if game_on == False:
                break
            computer_move("O")
            game_on = check_winner(moves_dictionary)
            if game_on == False:
                break
            user_move(user_input)
            game_on = check_winner(moves_dictionary)
            if game_on == False:
                break
            computer_move("O")
            game_on = check_winner(moves_dictionary)
            if game_on == False:
                break
            print("Tie")
            break
        else:
            computer_move("X")
            user_move(user_input)
            computer_move("X")
            user_move(user_input)
            computer_move("X")

            game_on = check_winner(moves_dictionary)
            if game_on == False:
                break
            user_move(user_input)
            game_on = check_winner(moves_dictionary)
            if game_on == False:
                break
            computer_move("X")
            game_on = check_winner(moves_dictionary)
            if game_on == False:
                break
            user_move(user_input)
            game_on = check_winner(moves_dictionary)
            if game_on == False:
                break
            computer_move("X")
            game_on = check_winner(moves_dictionary)
            if game_on == False:
                break
            print("Tie")
            break

    play_again = input('Would you like to play again? \n'
                       'If Yes type "Y" if No type "N":\n')
    play_again = play_again .upper()
    if play_again == "Y":
        tic_toe_game()
    else:
        print("Thanks for playing!")

tic_toe_game()














