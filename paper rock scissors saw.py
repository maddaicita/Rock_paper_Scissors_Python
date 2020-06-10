"""
“Rock, Paper, Scissors, and Saw”
"""
import random as r




print("..................................... .................................................................................")
print("..................................... ROCK, PAPER, SCISSORS AND SAW GAME...............................................")
print("..................................... .................................................................................")


"""..................................... ..................................................................................... """
"""..................................... DATA STRUCTURES DEFINITION........................................................... """
"""..................................... ......................................................................................"""


players=[" "," "]
player1stats=[[0,0,0],[0,0,0]] #list to save the statistic for the round, won, lost, or tied
player2stats=[[0,0,0],[0,0,0]]







"""..................................... ......................................................................................... """
"""..................................... FUNCTIONS DEFINITION..................................................................... """
"""..................................... ......................................................................................... """

#this function prompt the user to enter the two players names then validate and save them into a players array.
def validatePlayer():
    MIN_LIMIT=5
    MAX_LIMIT=20
    player1=''
    player2=''
    while True:
        player1= input("“What is the name of the first player?\n")
        
        if len(player1)< MIN_LIMIT:
            print("Make sure the Player1 names have more than 5 letters")
        elif len(player1)>MAX_LIMIT:
            print("Make sure the Player1 names have not more than 20 letters")
        else:
            players[0]=player1
            break
    while True:
        player2= input("What is the name of the second player?\n")
        if len(player2)<MIN_LIMIT :
            print("Make sure the Player2 names have more than 5 letters")
        elif len(player2)>MAX_LIMIT :
            print("Make sure the Player2 names have not more than 20 letters")
        elif player2==player1 :
            print("Enter a Different name")
        else:
            players[1]=player2
            break

#this function uses the player array to get the name of player 1 and prompt the player toselect a weapon.Display the choice selected      
def weapon_P1_Selection():
    print("\n", players[0],"'s turn\n")

    choice = {}
    choice['1']="for Rock." 
    choice['2']="for Paper."    
    choice['3']="for Scissors"
    choice['4']="for Saw"

    while True:
        options=choice.keys()
      
        for entry in options:
            print (entry, choice[entry])
        selection=input("Please Select one of the weapons:") 
        if selection =='1':
            choice_P1 = 'Rock'
            print(players[0]," selected ", choice_P1)
            return choice_P1
            break 
        elif selection == '2':
            choice_P1 = 'Paper'
            print(players[0]," selected ", choice_P1)
            return choice_P1
            break 
        elif selection == '3':
            choice_P1 = 'Scissors'
            print(players[0]," selected ", choice_P1)
            return choice_P1
            break 
        elif selection == '4':
           choice_P1 = 'Saw'
           print(players[0]," selected ", choice_P1)
           return choice_P1
           break 
        else: 
            print ("Wrong Option Selected!" )
            
#this function uses the player array to get the name of player 2 and prompt the player toselect a weapon.Display the choice selected       
def weapon_P2_Selection():
    print("\n", players[1],"'s turn\n")

    choice = {}
    choice['1']="for Rock." 
    choice['2']="for Paper."    
    choice['3']="for Scissors"
    choice['4']="for Saw"

    while True:
        options=choice.keys()
      
        for entry in options:
            print (entry, choice[entry])
        selection=input("Please Select one of the weapons:") 
        if selection =='1':
            choice_P2 = 'Rock'
            print(players[1]," selected ", choice_P2)
            return choice_P2
            break 
        elif selection == '2':
            choice_P2 = 'Paper'
            print(players[1]," selected ", choice_P2)
            return choice_P2
            break 
        elif selection == '3':
            choice_P2 = 'Scissors'
            print(players[1]," selected ", choice_P2)
            return choice_P2
            break 
        elif selection == '4':
           choice_P2 = 'Saw'
           print(players[1]," selected ", choice_P2)
           return choice_P2
           break 
        else: 
            print ("Wrong Option Selected!" )


# gives x a random value from 1-4 and translates the integer into a string.Display the choice selected    
def comp_Weapon():
    pc_Choice = str(r.randint(1,4));
    print("\n Computer turn\n")
    selection=pc_Choice 
    if selection =='1':
        pc_Choice = 'Rock'
        print("Computer selected ", pc_Choice)
        
    elif selection == '2':
        pc_Choice = 'Paper'
        print("Computer selected ", pc_Choice)
        
    elif selection == '3':
        pc_Choice = 'Scissors'
        print("Computer selected ", pc_Choice)
        
    else:
        pc_Choice = 'Saw'
        print("Computer selected ", pc_Choice)
        
    return pc_Choice   


