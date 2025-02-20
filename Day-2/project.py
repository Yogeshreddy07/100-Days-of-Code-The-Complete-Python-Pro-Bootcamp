#Its a tip calculator where it will ask then total bill then tip percentage and how many people to split the bill with
print("Welcome to the tip calculator!")

bill=float(input("What was the total bill? $")) #input for bill amount.

tip=int(input("How much tip would you like to give? 0,10, 12, or 15?"))#input for How much tip would you like to give in percentage.

total_bill=bill+((tip/bill)*100) #bill + the % of tip calculated

print(f"The Total Bill is:{total_bill}") #total bill adding the tip percentage amount

person_split=int(input("How many people to split the bill?"))  #input forHow many people to split the bill

split=total_bill/person_split
print(f"Each person should pay:${round(split,2)}") 

"""
Sample Output 1:
Welcome to the tip calculator!
What was the total bill? $153.45
How much tip would you like to give? 0,10, 12, or 15?0     
The Total Bill is:153.45
How many people to split the bill?5     
Each person should pay:$30.69

Sample Output 1:

"""