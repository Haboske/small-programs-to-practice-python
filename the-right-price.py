import random
import tools

# Creating a function that ask the player to choose range limit of the right price
def AskGameLimit(limitAsked: str):

    print("I'll need you to choose the "+limitAsked+" value of the right price.")
    
    limitValue: str = tools.AskUnsignedInt();
        
    return int(limitValue);

# Creating a function that compare the player choice with the priced defined randomly before the player start the game
def CheckPlayerChoice(playerChoice,price,tries):

    #if the number the player entered is less the price
    if playerChoice < price:

        #calculate the difference to check if the player is far away from the good price or not
        difference = price - playerChoice;
        if difference >= 10:
            print("lot more");
            return True;
        if difference < 10:
            print("more");
            return True;

    # Same tha above but if more than the price
    if playerChoice > price:

        difference = playerChoice - price
        if difference >= 10:
            print("lot less");
            return True; 
        if difference < 10:
            print("less");
            return True;

    # If the player found the right price   
    if playerChoice == price:
        print("You found the right price !");
        print("Your score is "+str(10-tries)+"/10 !");
        return False;
    
# Creating a function that is called at the end of the game when the player found the right price.
def EndGame():

    # Asking the user if he still wants to play or not
    answer: str =  input("Do you want to retry the party ? Yes or No : ");

    # We return True or False because the function if called to assign a value to a bool variable that is used for a loop. Depending on the answer the loop of the game will stop.
    while True:
            if(answer == "No"):
                print("Ok, bye");
                return False;
            elif(answer == "Yes"):
                print("Ok, let's restart then");
                return True;
            else:
                print('We asked you "Yes or No" not "'+answer+'"');
                answer = input('So... do you want to retry "Yes" or "No" ? ');
    
Game: bool = True;
while Game:
      
    # Generating the random number in the range that the player choosed
    while True:
        try:
            price: int = random.randint(AskGameLimit("minimum"),AskGameLimit("maximum"));
            print("Perfect ! Now, let's try to guess the right price");
            break;
        except: 
            print('Hey, the first value must be the lowest one and the second the biggest. Thanks');

    #Tries is an iterator that help us to calculate the score and stop the game if it exceeds 10
    tries: int = 0;
    playing: bool = True;

    #while playing is a loop that doesn't stop until the player hasn't found the Right Price
    while playing:
        
        #We ask the player to enter a number, then compare it with the defined price
        playerChoice:int = tools.AskUnsignedInt();
        playing = CheckPlayerChoice(playerChoice,price,tries);

        tries += 1;
        if(tries >= 10):
            print("You loose !")
            break;
    
    # Calling the function that check if the player still want to play or not
    Game = EndGame();
    
