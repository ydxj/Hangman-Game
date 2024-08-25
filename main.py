import random,os
from Hangman_art import logo,stages
from Hangman_words import word_list

choosing = random.choice(word_list).lower()
#print(choosing)
blancks = False
lives = 7
blanck = []

for i in range(0,len(choosing)):
    blanck.append("_")
while blancks == False :
    print(logo)
    print()
    print(f"You have {lives} lives left!")
    print(f"{''.join(blanck)}")
    print()
    print(stages[lives-1])
    gess = input("Gess a letter : ").lower()
    for i in range(0,len(choosing)):
        if gess == choosing[i]:
            #findit = "yes"
            blanck[i] = gess
            
            #print(blanck)
    if gess not in blanck:
        lives -= 1
    os.system('cls')
        
    if lives == 0:
        blancks = True
        print("You lose! Hangman died")
        print(f"The word that we looking for was : {choosing}")

    if "_" not in blanck:
        blancks = True
        print("You win !")
        print(f"The word we searchin for was : {''.join(blanck)}")


