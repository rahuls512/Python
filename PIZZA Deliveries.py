#Pizza Order: Using if_else and elif statement

print("Welcome to Pizza Deliveries!")
Size = str(input("What Size Pizza do you want? S,M or L:\n"))
add_pepperoni = str(input("Do you want pepperoni? Y or N:\n"))
extra_cheese = str(input("Do you want extra cheese? Y or N:\n"))
bill = 0

if Size == "S":
    bill += 15
elif Size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if Size == "s":
        bill += 2
    else:
        bill += 3    
    
else:
    bill = 3

if extra_cheese == "Y":
    bill += 1

print(F"Your final bill is ${bill}!")    

