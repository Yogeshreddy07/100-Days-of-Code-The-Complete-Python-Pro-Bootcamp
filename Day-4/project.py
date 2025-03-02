import random
print("Welcome To Rock Paper Scissors Game..")
l1=["Rock","paper","Scissors"]
in1=int(input("What do you? Type 0 for Rock,1 for paper or 2 for Scissors"))
r=random.randint(0,2)
print(f"Your choose:{l1[in1]}")
print(f"Computer choose:{l1[r]}")
if in1==r:
    print("Draw")
elif in1==0 and r==2:
    print("You win")
elif in1==1 and r==0:
    print("You win")
elif in1==2 and r==1:
    print("You win")
elif in1==2 and r==0:
    print("you lose")
elif in1==0 and r==1:
    print("you lose")
elif in1==1 and r==2:
    print("you lose")
else:
    print("Enter valid no.")

