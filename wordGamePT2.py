word = "Mississippi"
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
            
            # else:
            #     print("YOU LOSE")

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
            
            # else:
            #     print("YOU LOSE")

else:
    print("YOU LOSE!!")
    

