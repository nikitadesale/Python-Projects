#fortune cookie game writen in python@nikitadesale really a fun game
import random
print("Your Good Name Please:)__")
n=input()
print(n+" Your fortune cookie says")
fortune = random.randint(1,8)
if fortune == 1:
    print("Good things happen just wait and have Patience")
elif fortune == 2:
    print("Oho, A lovely day you have today")
elif fortune == 3:
    print("The early bird gets the worm.")
elif fortune == 4:
    print("Your intuitions will make yiur day!")
elif fortune == 5:
    print("Now is the time to try something new!")
elif fortune == 6:
    print("Today it is up to you to create a peacefulness you long for")
elif fortune == 7:
    print("You will be hungry again in one hour.")
elif fortune == 8:
    print("Fortune cookies rarely share fortunes.")
print("\nHave a nice day")