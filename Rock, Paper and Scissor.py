import random

rps=["rock", "paper", "scissor"]
a = "rock"
b = "paper"
c = "scissor"

a > c
b > a
c > b
win = 0
lose = 0
tie = 0

n = int(input("enter the number of rounds you want : \n"))
for i in range(0,n):
 comp = random.choice(rps)
 user = input("enter your choice (Rock, Paper or Scissor) : ")
 if(user not in rps) :
     print("inalid input")
     print("Restart the Game")
     break
    
 print(f"Computer choice {comp}")
 
 if(comp == a and user == b or comp == b and user == c or comp == c and user == a):
    print("you won")
    win += 1
 elif(comp == b and user == a or comp == c and user == b or comp == a and user == c):  
    print("compurter won")
    lose += 1
 elif(comp == user):
    print("it is a tie")
    tie += 1

print(f"the final results are Win : {win} , Lose : {lose} and Tie : {tie}")