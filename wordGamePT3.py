from urllib.request import urlopen
import random

#create a list holding words from source
word_list = urlopen("https://raw.githubusercontent.com/dwyl/english-words/master/words.txt").read().decode('utf-8')
word_list = word_list.split('\n')


#select a random word from list
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

    