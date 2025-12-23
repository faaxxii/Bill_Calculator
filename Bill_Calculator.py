print("Welcome to Bill Calculator")
bill = float(input("What is the total bill?: "))
tip = float(input("What is the tip amount?: "))
tip = tip / 100
totalTip = tip * bill
totalBill = bill + totalTip
people = int(input("How many people would you like to pay?: "))
totalPay = totalBill / people
print("Each person should pay: "+ str(round(totalPay, 2)))
