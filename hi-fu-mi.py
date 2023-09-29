#We import all the necessary packages
import random
from colorama import Fore, Back, Style

print("///////////////////////////////\n///////////////////////////////\n///////////////////////////////\n///////////////////////////////")
print(Back.WHITE,Fore.BLACK,"//!\\\\ THE UI OF THIS PYTHON PROGRAM HAS BEEN DEVELOP TO WORK ON MACOS, LINUX, OR GITBASH ON WINDOWS,")
print("SO PLEASE DON'T TRY TO USE IT ON WINDOWS CMD OR POWERSHELL, EITHER YOU'RE GOING TO HAVE SOME ERROR MESSAGES")
print("ALSO BE SURE TO HAVE THE COLORAMA PACKAGE FOR PYTHON INSTALLED ON YOUR COMPUTER")
print("IF NOT, YOU NEED TO INSTALL IT BY WRITING THIS SMALL LINE ON YOUR CONSOLE \"-pip install colorama\"")
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


#we ask the player how much round they want to play
#round = int(input("Hi ! Welcome to the Hi, Fu, Mi ! Game. \nHow many round do you want to play ? "))
#print("please make an effort : ", round)

#we set the default score for the player and the ai to 0
player_score = 0
ai_score = 0
i = 0

#we set the three different options that the player and the ai are willing to choose
options = ["hi", "fu", "mi"]


#while the sum of player_score + ai_score is under the number of round the player want to play the loop doesn't stop
#I could have used an iterator like i and write "while i < round : player_choice... i += 1", both work in this situation
while i < round:

    #simple UI that indicate to the player which round he is playing and the score of both opponents
    print(Fore.YELLOW , "\n \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\", Fore.RESET, Back.YELLOW,"           ",Back.RESET )
    print(Fore.YELLOW ,"Round : ", int(i+1), Fore.GREEN ,"  Your score = ", player_score , Fore.RED ," AI score = ", ai_score , Fore.BLUE)
    print(Fore.YELLOW , Back.YELLOW, "           " , Back.RESET , "/////////////////////////////////\n" , Back.RESET , Fore.RESET,)
    
    #we ask the player which choice he want to play
    player_choice = input("What are you playing ? Hi, Fu or Mi ?\nSmall reminder : hi>mi, fu>hi, mi>fu\nYour choice : ")
    
    #we redirect the player everytime he choose an unknow option
    while player_choice not in options:
        player_choice = input("Wrong choice ! You choose, Hi, Fu or Mi ! (without the quotation marks of course)")

    print("Hi....\nFu....\nMi !")
    
    #we select a random choixe available in the table we created named "options"
    ai_choice = random.choice(options)

    #we compare the choice between the player and the AI
    if player_choice == ai_choice:
        print(Back.WHITE,Fore.BLACK,"IT'S A DRAW, YOU BOTH PICK THE SAME CHOICE, RETRY",Fore.BLUE,Back.RESET)
    #elif allow us to make multiple comparison
    elif player_choice == "hi" and ai_choice == "mi" \
    or player_choice == "fu" and ai_choice == "hi" \
    or player_choice == "mi" and ai_choice == "fu":
        #if the player won we give him 1 point
        print(Fore.GREEN + "YOU WON THIS ROUND ! your choice was '", str(player_choice), "' and the ai choice was '", ai_choice, "'",Fore.RESET)
        player_score += 1
        i += 1
    else:
        #if the ai won we give him 1 point
        print(Fore.RED + "YOU LOST THIS ROUND ! your choice was '", str(player_choice), "' and the ai choice was '", ai_choice, "'",Fore.RESET)
        ai_score += 1
        i += 1

#We announce to the player who won the match
if player_score > ai_score:
    print(Back.GREEN ,"YOU THE BEAST, YOU WON THIS MATCH AND BY FAR !", Back.RESET)
elif player_score == ai_choice:
    print(Back.YELLOW ,"YOU BOTH NOOB, NONE OF YOU ARE EVEN ABLE TO WON AT A HI FU MI GAME WTF", Back.RESET)
else:
    print(Back.RED ,"WHAT A SHAME, YOU LOST TO A COMPUTER !", Back.RESET)
