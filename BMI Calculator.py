#BMI Body mass index:
#BMI build using the input(), Variable,Math operation and type casting

#input() and varible:
height = input("Enter your height M : \n")
weight = input("Enter your weight kg: \n")

bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)