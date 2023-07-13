#string as input , it is ending with ing, if it is not ending with ing add ing at the end else add ly
# input : string   output : stringly
#input : cook   output:cooking

a = input("Enter Somthing here:")

if a.endswith("ing"):
    b = a + "ly"
else:
    b = a + "ing"

print(b)