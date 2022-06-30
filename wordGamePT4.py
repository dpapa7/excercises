from urllib.request import urlopen
import random

#create a list holding words from source
word_list = urlopen("https://raw.githubusercontent.com/dwyl/english-words/master/words.txt").read().decode('utf-8')
word_list = word_list.split('\n')

#select a random word from list
randomNUM = random.randint(0, len(word_list))
word = word_list[randomNUM]
#create list to add used words
UsedWords = []

for word in UsedWords:
    if UsedWords(word) in word_list:
        word_list.remove(UsedWords)
    else:
        break


Guess = " "
count = 7

wins = 0
loses = 0


GameRestart = True

while GameRestart:

    Guess = input("\nenter your guess: ")
    if count  == 0:
        print("YOU LOSE!! \nThe correct word was ", word)
        loses = loses + 1
        print("Your performance so far\nWins: ", wins,"\nLoses: ", loses)
        GameRestart = bool(input("\nThanks for playing, Would you like to play again?\nType something and press enter to restart the game, ONLY press enter to exit"))
        count = 7
        
    
    elif len(Guess) > 1:
            
            if Guess == word:
                print("YOU WIN")
                wins = wins +  1
                print("Your performance so far\nWins: ", wins,"\nLoses: ", loses)
            else:
                print ("try again")
                count = count - 1
                print("Remaining Guesses: ",count)

    else:
            if Guess in word:
                
                for i in range(0,len(word)):
                    
                    if word[i] == Guess:
                        print(word[i], end = "")
                    
                    elif word[i] == " ":
                        print(" ", end = "")

                    else:
                        print("-", end = "")
            
            else:
                print("Wrong Letter, Try again")
                count = count - 1
                print("Remaining Guesses: ",count)
    
    if GameRestart:
        UsedWords.append(word)
    else:
        break    
else:
    print("Thanks for playing")
