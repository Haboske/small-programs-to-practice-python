import random

# Generating the random number between 1 and 10000
price = random.randint(1,10000)

# tries is no more than an iterator
tries = 0

# announcing to the player that he is playing "the right price"
print("Try to guess the right number in between 1 and 10000, the more you try, the more points you will loose")

# generating a boolean loop that ask the player to enter a number until he finds the right one
while True:
    #number is the variable that we are going to compare with the right price, and the function input ask the player to write the number in the console
    number = int(input())
    #we add 1 everytime the player is trying to guess the right number to further calculate his score
    tries += 1
    #if the number the player entered is less the price
    if number < price:
        #calculate the difference to check if the player is far away from the good price or not
        difference = price - number
        #if far away we announce it
        if difference >= 100:
            print("lot more")
        if difference < 100:
            print("more")
    if number > price:
        difference = number - price
        if difference >= 100:
            print("lot less")
        if difference < 100:
            print("less")
    #if the player find the right price
    if number == price:
        #we display to the player his score after his win.
        print("the right price ! your score is " +str(int(100)-tries))
        #we stop the loop
        break

#announcing that the party is over
print("party over")