# determines if player 1 won, lost, or tied the previous round and adds it into the appropriate slot in player1stats        
def determine_winner_p1():
    choice_P1=weapon_P1_Selection()
    choice1_Comp=comp_Weapon()
    ties=player1stats[0][2]
    won= player1stats[0][0]
    lose=player1stats[0][1]
    
    if choice_P1==choice1_Comp:
        ties+=1
        print("This round was tied")
        
    elif choice_P1=='Rock':
        if choice1_Comp=='Scissors' or choice1_Comp=='Saw':
            won+=1
            print(players[0],"Won")
        else:
            lose+=1
            print(players[0],"Lose")

    elif choice_P1 == 'Paper':
        if choice1_Comp=='Rock':
            won+=1
            print(players[0],"Won")
        else:
            lose+=1
            print(players[0],"Lose")
                  
    elif choice_P1=='Scissors':
        if choice1_Comp=='Paper':
            won+=1
            print(players[0],"Won")
        else:
            lose+=1
            print(players[0],"Lose")
                  
    elif choice_P1=='Saw':
        if choice1_Comp=='Scissors' or choice1_Comp=='Paper':
            won+=1
            print(players[0],"Won")
        else:
            lose+=1
            print(players[0],"Lose")
                  
    
    player1stats[0][2]=ties
    player1stats[0][0]=won
    player1stats[0][1]=lose
    


# determines if player 2 won, lost, or tied the previous round and adds it into the appropriate slot in player2stats

def determine_winner_p2():  #incrementar round y ademas obtener el valor que hay en la lista para incrementarlo despues 
    choice_P2=weapon_P2_Selection()
    choice2_Comp=comp_Weapon()
    ties=player2stats[0][2]
    won= player2stats[0][0]
    lose=player2stats[0][1]
    
    if choice_P2==choice2_Comp:
        ties+=1
        print("This round was tied")
    
    elif choice_P2=='Rock':
        if choice2_Comp=='Scissors' or choice2_Comp=='Saw':
            won+=1
            print(players[1],"Won")
        else:
            lose+=1
            print(players[1],"Lose")
    
    elif choice_P2=='Paper':
        if choice2_Comp=='Rock':
            won+=1
            print(players[1],"Won")
        else:
            lose+=1
            print(players[1],"Lose")
                  
    elif choice_P2=='Scissors':
        if choice2_Comp=='Paper':
            won+=1
            print(players[1],"Won")
        else:
            lose+=1
            print(players[1],"Lose")
                  
    elif choice_P2=='Saw':
        if choice2_Comp=='Scissors' or choice2_Comp=='Paper':
            won+=1
            print(players[1],"Won")
        else:
            lose=lose+1
            print("You have",players[1],"Lose")
            
    player2stats[0][2]=ties
    player2stats[0][0]=won
    player2stats[0][1]=lose
    
             
 
# determines if player 1 won, lost, or tied the previous game and adds it into the appropriate slot in player1stats
def determine_p1_game_wins():
    winGameP1= player1stats[1][0] #the games that won the player 1
    tiesGameP1=player1stats[1][2]#the games that tied the player 1
    loseGameP1=player1stats[1][1]#the games that lose the player 1

    winRoundP1=player1stats[0][0]
    winRoundP2=player2stats[0][0]
    tiesRoundP1=player1stats[0][1]
    loseRoundP1=player1stats[0][2]

    if winRoundP1>=2:
        player1stats[1][0]=winGameP1+1
        print(players[0],"Won the game")
        
    elif loseRoundP1>=2:
        player1stats[1][1]=loseGameP1+1
        print(players[0],"Computer won")
        
    elif winRoundP1==1 and winRoundP2==1:
        player1stats[1][2]=tiedtGameP1+1
        print(players[0],"Tied Game, no winners")


# determines if player 2 won, lost, or tied the previous game and adds it into the appropriate slot in player2stats
def determine_p2_game_wins():
    
    winGameP2= player2stats[1][0] #the games that won the player 1
    tiesGameP2=player2stats[1][2]#the games that tied the player 1
    loseGameP2=player2stats[1][1]#the games that lose the player 1

    winRoundP2=player2stats[0][0]
    winRoundP1=player1stats[0][0]
    tiedRoundP2=player2stats[0][1]
    loseRoundP2=player2stats[0][2]

    if winRoundP2>=2:
        player1stats[1][0]=winGameP2+1
        print("Won the game")
        
    elif loseRoundP2>=2:
        player1stats[1][1]=loseGameP2+1
        print("Computer won")
        
    elif winRoundP2==1 and winRoundP1==1:
        player1stats[1][2]=tiesGameP2+1
        print("Tied Game, no winners")
        
 
