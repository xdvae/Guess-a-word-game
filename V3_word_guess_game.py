# Making guess word game things to do :

# Import the game data dict (contains arrays as key value pairs of name and three hints). 

# Make a greet() function that asks user if they wanna play or not.

# Make a start() function that will start the game details about how the game will go below:

# Start function will pick a random word from a dict of words, get it's length and display an empty underscore equal to the size of the word eg:- (word: elephant , empty line: _ _ _ _ _ _ _ _).

# User will have 10 tries after 2,3 wrong guesses it will show another hint until it tries reach 0, if user guess is right start another function that will show the win or loose screen.

# Use booleans to impliment which hint to show eg:- if (hint_1 == True): show hint else keep it hidden make use of this for 3 hints.
# Note: After every 2-3 answers that are guessed wrong, set one boolean to true otherwise the hint will not show. 

# Make a gameover() function that will take a boolean as parameter if user wins set the parameter to True and send it to the gameover() function to display the winnig screen, else display the loose screen if the boolean is wromg.

# This text below has the text colors as variables without them the code will not work-
RESET = '\033[0m'      # Reset to default
BOLD = '\033[1m'       # Bold
UNDERLINE = '\033[4m'  # Underline

# Foreground colors
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
PURPLE = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
LIME = '\033[92m'
# -----------------------------------------------------------------------------------------------------------------------------

# Step 1:- Importing the database, importing random (for random words), importing os (to use 'cls').
import random
import os
# The data of the game will come from ("Word_data.JSON") File,importing it below.
import json
with open('word_data.json', 'r') as file:
    Words = json.load(file)
#Defining the greet function Everything that shows when game starts is displayed here
def greet():
    os.system("cls")
    input_check = True #Using this to check for correct input set it to True before using
    print(CYAN+"_"* 50)
    print(RED+"Guess"+YELLOW+" the"+ CYAN+" word"+ PURPLE+" game"+RESET+"")
    print("Enter 1 to start game.\n")
    print("Enter 2 to learn how to play.\n")
    print("Enter 3 to exit.")
    print(CYAN+"_"* 50+RESET)
    while True:
        try: #Prevents ValueError's 
            while input_check == True:
                player_inpt = int(input("> "))
                
                if player_inpt == 1 or player_inpt == 2:
                    #print("The code reached here #1") #for testing
                    input_check = False
                    if player_inpt == 1:
                        start()
                    
                    elif player_inpt == 2:
                        how_to_play_display();
                           
                    elif player_inpt == 3:
                        print("Exiting...")
                        
                    break
                
                else:
                    print("Please enter 1 or 2.")
                    continue
            break
        except ValueError:
            print("Please enter 1 or 2.")
        
