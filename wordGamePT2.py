
from urllib.request import urlopen
import random

#reference word file
# f = open("words.txt", "r")
# word = []

# with open ("words.txt", "r") as file:
#     allText = file.read()
#     words = list(map(str,allText.split())) 

# #count number of lines in word file
# for lineCount, line in enumerate (f):
#     pass
# lineCount + 1

word_list = urlopen("https://raw.githubusercontent.com/dwyl/english-words/master/words.txt").read().decode('utf-8')
word_list = word_list.split('\n')


#select a random word from file
randomNUM = random.randint(0, len(word_list))
word = word_list[randomNUM]


Guess = " "
count = 7


while count > 0 :
    Guess = input("\nenter your guess: ")
    if count == 0:
        break
    
    elif len(Guess) > 1:
            
            if Guess == word:
                print("YOU WIN")
            
            else:
                print ("try again")
                count = count - 1
                print(count)

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
                print(count)
else:
    print("YOU LOSE!! \nThe correct word was ", word)

    