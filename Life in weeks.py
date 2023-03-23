#life in weeks: using f-string,Number manipulation,math operation
#Input() age
age = int(input("Enter Your Current age?\n"))


#mathematical operation
years_remaining = 90-age
months_remaining = years_remaining*12
weeks_remaining = years_remaining*52
days_remaining = years_remaining*365


# usning f-string
message = f"You have {days_remaining} days,{weeks_remaining} weeks,and {months_remaining} months left"
#print the message
print(message)