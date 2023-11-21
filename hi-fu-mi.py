#We import all the necessary packages
import random
import inquirer
from colorama import Fore, Back, Style

def Play(playerChoice,computerChoice,score):
    print("Hi....\nFu....\nMi !")
    #we compare the choice between the player and the AI
    if playerChoice == computerChoice:
        print(Back.WHITE,Fore.BLACK,"IT'S A DRAW, YOU BOTH PICK THE SAME CHOICE, RETRY",Fore.BLUE,Back.RESET)
    #elif allow us to make multiple comparison
    elif playerChoice == "Hi" and computerChoice == "Mi" \
    or playerChoice == "Fu" and computerChoice == "Hi" \
    or playerChoice == "Mi" and computerChoice == "Fu":
        #if the player won we give him 1 point
        print(Fore.GREEN + "YOU WON THIS ROUND ! your choice was '", str(playerChoice), "' and the ai choice was '", computerChoice, "'",Fore.RESET)
        score[0] += 1;
    else:
        #if the ai won we give him 1 point
        print(Fore.RED + "YOU LOST THIS ROUND ! your choice was '", str(playerChoice), "' and the ai choice was '", computerChoice, "'",Fore.RESET)
        score[1] += 1;
        
    return score;
        
def DisplayScore(score):
    #We announce to the player who won the match
    if score[0] > score[1]:
        print(Back.GREEN ,"YOU THE BEAST, YOU WON THIS MATCH AND BY FAR !", Back.RESET)
    elif score[0] == score[1]:
        print(Back.YELLOW ,"YOU BOTH NOOB, NONE OF YOU ARE EVEN ABLE TO WON AT A HI FU MI GAME WTF", Back.RESET)
    else:
        print(Back.RED ,"WHAT A SHAME, YOU LOST TO A COMPUTER !", Back.RESET)
    

print("///////////////////////////////\n///////////////////////////////\n///////////////////////////////\n///////////////////////////////")
print(Back.WHITE,Fore.BLACK,"//!\\\\ THE UI OF THIS PYTHON PROGRAM HAS BEEN DEVELOP TO WORK ON MACOS, LINUX, OR GITBASH ON WINDOWS,")
print("SO PLEASE DON'T TRY TO USE IT ON WINDOWS CMD OR POWERSHELL, EITHER YOU'RE GOING TO HAVE SOME ERROR MESSAGES")
print("ALSO BE SURE TO HAVE THE COLORAMA PACKAGE FOR PYTHON INSTALLED ON YOUR COMPUTER")
print("IF NOT, YOU NEED TO INSTALL IT BY WRITING THIS SMALL LINE ON YOUR GITBASH CONSOLE \"-pip install colorama\" THIS LINE WON'T WORK ON MAC, TRY THIS \" pip3 install colorama\"") 
print("THANK YOU, and ENJOY")
print("But watchout, the narrator may be a bit... arrogant.",Back.RESET,Fore.RESET)
print("///////////////////////////////\n///////////////////////////////\n///////////////////////////////\n///////////////////////////////\n\n")

#I force the player to enter a int value
while True:
    try:
        round = int(input("Hi ! Welcome to the Hi, Fu, Mi ! Game. \nHow many round do you want to play ? "))
        #break stop the loop and allow to continue the script. but if there is an error it won't break.
        break
    except ValueError:
        #if there is a ValueError, like writting a chain character instead of a number, I warn the player that he needs to put only a number.
        print(Fore.YELLOW,"\nHey hey hey, I asked you to put a number, not a word or a sentence. How do you want me to understand that you want to play 35 round if you indicate me 'THIRTY FIVE' as a string ! \nPlease, retry (but this time with a number) :)",Fore.WHITE)

#we set the default score for the player and the score to 0
score: list = [0,0]
i:int  = 0

#we set the three different options that the player and the computer are willing to choose
ai_options = ["Hi", "Fu", "Mi"]

options = [inquirer.List
            ('choice',
                message="What do you play ?",
                choices=ai_options,
            ),
]

#I create an other array for the computer choice because we can't randomly select an value in an inquirer list

#while the sum of player_score + ai_score is under the number of round the player want to play the loop doesn't stop
while i < round:

    #simple UI that indicate to the player which round he is playing and the score of both opponents
    print(Fore.YELLOW , "\n \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\", Fore.RESET, Back.YELLOW,"           ",Back.RESET )
    print(Fore.YELLOW ,"Round : ", int(i+1), Fore.GREEN ,"  Your score = ", str(score[0]) , Fore.RED ," AI score = ", str(score[1]) , Fore.BLUE)
    print(Fore.YELLOW , Back.YELLOW, "           " , Back.RESET , "/////////////////////////////////\n" , Back.RESET , Fore.RESET,)
    
    score = Play(inquirer.prompt(options)['choice'],random.choice(ai_options),score);
    i += 1;
    
DisplayScore(score);
    


    


