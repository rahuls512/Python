# Take input from the user
n = int(input("Enter a number: "))

# Initialize the factorial to 1
factorial = 1

# Calculate the factorial using a while loop
while n > 0:
    factorial *= n           #fact=fact*n  
    n -= 1                   # n=n-1

# Print the result
print("Factorial is:", factorial)