import tools
import time

def InitiateGameBoard()-> list: # Function that initiate the gameboard

    # Generating the game board depending on the size of the grid set by a constant
    table : list[list[str]] = []
    for y in range(grid_length): # Generating Y axis
        table.append([])
        for x in range(grid_length): # Generating X axis in Y index
            table[y].append('~')
    return table

def UpdateGameBoard(index:list,player:str)-> list: # Function that update the gameboard on the last play
    game_board[index[0]][index[1]] = player 
    return game_board

def PrintGameBoard(): # Function that print the gameboard
    for y in game_board:
        print(y)
    
def AskPlayerToPlay()-> list: # Function that ask the player to play      
    
    # Le joueur joue son tour
    print('Quelle ligne souhaitez vous jouer ? De 1 à '+str(grid_length));
    row:int = (tools.AskUnsignedInt())-1; # We ask for the Y axis to play
    print('Quelle colonne souhaitez vous jouer De 1 à ?'+str(grid_length));
    column:int = (tools.AskUnsignedInt())-1; # We ask for the X axis to play

    while not CheckPlayable([row,column]): # We check if this play is available
        print('Quelle ligne souhaitez vous jouer ?');
        row:int = (tools.AskUnsignedInt())-1;
        print('Quelle colonne souhaitez vous jouer ?');
        column:int = (tools.AskUnsignedInt())-1;

    return [row,column] # We return the Y and X axis selected by the player

def AskCpuToPlay()-> list: # Function that call the cpu to play and choose the best play possible, either to win or to block

    
    cpu_play_block_list = GetPlaysList('O') # We get the list of winning combinations of player1 so we'll be able to block it
    cpu_play_win_list = GetPlaysList('X')   # We get the list of winning combinations of cpu so we'll be able find a winning play

    cpu_play_win_tries:int = 1 # We initiate iterator that will help us to iterate in our play_lists and that increase if the play selected is not available so we don't pick up the same
    cpu_play_block_tries:int = 0 # Quite the same thing but for blocking plays

    cpu_play = CpuGetPlay(cpu_play_win_list,'win') # We first try to find a winning play

    if cpu_play == False : # If not winning play available so
        cpu_play = CpuGetPlay(cpu_play_block_list) # We'll find a blocking play
    
    while not CheckPlayable([cpu_play[0],cpu_play[1]]): # While we don't find an available play
        
        while cpu_play_win_tries <= len(cpu_play_win_list[0]): # We try to find an other winning play
            cpu_play = CpuGetPlay(cpu_play_win_list, 'win',cpu_play_win_tries)
            cpu_play_win_tries +=1
            
        if cpu_play_win_tries > len(cpu_play_win_list[0]): # If we don't find any winning play cpu_play_win_list[0] containing our winning combinations
            
            cpu_play = CpuGetPlay(cpu_play_block_list,'block',cpu_play_block_tries) # We'll then find a blocking combination
            cpu_play_block_tries += 1
    
    # You'll find out that there is no random play, for the simple reason that as soon as the first player made a play, we can't have less than one blocking play available

    return cpu_play # We return the Y and X index of the selected play

