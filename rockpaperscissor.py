import random 
comp = random.randint(1,3) 

if comp == 1:
   compturn = "rock"
if comp == 2:
   compturn = "paper"
if comp == 3:
   compturn = "scissors"

you = input("")

if you != "rock" and you != "paper" and you != "scissors":
   print("wrong input please choose one from scissors,rock,paper",you) 


if you == "rock" and compturn == "paper":
      print ("you lost")
if you == "paper" and compturn == "scissors":
      print ("you lost")
if you == "scissors" and compturn == "rock":
      print ("you lost")


if you == "rock" and compturn == "rock":
      print ("tie")
if you == "paper" and compturn == "paper":
      print ("tie")
if you == "scissors" and compturn == "scissors":
      print ("tie")
      


if you == "rock" and compturn == "scissors":
      print ("you won")
if you == "paper" and compturn == "rock":
      print ("you won")
if you == "scissors" and compturn == "paper":
      print ("you won")


print ("computer's choice :" + compturn)
print ("your choice :" + you)