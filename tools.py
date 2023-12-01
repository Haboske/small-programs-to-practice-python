# Creating a function that check every character and verify if it is a unsigned integer character 'between 1 to 9'
def CheckUnsignedInt(string: str):
    for character in string:
        if not character.isnumeric():
            return False
    return True;

# Creating a function that is going to ask the player to enter an Unsigned Integer Number
def AskUnsignedInt(): 
    
    stringInput: str = (input('Please enter a number : '));
    
    # And we call the function created just above to check if the input value is only made of unsigned integer characters
    while not CheckUnsignedInt(stringInput):
        stringInput: str = (input('I said enter a number ! Nothing else : '));
    
    return int(stringInput);

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