import random
print("-------------------WELCOME to the Word Guessing Game-------------------")
# print("\n select you level:")
easy=["Apple","Pear","Banana","Orange","Mango","Avocado","peach","kiwi","Pomegranate","Watermelon","Strawberry","Guava","Lichi","Papaya","Plum","Cherry","Fig","Melon",""]
medium=["Dragon fruit","Pomegranate","Blueberry","Raspberry","Jackfruit","Olive","Dates","Craneberry","Pumpkin","Custard apple","Persimmon","Pineapple"]
hard=["Doraemon","Dorami","Nobita","Nobisuke","Nanichan","Shinchan","Shizuka","Daisy Duck","Shishimaru","kenichi","Yumeko","Simba","Suneo","Kirmada"]
level=input("Select your level: \n Easy\n Medium\n Hard \n Level--->").strip().lower()
attempt=1


if level=="easy":
    word=random.choice(easy).lower()
    print("\n--------Word is related to FRUIT---------")
elif level=="medium":
    word=random.choice(medium).lower()
    print("\n--------Word is related to FRUIT---------")
elif level=="hard":
    word=random.choice(hard).lower()
    print("\n--------Word is related to CARTOON CHARACTER---------")

else:
    print("Oops! invaliid enter")
    exit()
   
print(f"\nLength of your word is {len(word)}\n")
hint = ["_"] * len(word)

while True:
    guess=input("Enter your guess:").lower()
# ____________________IF THE USER WANT TO QUIT_______________
    if guess=="quit":
        print("Your word is :",word)
        print("THANKYOU.Exiting the program..........")
        exit()

    if guess.lower()==word.lower():
        print(f"Congratulations.You guessed the correct word in your {attempt} attempt.")
        break
    else:
        attempt+=1
# 
    for i in range(len(guess)):
        if guess[i]==word[i]:
            hint[i]=word[i]
    # print("HINT:",hint)
    print("HINT:","".join(hint))

# ____________________________SUGGEST THE FIRST LETTER______________________
    if attempt==8 and "".join(hint) =="_"*len(word):
        # for i in word:
            print("your first letter is:",word[0])
            hint[0]=word[0]


# ____________________If length of guess is not equal to length of word_______________________
    if len(guess) != len(word)and guess!=hint:
        print(f"Length of your word is {len(word)}")


# _____________________If user want hint___________________
    if guess=="hint":
        for i in range(len(word)):
                if hint[i]=="_":
                    hint[i]=word[i]
                    print(f"Your {i+1} letter is {word[i]}")
                    print("HINT:","".join(hint))
                    break

# _____________________________HELP THE USER____________________________________________
    if attempt==15 and guess!=word and hint.count("_")==1:
        pass
    elif attempt==15 and guess!=word:
        help=input("Will I help you(yes/no)").strip().lower()
        if help=="yes":
            for i in range(len(word)):
                if hint[i]=="_":
                    hint[i]=word[i]
                    print(f"Your {i+1} letter is {word[i]}")
                    print("HINT:","".join(hint))
                    break
                else:
                   pass
        else:
            print("All the best.")


# ____________________ASK USER TO QUIT______________
    if attempt==22:
        q=input("Do you want to quit(yes/no)").strip().lower()
        if q=="yes":
            print("Your word is :",word)
            print("THANKYOU.Exiting the program..........")
            exit()
        else:
            continue

print("THANK YOU.For playing word Guessing GAME")
print("HAVE A NICE DAY")
        


