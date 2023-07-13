#A Dictionary is a collection of key-value pairs, where each key is unique and maps to a value.
# Dictionaries are mutable and can be modified by adding, removing, or updating key-value pairs.

a={1:'a',2:'b',3:'c',1:'A',2:'B'}
print(a)

i={}
n=int(input("how many records:"))
for j in range(n):
    name=input("Enter name:")
    maths=input("maths marks")
    i[name]=maths
    print(i)