def GetPlaysList(player:str)->list: # Function that return a list of plays depending on winning combinations for the asked player
    
    play_list:list=[] 
    # Play list is a table that contain a list of play to prioritize, either to win or to counter
    # this list contains multiple list, where each list contained is a play that contain the y axis, the x axis and the level of priority to play it in a scope from 0 to 2 (2 being the most urgent to play)
    
    prioritised_play_list: list = [[],[],[]]
    # prioritised_play_list is globally the playlist but ordered by priority
    # it contains 3 list, the index 0 contains the most urgent plays...
    
    l:int = 0; # l 
    
    for y in range(grid_length): # I travel thrue all the Y index
        for x in range(grid_length): # I travel thrue all the X index
            # To be honest, this is not optimized, I could have done a list with all the index's of moove played and travel thrue this which would have considerably decreases the amount of iteration (even a lot more if our grid_lenght is enormous)

            l:int = -1
            if game_board[y][x] == player:
                
                # We horizontaly check
                while l<=play_length_count-1:
                    if x+l <= grid_length-1:
                        
                        # We check winning combinations
                        if x+l+1 <= grid_length-1 and x+l-1 >= 0:
                            
                            # If we find a O | ~ | O combination
                            if game_board[y][x+l-1] == player and game_board[y][x+l+1] == player and game_board[y][x+l] == '~':
                                play_list.append([y,x+l,2])
                                
                            # If we find a  O | O | ~ combination
                            elif game_board[y][x+l-1] == player and game_board[y][x+l] == player and game_board[y][x+l+1] == '~':
                                play_list.append([y,x+l+1,2])
                                
                            # If we find a ~ | O | O combination
                            elif game_board[y][x+l-1] == '~' and game_board[y][x+l] == player and game_board[y][x+l+1] == player:
                                play_list.append([y,x+l-1,2])
                            
                        # If we find and alone play
                        if(game_board[y][x+l] == player):    
                            
                            # We suggest O | <X>
                            if x+l+1 <= grid_length-1 and game_board[y][x+l+1] == '~':
                                play_list.append([y,x+l+1,1])
                                
                            # We suggest <X> | O
                            if x+l-1 >= 0 and game_board[y][x+l-1] == '~':
                                play_list.append([y,x+l-1,1])
                        
                    l+=1
                l=0
                
                # We vertically check
                while l<=play_length_count-1: 
                    if y+l <= grid_length-1:
                        
                        # We check winning combinations
                        if y+l+1 <= grid_length-1 and y+l-1 >= 0:
                            
                            # If we find a O | ~ | O vertically
                            if game_board[y+1-1][x] == player and game_board[y+l+1][x] == player and game_board[y+l][x] == '~':
                                play_list.append([y+l,x,2])
                                
                            # If we find a O | O | ~ vertically
                            elif game_board[y+l-1][x] == player and game_board[y+l][x] == player and game_board[y+l+1][x] == '~':
                                play_list.append([y+l+1,x,2])
                                
                            # If we find a ~ | O | O vertically
                            elif game_board[y+l-1][x] == '~' and game_board[y+l][x] == player and game_board[y+l+1][x] == player:
                                play_list.append([y+l-1,x,2])
                            
                        # If we find and alone play
                        if(game_board[y+l][x] == player):    
                            
                            # We suggest O | X vertically
                            if y+l+1 <= grid_length-1 and game_board[y+l+1][x] == '~':
                                play_list.append([y+l+1,x,1])
                                
                            # We suggest X | O vertically
                            if y+l-1 >= 0 and game_board[y+l-1][x] == '~':
                                play_list.append([y+l-1,x,1])
    
                    l+=1  
                l=0
                
                # We diagonally check /
                while l<=play_length_count-1:
                    
                    if x+l <= grid_length-1:
                        
                        # We check winning combinations
                        if x+l+1 <= grid_length-1 and x+l-1 >= 0 and y+l+1 <= grid_length-1 and y+l-1 >= 0:
                            
                            # If we find a O | ~ | O diagonally combination /
                            if game_board[y-l+1][x+l-1] == player and game_board[y-l][x+l] == '~' and game_board[y-l-1][x+l+1] == player:
                                play_list.append([y-l,x+l,2])
                                
                            # If we find a O | O | ~ diagonally combination /
                            elif game_board[y-l+1][x+l-1] == player and game_board[y-l][x+l] == player and game_board[y-l-1][x+l+1] == '~':
                                play_list.append([y-l-1,x+l+1,2])
                                
                            # If we find a ~ | O | O diagonally combination /
                            elif game_board[y-l+1][x+l-1] == '~' and game_board[y-l][x+l] == player and game_board[y-l-1][x+l+1] == player:
                                play_list.append([y-l+1,x+l-1,2])
                        
                    l+=1
                l=0
                
                # We diagonally check \
                while l<=play_length_count-1:
                    
                    if x+l <= grid_length-1:
                        
                        # We check winning combinations
                        if x+l+1 <= grid_length-1 and x+l-1 >= 0 and y+l+1 <= grid_length-1 and y+l-1 >= 0:
                            
                            # If we find a O | ~ | O diagonally combination \
                            if game_board[y+l-1][x+l-1] == player and game_board[y+l][x+l] == '~' and game_board[y+l+1][x+l+1] == player:
                                play_list.append([y+l,x+l,2])
                                
                            # If we find a O | O | ~ diagonally combination \
                            elif game_board[y+l-1][x+l-1] == player and game_board[y+l][x+l] == player and game_board[y+l+1][x+l+1] == '~':
                                play_list.append([y+l+1,x+l+1,2])
                                
                            # If we find a ~ | O | O diagonally combination \
                            elif game_board[y+l-1][x+l-1] == '~' and game_board[y+l][x+l] == player and game_board[y+l+1][x+l+1] == player:
                                play_list.append([y+l-1,x+l-1,2])
                        
                    l+=1
                l=0
            
    # We then order our list by level of priority prioritised_play_list[0] being the most important
    for play in play_list:
        if play[2] >= 2 :
            prioritised_play_list[0].append([play[0],play[1]])
        if play[2] == 1 :
            prioritised_play_list[1].append([play[0],play[1]])
        else :
            prioritised_play_list[2].append([play[0],play[1]])    
                
    return prioritised_play_list
                            
