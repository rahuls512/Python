#Variables:
#In Python, a variable is a name that refers to a value.
#You can assign a value to a variable using the assignment operator (=).

name = "Rahul"
print(name)
name = "Sharan"
print(name)

name = input("What is your name? ")
Length = len(name)
print(Length)


#WPA that Switches the values stored in the variable a and B:
#Input:- a=3,b=5
#Output:- a=5,b=3

a = input("a:")
b = input("b:")

c = a
a = b
b = c

print("After Switching the a and b values:")
print("a:"+ a)
print("b:"+ b)