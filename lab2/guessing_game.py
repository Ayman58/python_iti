"""Word guessing game (hangman)
A list of words will be hardcoded in your program, out of which the interpreter will choose 1 random word.
The user first must input their names
Ask the user to guess any alphabet. If the random word
contains that alphabet, it will be shown as the output(with correct placement)
Else the program will ask you to guess another alphabet.
Give 7 turns maximum to guess the complete word."""
import random
def mygame():
    myls=("ayman","mohammed","ahmed")
    # print(myls)
    ch=random.choice(myls)
    user_name=input("Enter your name ")
    c=0
    while c<8 :
        print(f"chance number:{c+1}")
        c+=1
        gu = input("guess an alphabet")
        for w in myls:
            for char in w:
                if char==gu:
                    print(f"your guess is right-->{w} ")
                    exit()




mygame()