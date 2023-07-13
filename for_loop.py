#A for loop is a programming construct used to iterate or loop over a set of values or a sequence of 
#code statements. The for loop is particularly useful 
#when you know the number of iterations you want to perform or the range of values you want to iterate over.

## for variable in range:     # code to be executed in each iteration
#Here, variable is a variable that takes on each value in the range of values.
# The code inside the for loop is executed once for each value of variable in the range


for num in range(1,11):    #start=1 #end >11 , end=10
    print(num)

for i in range(2,11,2):  #start=2 #end >11, end=10, step=2
    print(i)   

#list numbers with for loop and indexing numbers
a =[11,12,13,14,15,16]
for index,j in enumerate(a):
    print(index,j)    