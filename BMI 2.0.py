#BMI(Body mass index) calculation:Using if_else and elif statement
#BMI
#formula bmi=weight/(height/100)**2

print("Check Your Body mass index!")
height = float(input("Enter your height in cm:"))
weight = float(input("Enter your Weight in kg:"))

bmi = round(weight / (height/100) ** 2)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")   
