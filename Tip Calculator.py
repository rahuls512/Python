#Tip Calculator: using input(),print(),variable,math operation,

print("Welcome to the tip calculator!")
bill = float( input("What was the total bill? RS."))
tip = int( input("How much tip would you like to give? "))
people = int( input("how many people to split the bill? "))

#bill_with_tip = tip/100*bill+bill
#print(bill_with_tip)

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person,2)
print(f"Each person shoud pay:${final_amount}")
