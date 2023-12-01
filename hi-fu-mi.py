
import random
import inquirer
from colorama import Fore, Back
import tools

#initialisation des variables
options:list = ["Hi", "Fu", "Mi"]
options_select: list = [inquirer.List
            ('choice',
                message="What do you play ?",
                choices=options,
            ),
]
Game: bool = True;


#Play
#ai_choice: int = random.randint(0,2)
#player_choice:int = int(input('Veuillez entrer un nombre'))
#matchRound = [player_choice,ai_choice]

# We create the function that is
def PlayRound(playerChoice,score):
    
    # We create the list that contain all our combinations and an other list that (with the same index) contain the score for the player and the AI
    possibilite: list = [["Hi","Hi"],["Hi","Fu"],["Hi","Mi"],["Fu","Hi"],["Fu","Fu"],["Fu","Mi"],["Mi","Hi"],["Mi","Fu"],["Mi","Mi"]]
    result: list = [[0,0,1,1,0,0,0,1,0],[0,1,0,0,0,1,1,0,0]]
    
    # We insert the player choice in the 0 index and the ai choice in the 1 index
    matchRound = [playerChoice,random.choice(options)]
    
    # Then we insert in the score the result of the combination depending of the index
    score[0] += result[0][possibilite.index(matchRound)]
    score[1] += result[1][possibilite.index(matchRound)]
    
    # We initiate a third score index that contain the last combination so we can use it in an other function to display the ui depending of the last result
    score[2][0] = result[0][possibilite.index(matchRound)]
    score[2][1] = result[1][possibilite.index(matchRound)]
 
    print("Hi....\nFu....\nMi !");
    
    #We then return the score
    return score
    
# We create a function that display the result of the last round depending of the last score update
def DisplayRoundResult(score):
    
    if(score[2] == [1,0]):
        print(Fore.GREEN +"YOU WON THIS ROUND !",Fore.RESET)
    if(score[2] == [0,1]):
        print(Fore.RED + "YOU LOST THIS ROUND !",Fore.RESET)
    if(score[2] == [0,0]):
        print(Back.WHITE,Fore.BLACK +"IT'S A DRAW NOBODY WON",Fore.RESET,Back.RESET)
                       
while Game:
    
    # Reset de la variable score à zéro, index 0 = score du joueur, index 1 = score de l'ordinateur, index 2 = résultat du dernier round
    score:list = [0,0,[0,0]];
    i:int = 0
    
    #I force the player to enter a int value
    while True:
        try:
            round:int = int(input("Hi ! Welcome to the Hi, Fu, Mi ! Game. \nHow many round do you want to play ? "))
            #break stop the loop and allow to continue the script. but if there is an error it won't break.
            break
        except ValueError:
            #if there is a ValueError, like writting a chain character instead of a number, I warn the player that he needs to put only a number.
            print(Fore.YELLOW,"\nHey hey hey, I asked you to put a number, not a word or a sentence. How do you want me to understand that you want to play 35 round if you indicate me 'THIRTY FIVE' as a string ! \nPlease, retry (but this time with a number) :)",Fore.WHITE)

    while i < round:
        
        print(Fore.YELLOW , "\n \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\", Fore.RESET, Back.YELLOW,"           ",Back.RESET )
        print(Fore.YELLOW ,"Round : ", int(i+1), Fore.GREEN ,"  Your score = ", str(score[0]) , Fore.RED ," AI score = ", str(score[1]) , Fore.BLUE)
        print(Fore.YELLOW , Back.YELLOW, "           " , Back.RESET , "/////////////////////////////////\n" , Back.RESET , Fore.RESET,)
        
        score = PlayRound(inquirer.prompt(options_select)['choice'],score);
        DisplayRoundResult(score)
        
        i+=1
    
    Game = tools.EndGame();