#Defining the start function all the game code goes in here.
def start():
    os.system("cls")
    random_number = random.randint(0,399)
    word_chosen = Words['name'][random_number]  # Picks random word at a random index.
    word_chosen = word_chosen.lower()           # De-capitalises the word (The data is capitalised).
    word_chosen_len = len(word_chosen)          # Gets the length of the chosen word.
    
    hint_1 = False  # Boolean used to display hint one for the word. 
    hint_2 = False  # Boolean used to display hint two for the word.
    hint_3 = False  # Boolean used to display hint three for the word.
    
    underlined_str = ["_"] * word_chosen_len # This displays the empty underline string equal to the size of the word.
    formatted_underline_str = ' '.join(underlined_str)
    tries = 10      # This is the total number of tries player gets.
    next_hint = 10   # The number that will show next hint every 3rd wrong guess.
    
    while(tries > 0):       # Starts the loop.

        # The code below will check if the empty string input (_ _ _ _) is equal to the answer. If so, it will end the game and consider you a winner.
        underlined_word_nospace = ''.join(underlined_str)   # Needed a string without spaces so im compairing this.
                                                            # Note: (formatted_underline_str) has spaces.
        if(underlined_word_nospace == word_chosen): # Checks if it's equal to the answer.
            win_or_loose = True 
            gameover(win_or_loose, word_chosen) # If so end the game, else continue.
            
        if(tries == 10):    # Sets the hint 1 to True so it shows in the begining of the game.
            hint_1 = True
        if(tries == 7):     # Sets the hint 2 to True so it shows after 3 attempts.
            hint_2 = True   
        if(tries == 4):     # Sets the hint 3 to True so it shows after 6 attempts.
            hint_3 = True 
            
        # The code below is displayed when game starts.    
        print(CYAN+"_"* 50)  
        print(UNDERLINE+"GUESS THE WORD"+RESET)
        print("Length: "+CYAN+str(word_chosen_len)+RESET+"  Tries: "+LIME+str(tries)+RESET)
        print(BOLD+formatted_underline_str)
        
        # Checks for which hints to show.
        if(hint_1 == True):
            print("Hint 1: "+str(Words['hint_1'][random_number])+".\n")
        if(hint_2 == True):
            print("Hint 2: "+str(Words['hint_2'][random_number])+".\n")
        if(hint_3 == True):
            print("Hint 3: "+str(Words['hint_3'][random_number])+".\n")
        print(CYAN+"_"* 50+RESET)
        
        # Managing player input and matching the answer below.
        player_input = input("> ")
        player_input = player_input.lower()
        
        
        if player_input == '': 
            os.system("cls")
            print(RED + "Answer cannot be empty"+RESET)     # Shows error if the input is empty (DOES NOT DEDUCT TRIES).
            
            
        elif (len(player_input) > word_chosen_len):     # Keep this here so it prevents some cheeky people from just entering
            os.system("cls")                            # "abcdefghijklmnopqrstuvwxyz" and seeing the full answer.
            print(RED+"The answer you enter cannot be longer than the word\nNo attempts has been deducted."+RESET)
           
            
        elif(player_input == word_chosen):       # If the answer is correct it will set (win_or_loose) to True
            win_or_loose = True                  # before sending it to the gameover() function.
            gameover(win_or_loose,word_chosen)
            break                              
    
    
        elif(player_input != word_chosen):      # If the answer is not True it will :- 
            tries -= 1      # 1. Deduct a try (attempt).
            next_hint -=1   # 2. Deduct a value from next hint.
            
# The code below is used to see which letters are present in the input And in answer. Then, it will change the empty
# underline (_ _ _ _ _) to that letter if it is present eg:- (Word: "pizza", input: "people", new underline_str: "P _ _ _ _" ).

            for i in player_input:      # Using for-loop to go through each letter of the input
                input_letter = i
                index = 0
                
                while (index < word_chosen_len):    # Using while loop to go through each letter of the answer (index).
                    if(input_letter == word_chosen[index]):     # If it matches, change the underlined str to the letter at 
                        underlined_str[index] = input_letter    # that index.
                        formatted_underline_str = ' '.join(underlined_str)
                        index += 1                              # index += 1, so it moves forward even if finds a match.
                        
                    else:
                        index += 1      # Incase it does not find match just move's the code forward.
            
            os.system("cls") # Clears screen and shows input wrong message.
            print(YELLOW+"The word",player_input,"was not the right word!"+RESET+"\nTry again.\n")
                                
                        
# when player runs out of attemps send the bool to gameover() function to display "Player lost message":                
    if(tries == 0):
        win_or_loose = False
        gameover(win_or_loose, word_chosen)
    