# after three rounds played this function determine who won the game, player 1, 2 or the computer.
def play_Game():

    for x in range(0,3):
        print("\n***********")
        print("ROUND", x+1)
        print("*************")
        #call function to get player 1’s choice i.e., p1_weapon = p1choice() 
        determine_winner_p1()
        #call function to get player 2’s choice i.e., p2_weapon = p2choice()
        determine_winner_p2()
    # after three rounds played determine who won the game, player 1, 2 or the computer.
  
    determine_p1_game_wins()
    determine_p2_game_wins()




#Displays who is winning overall
def determine_winner_overall():
    
    #same numbers of wins, losses and ties.Is Tied
    if player1stats[0][0] == 0 and player2stats[0][0] == 0:
        return "You have to play first"
    elif player2stats[1][0] == player1stats[1][0]:
         if player2stats[1][1] == player1stats[1][1]:
             if player2stats[1][2] == player1stats[1][2]:
                 return (players[0] + " and " + players[1] + " are tied!")
                
            #If  player 1 has more ties than the player2 or viceversa  
             elif player1stats[1][2] > player2stats[1][2]:
                 return (players[0]," is the winner")
             else:
                 return (players[1]," is the winner")
                
         #if player 1 have less loses or win
         elif player1stats[1][1] < player2stats[1][1]:
             return (players[0]," is the winner")
         else:
             return (players[1]," is the winner")
            
    elif player1stats[1][0] > player2stats[1][0]:
        return (players[0]," is the winner")
    else:
        return (players[1]," is the winner")
     

# function displays the Wins, Loses, and Ties.Displays who is winning overall
def stats():
    print("************************************************************************************************")
    print("************************************************************************************************")
    print(" “ROCK, PAPER, SCISSORS, AND SAW” GAME STATISTICS\n")
    print("************************************************************************************************")
    print("************************************************************************************************")
    print("Players\t\tRounds:\t win\tLost\tTied\t\tGames:\t win\tLost\tTied")

    player1= "{:<20}".format(players[0])
    player2= "{:<20}".format(players[1])


    print(player1 + "\t " + str(player1stats[0][0]) + "\t " + str(player1stats[0][1]) +
    "\t " + str(player1stats[0][2]) + "\t\t\t " + str(player1stats[1][0]) + "\t " + str(player1stats[1]
    [1]) + "\t " + str(player1stats[1][2]))
    print(player2 + "\t "+ str(player2stats[0][0]) + "\t " + str(player2stats[0][1]) +
    "\t " + str(player2stats[0][2]) + "\t\t\t " + str(player2stats[1][0]) + "\t " + str(player2stats[1]
    [1]) + "\t " + str(player2stats[1][2]) + "\n")
    print("\n*********************************************************************************************")

    print("\n*********************************************************************************************")

    #print the winner
    print(determine_winner_overall())
    print("\n*********************************************************************************************")
    print("\n*********************************************************************************************")

def rules():
    
    print("*********************************************************************************************************************")
    print("*********************************************************************************************************************")
    print(" “ROCK, PAPER, SCISSORS, AND SAW” GAME RULES\n")
    print("*********************************************************************************************************************")
    print("*********************************************************************************************************************")
    print("Winner of the round will be determined as follow:\n")
    print( "a.Rock breaks scissors and Saw therefore rock wins over scissors and saw. Rock loses against paper.\n")
    print( "b.Scissors cut paper therefore scissors win over paper. Scissors lose against rock and Saw.\n")
    print( "c.Paper covers rock therefore paper wins over rock. Paper loses against scissors and saw.\n")
    print( "d.Saw cuts through scissors and paper therefore saw wins over scissors and paper. Saw loses against rock.\n")
    print( "e.If player and computer make the same selection, there is a tie.\n")
    print( "Winner of the game against the computer is one who won more rounds (must account for ties)\n")
    print( "Overall human winner is based on the greater number of won games against the computer. \n")
    print( "and least games lost (must account for tie between human players)")
    print("*********************************************************************************************************************")
    print("*********************************************************************************************************************")


            
def main():
    
    validatePlayer()
    
    print("..................................... ......................................................................... .....")
    print("  HELLO ",players[0],"and",players[1],"!\n","WHAT DO YOU WANT TO DO NEXT?")
    print("..................................... ...............................................................................")
    menu = {}
    menu['1']="Play Game." 
    menu['2']="Show Game Rules."    
    menu['3']="Show Statistics"
    menu['4']="Exit"

    while True:
        options=menu.keys()
      
        for entry in options:
            print (entry, menu[entry])

        selection=input("Please Select one of the options:") 
        if selection =='1':
            play_Game()
            
        elif selection == '2':
           
             rules()

        elif selection == '3':
            stats()
            
        elif selection == '4':
            print("\nGoodbye\n")
            break
        
        else: 
            print ("Unknown Option Selected!" ) 





    

"""..................................... ................................................................................. """
"""..................................... PROGRAM FLOW..................................................................... """
"""..................................... ................................................................................. """


main()




