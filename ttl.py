#!/home/mamaah/development/TTL/bin/python3
import getpass
import sys

#TTL = two truths and a lie
#Two players; Player 1 and Player 2
#two players, three items, two are true and one is a lie
#Player 1 names three items, two of the items are true, one is a lie
#Player 1 names item which is a lie (happy now?)
#computer should convert input into numerical values
#Player 2, determines wc is a lie
#if player 2 gives a wrong response, players switch "sides"
#player 2 now names three items for round 2 to begin
#player 1 identifies which item is a lie
#if player 1 gives wrong response, game restarts

#Define some functions
def TTL():
    player_input1 = input('please enter your 1st statement: ')
    player_input2 = input('please enter your 2nd statement: ')
    player_input3 = input('please enter your 3rd statement: ')
    return player_input1, player_input2, player_input3

while True:
    try:
        #welcome the players by creating a welcome message
        print('welcome to two truths and a lie')
        #create game instructions
        print('game rules')
        print("""
        TTL = two truths and a lie
        Two players; Player 1 and Player 2
        two players, three items, two are true and one is a lie
        Player 1 names three items, two of the items are true, one is a lie
        Player 1 names item which is a lie (happy now?)
        computer should convert input into numerical values
        Player 2, determines wc is a lie
        if player 2 gives a wrong response, players switch "sides"
        player 2 now names three items for round 2 to begin
        player 1 identifies which item is a lie
        if player 1 gives wrong response, game restarts
        """)
        #first we create a variable called count and we set it to zero
        count = 0
        #then we say while count is less than 2, keep running 
        #Player 1 and 2 will get a turn while count is less than 2
        while count < 2:
            if count == 0:
                print("this is player_one's turn")
                print()
            else:
                print("this is player_two's turn")
                print()
            #get and save three inputs from player 1
            player1_responses = TTL()

            #convert inputs to numerical values
            numericals = {1: player1_responses[0],2:player1_responses[1], 3:player1_responses[2]}
            for k, v in numericals.items():
                print(k, ":", v)
            #get numerical input from Player 1 for the lie
            lie = getpass.getpass('active_player, please enter numeric value for the lie: ')
            #get input from player 2 for the lie
            other_player = input('please enter your guess for the lie: ')
            #compare player 1's input with player 2's input
            
            #if lie == player2_guess
            if lie == other_player:
                #print(Right)
                print('oh well, you got it!!!')
            else:
                #if player2's input != player1's input
                #print(Wrong)
                print('your butt got tricked!')
            count += 1
            print()
    except KeyboardInterrupt:
        print(" i'm sorry you have to go!")
        sys.exit()
    play_again = input("Do you want to play again?: ")
    if play_again.upper() == "N":
        break