# Defining the gameover function all the code after game ends (win or lose) goes here.
def gameover(win_or_loose, word_chosen): 
    
    if win_or_loose == True: # Plays the win side of the function if player won.
        os.system('cls')     
        print(CYAN+"_"* 50+RESET)                       
        print(BOLD+LIME+"Congrats! You got it right!"+RESET+"\n")
        print("The word was: "+BOLD+UNDERLINE+PURPLE+word_chosen+"."+RESET)
        print("What would you like to do now\n"+GREEN+"1."+RESET+" To"+BOLD+UNDERLINE+" play again.\n"+RESET+RED+"2."+RESET+" To "+BOLD+UNDERLINE+"exit.\n")
        print(CYAN+"_"* 50+RESET)
         
        while True:    # Using 2 while loops, this one is used if player enters some other number other than 1 or 2.   
            while True:     # Make sure they enter a number.
                try:
                    choice = int(input("> "))
                    break
            
                except ValueError:
                    print("Please enter 1 or 2")

            if (choice == 1):       # If user inputs 1, Restart the game.
                start()
                break
                
            elif (choice == 2):     # If user inputs 2, End the program.
                print("Exiting...")
                break
            
            else:                   # If user inputs something else, keep asking.
                print("Please enter 1 or 2")
                continue

       
    elif win_or_loose == False: # Plays the lost side of the function if player lost.
        os.system("cls")
        print("Sorry! you "+RED +"lost."+RESET)
        print("The word was: "+BOLD+UNDERLINE+PURPLE+word_chosen+"."+RESET)
        print("What would you like to do now\n"+GREEN+"1."+RESET+" To"+BOLD+UNDERLINE+" play again.\n"+RESET+RED+"2."+RESET+" To "+BOLD+UNDERLINE+"exit.\n")
        print(CYAN+"_"* 50+RESET)
        while True:    # Using 2 while loops, this one is used if player enters some other number other than 1 or 2.   
            while True:     # Make sure they enter a number.
                try:
                    choice = int(input("> "))
                    break
            
                except ValueError:
                    print("Please enter 1 or 2")

            if (choice == 1):       # If user inputs 1, Restart the game.
                start()
                break
                
            elif (choice == 2):     # If user inputs 2, End the program.
                print("Exiting...")
                break
            
            else:                   # If user inputs something else, keep asking.
                print("Please enter 1 or 2")
                continue

# The code below is displayed when player enter's 2 in the greet section. The code is an overview of the game and tells them how to play.
def how_to_play_display():
    os.system("cls")
    print(CYAN+"_"* 50+RESET)
    print(RED+"Guess"+YELLOW+" the"+ CYAN+" word"+ PURPLE+" game"+RESET+"\n\nHOW TO PLAY:-")   
    print(YELLOW+"\n\n------What will heppen?------ \n"+RESET)
    print("One's you hit "+BOLD+UNDERLINE+LIME+'play'+RESET+" a random word will be chosen from a list of words.\n")
    print(YELLOW+"Your GOAL:"+RESET+" You (player) need to "+BOLD+"guess/complete"+RESET+" the word in 10 tries. If you "+BOLD+"fail"+RESET+" to guess the word or make the word YOU WILL "+RED+"LOOSE.\n"+RESET)
    print(YELLOW+"During Game:"+RESET+UNDERLINE+BOLD+" While playing Every guess you make or Every letter you input gets checked"+RESET+" to see if it exists in the chosen word "+LIME+"(Answer)"+RESET+".\nIf so, that letter or the "+UNDERLINE+BOLD+"letters"+RESET+" in the word "+UNDERLINE+BOLD+"you input will be placed in the empty underscores.\n"+RESET)
    print("------eg------\nWord: '"+BOLD+CYAN+"Apple"+RESET+"' Player input: '"+BOLD+LIME+"Pizza"+RESET+"'.\nSince '"+BOLD+YELLOW+"P"+RESET+"' and '"+BOLD+YELLOW+"A"+RESET+"' both exist in the word '"+BOLD+CYAN+"Apple"+RESET+"' they will be placed on their "+BOLD+UNDERLINE+"index"+RESET+RED+"\n\nOld Underscores:"+RESET+" _ _ _ _ _. \n"+GREEN+"New Underscores:"+RESET+" A P P _ _. ")
    print(CYAN+"_"* 50+RESET)
    input("\n\n----------------Press enter to continue--------------------")
    os.system("cls")
    print(CYAN+"_"* 50+RESET)
    print(YELLOW+"To win:"+RESET+" The player needs to complete the word (finding all letters) "+BOLD+UNDERLINE+"or"+RESET+" completely guess the word in order to win.\nYou will be provided "+CYAN+"hints"+RESET+" after a few wrong attempts that will help you "+LIME+BOLD+"guess"+RESET+" the word, use "+BOLD+UNDERLINE+"logic"+RESET+" or"+BOLD+UNDERLINE+" EYEBALL"+RESET+" it to find the word.")
    
    print("\n\nThis game was made by: "+CYAN+UNDERLINE+BOLD+"vaibhav"+RESET+"\nGithub: "+CYAN+UNDERLINE+BOLD+"xdvae"+RESET)
    print("Have fun playing!\n"+BOLD+UNDERLINE+"Goodluck.\n\n"+RESET)
    print(CYAN+"_"* 50+RESET)
    input("\n\n----------------Press enter to continue--------------------")
    greet()
    
    
greet()