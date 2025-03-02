print("Welcome ToTreasure Island.\nYour mission is to find the treasure.")
in1=input("You are at a crossroad.\nWhere do you want to go?\n     Type left[l] or right[r]").lower()
if in1=="l":
    in2=input("You have come to lake.Thare is an island in middle of lake.\n     Type 'swim[s]' to swin across or 'wait[w]'to wait for boat").lower()
    if in2=="w":
        in3=input("You arrive at island unharmed.There are 3 door.\n     Type which door you choose Red[r],Yellow[y],Blue[b]").lower()
        if in3=="y":
            print("Congratulations,You found treasure.You Win!!")
        elif in3=="r":
            print("You enter a room of beasts. Game Over!")
        elif in3=="b":
            print("It's room full of fire. Game Over!")
    elif in2=="s":
        print("You are Killed by shark. Game Over!")
    else:
        print("Enter valid input") 
elif in1=="r":
    print("You fall into a hole. Game Over!")     
else:
    print("Enter valid input") 

"""
#--> Sample Outputs:
#------------------------->1
Welcome ToTreasure Island.
Your mission is to find the treasure.
You are at a crossroad.
Where do you want to go?
     Type left[l] or right[r]l
You have come to lake.Thare is an island in middle of lake.
     Type 'swim[s]' to swin across or 'wait[w]'to wait for boatw
You arrive at island unharmed.There are 3 door.
     Type which door you choose Red[r],Yellow[y],Blue[b]y
Congratulations,You found treasure.You Win!!

#------------------------->2
Welcome ToTreasure Island.
Your mission is to find the treasure.
You are at a crossroad.
Where do you want to go?
     Type left[l] or right[r]r
You fall into a hole. Game Over!

#------------------------->3
Welcome ToTreasure Island.
Your mission is to find the treasure.
You are at a crossroad.
Where do you want to go?
     Type left[l] or right[r]l
You have come to lake.Thare is an island in middle of lake.
     Type 'swim[s]' to swin across or 'wait[w]'to wait for boats
You are Killed by shark. Game Over!

->> Try the Game for more outputs...
""" 


