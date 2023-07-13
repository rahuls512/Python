name = input("Enter name: ")
marks = float(input("Enter marks: "))

total_marks = 500
total = marks
percentage = (total / total_marks) * 100

if percentage >= 70:
 if percentage >= 60:
    class_name = "Distinction"
else: 
 class_name = "First Class"
    

print("Name:", name)
print("Total marks:", total)
print("Percentage:", percentage)
print("Class:", class_name)

