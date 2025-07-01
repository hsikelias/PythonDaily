print("Welcome to Tip Caluclator")
print("Caluclate amount in dollars $$ and cents")
TotalBill = float(input("What was the total bill: "))
Tip1 = int(input("How much tip would you like to give?10/20/30?"))
NoOfPeople = int(input("How many people splitting the bill?"))

Tip2 = Tip1/100
TotalBill2 = TotalBill * Tip2
FinalBill =  TotalBill+TotalBill2
SplitBill = FinalBill/NoOfPeople
print("Each person should pay", round(SplitBill,2))

