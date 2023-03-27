#Love Calculator: Using if_else and elif statement, logical operation, lower(),count().

#Example:
#name1 = "Rahul"
#name2 = "Sharan"

#T occurs 0 times            L occurs 1 times 
#R occurs 2 times            O occurs 0 times 
#u occurs 1 times            V occurs 0 times 
#E occurs 0 times            E occurs 0 times 
#Total = 3                   Total = 1

# love_score = 31

# Conditions:
# love_score less then 10 or greator than 90,  message:-you go togehter like coke and mentos
# love_scores between 40 and 50,  message:-you are alright together
# otherwise the message will just be their score
 

print("Welcome to the LOVE Calculator!")
name1 = input("What is your name:?\n")
name2 = input("What is their name:?\n")

combine_string = name1 + name2
lower_case_stringn = combine_string.lower()

t = lower_case_stringn.count("t")
r = lower_case_stringn.count("r")
u = lower_case_stringn.count("u")
e = lower_case_stringn.count("e")

true = t+r+u+e

l = lower_case_stringn.count("l")
o = lower_case_stringn.count("o")
v = lower_case_stringn.count("v")
e = lower_case_stringn.count("e")

love = l+o+v+e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score},you go togehter like coke and mentos")
elif (love_score >=40) and (love_score <=50):
    print(f"Your score is {love_score},you are alright together")  
else:
    print(f"Your score is {love_score}")