def CpuGetPlay(prioritised_play_list:list,play_type:str='',iterator:int = 0)->list: # Function that ask the cpu to pick a play in the list of winning or blocking combination
    i:int = 0
          
    if play_type == 'win' and iterator == 0: # If we are trying to find a winning play
        
        for play in prioritised_play_list[0]:
            if i >= iterator : # We are being sure this isn't a play that we already suggested
                return [play[0],play[1]]
            else :
                i += 1
        i = 0
    
    if play_type == 'win' and iterator > 1: # We are trying to construct a winning combination, but iterator has to be above 1 because before trying to construct a winning combination we must be sure that there is no winning combination for the player
        
        for play in prioritised_play_list[1]:
            if i >= iterator :
                return [play[0],play[1]]
            else :
                i += 1
        i = 0

        for play in prioritised_play_list[2]:
            if i >= iterator :
                return [play[0],play[1]]
            else :
                i += 1

    if not play_type == 'win' : # We are trying to find a blocking play

        for play in prioritised_play_list[0]:
            if i >= iterator :
                return [play[0],play[1]]
            else :
                i += 1
        i = 0

        for play in prioritised_play_list[1]:
            if i >= iterator :
                return [play[0],play[1]]
            else :
                i += 1
        i = 0
    
        for play in prioritised_play_list[2]:
            if i >= iterator :
                return [play[0],play[1]]
            else :
                i += 1

    return False
             
def CheckPlayable(play:list)-> bool: # Function that check if the play selected isn't already taken on the game board
    try:  
        if game_board[play[0]][play[1]] == '~': # If the play isn't already played
            return True
        else:
            print('\n\nCase injouable, réessayez\n\n')
            return False
    except:
        print('Case injouable, réessayez')
        return False

def CheckWinning(play_list:list, last_play:list, player:str)-> bool: # Function that check if the actual play is a winning one or not
    
    for play in play_list[0]:
        if last_play[0] == play[0] and last_play[1] == play[1]:
            print("JOUEUR "+player+" A GAGNE, FIN DE LA PARTIE")
            gameBoard = UpdateGameBoard(last_play,player)
            PrintGameBoard()
            return True
        
    
        
    return False

Game:bool = True;
while Game: # Loop that loop until the player want to stop

    grid_length: int = 5 # No limit :) (in the limits of your computer's capacities)
    play_length_count: int = 3 # For a fonctionnal IA and winning condition it must be 3. I haven't the time yet to make it works for less or more.
    
    game_board = InitiateGameBoard() # Initiating the gameBoard
    PrintGameBoard() # Printing the gameboard before the game starts
    
    while True : # While the game is not over by a breaking condition

        player1_play:list = AskPlayerToPlay() # Calling the function that ask the player to pick a play
        if CheckWinning(GetPlaysList('O'),player1_play,'O') : # Checking if the player's play is winning
            break
        game_board = UpdateGameBoard(player1_play,'O') # We update the gameboard

        player2_play: list = AskCpuToPlay() # Calling the function that'll generate the best play possible for the cpu either it is to win or to counter the player1
        if CheckWinning(GetPlaysList('X'),player2_play,'X') : # Checking if the cpu's play is winning
            break
        game_board = UpdateGameBoard(player2_play,'X') # We update the gameboard
        
        PrintGameBoard() # We print the gameboard at the end of this round

    Game = tools.EndGame(); # Asking the player if he wants to restart or no

#start = time.time()
#print('timer : ')
#print(time.time() - start)