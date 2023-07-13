#String methods:
#len(): Returns the length of a string.
##upper(): Converts all characters in a string to uppercase.
#strip(): Removes leading and trailing whitespace from a string.
#replace(): Replaces one substring in a string with another substring.
#split(): Splits a string into a list of substrings based on a delimiter.

#len()
string = "Hello, World!" 
length = len(string)                  
print("The length of the string is", length)

#lower()
a = string.lower()    
print("The lowercase string is", a)

#upper()
e = string.upper()    
print("The uppercase string is", e)
#strip()
b = string.strip()
print("The stripped string is", b)

#replace()
c = string.replace("World", "Universe")
print("The new string is", c)

#split()
d = string.split(",")
print("The split string is", d)
