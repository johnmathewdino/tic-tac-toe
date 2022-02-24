# Instructions:
# Create a tic-tac-toe program using Python command line. You are NOT allowed to search for or copy any tic-tac-toe
# code from the Internet. You must create everything from scratch.
# However, you are allowed to search for syntax of Python in w3schools.com or other reference sites.
# 1) It should be a 2-player app.
# 2) The token of the players can be just plain-text: X and O.
# 3) The board should be drawn in the following 3x3 tic-tac-toe board format:
# 		Example:	X _ O
# 				_ X _
# 				_ _ _
# 4) The first player will play X. The second player will play O.
# 5) The application should determine when a player wins or there is a draw.
# 6) Email the Python .py files to eusebio.yu@achievewithoutborders.com for grading.
# Bonus: Maintain scores for both players.
# Time Limit: 6 hours






board_dict = {1: "_", 2: "_", 3: "_", 4: "_", 5: "_", 6: "_", 7: "_", 8: "_", 9: "_"}

# the board
def board(board_dict):
    board = """
    
    {} {} {}
    {} {} {}
    {} {} {}
    
     """.format(board_dict[1], board_dict[2], board_dict[3], board_dict[4], board_dict[5], board_dict[6],
                     board_dict[7], board_dict[8], board_dict[9])
    print(board)




def game (p1_score=0,p2_score=0):
    turn_count = 0
    mark = 'X'
    player = "Player 1"
    board(board_dict)


    # 9 correct turn at most
    while turn_count != 9:

        # input of the user
        turn = input("{} turn: ".format(player))

        # if input is == exit or quit, exit the game

        if turn.lower() == "exit" or turn.lower() == "quit":
            quit()

        try:
            # if turn = 1-9
            if int(turn) in board_dict:

                # if turn not yet marked
                if board_dict[int(turn)] == "_":
                    board_dict[int(turn)] = mark


                    # turn count plus 1 --- correct turn
                    turn_count += 1
                    # change player
                    if mark == "X":
                        mark = "O"
                        player = "Player 2"
                    else:
                        mark = "X"
                        player = "Player 1"
                # if turn is already taken
                else:
                    print("turn already taken.")
                # display board
                board(board_dict)

                # Check if player 1 wins:
                if board_dict[1] == "X" and board_dict[2] == "X" and board_dict[3] == "X":
                    print("player 1 wins")
                    p1_score+=1
                    # board(board_dict)
                    break
                elif board_dict[4] == "X" and board_dict[5] == "X" and board_dict[6] == "X":
                    print("player 1 wins")
                    p1_score += 1
                    board(board_dict)
                    break
                elif board_dict[7] == "X" and board_dict[8] == "X" and board_dict[9] == "X":
                    print("player 1 wins")
                    p1_score += 1
                    board(board_dict)
                    break
                elif board_dict[1] == "X" and board_dict[4] == "X" and board_dict[7] == "X":
                    print("player 1 wins")
                    p1_score += 1
                    board(board_dict)
                    break
                elif board_dict[2] == "X" and board_dict[5] == "X" and board_dict[8] == "X":
                    print("player 1 wins")
                    p1_score += 1
                    board(board_dict)
                    break
                elif board_dict[3] == "X" and board_dict[6] == "X" and board_dict[9] == "X":
                    print("player 1 wins")
                    p1_score += 1
                    board(board_dict)
                    break
                elif board_dict[7] == "X" and board_dict[5] == "X" and board_dict[3] == "X":
                    print("player 1 wins")
                    p1_score += 1
                    board(board_dict)
                    break
                elif board_dict[1] == "X" and board_dict[5] == "X" and board_dict[9] == "X":
                    print("player 1 wins")
                    p1_score += 1
                    board(board_dict)
                    break


                # check if player 2 wins
                elif board_dict[1] == "O" and board_dict[2] == "O" and board_dict[3] == "O":
                    print("player 2 wins")
                    p2_score += 1
                    board(board_dict)
                    break
                elif board_dict[4] == "O" and board_dict[5] == "O" and board_dict[6] == "O":
                    print("player 2 wins")
                    p2_score += 1
                    board(board_dict)
                    break
                elif board_dict[7] == "O" and board_dict[8] == "O" and board_dict[9] == "O":
                    print("player 2 wins")
                    p2_score += 1
                    board(board_dict)
                    break
                elif board_dict[1] == "O" and board_dict[4] == "O" and board_dict[7] == "O":
                    print("player 2 wins")
                    p2_score += 1
                    board(board_dict)
                    break
                elif board_dict[2] == "O" and board_dict[5] == "O" and board_dict[8] == "O":
                    print("player 2 wins")
                    p2_score += 1
                    board(board_dict)
                    break
                elif board_dict[3] == "O" and board_dict[6] == "O" and board_dict[9] == "O":
                    print("player 2 wins")
                    p2_score += 1
                    board(board_dict)
                    break
                elif board_dict[7] == "O" and board_dict[5] == "O" and board_dict[3] == "O":
                    print("player 2 wins")
                    p2_score += 1
                    board(board_dict)
                    break
                elif board_dict[1] == "O" and board_dict[5] == "O" and board_dict[9] == "O":
                    print("player 2 wins")
                    p2_score += 1
                    board(board_dict)
                    break

                if turn_count == 9:
                    print("----DRAW----")


            # if turn != 1-9
            else:
                board(board_dict)
                print("Select from 1-9 only")

                continue
        except:
            board(board_dict)
            print("Select from 1-9 only")

            continue

    # print score
    print("Player 1 (X) score: {},\nPlayer 2 (O) score: {}".format(p1_score,p2_score))
    restart = input("Press [Y] to play again: ")
    if restart.lower() == "y":

        # clear the dictionary
        for i in range(10):
            board_dict[i] = "_"
        # restart the game
        game(p1_score=p1_score,p2_score=p2_score)


def menu():

    menu = int(input("""
        W E L C O M E
             T O 
    T I C - T A C - T O E
    
Instruction:
Enter 1-9 to mark your turn. The format of the board is as below:

            1 2 3
            4 5 6
            7 8 9

    Enter [1] to play game
    Enter [quit] or any key to quit
    """))

    if menu == 1:
        game()
    elif menu == 2:
        pass
    else:
        quit()




menu()







