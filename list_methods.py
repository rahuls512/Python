#List methods:
#append(): adds an item to the end of the list.
#extend(): adds the elements of another list to the end of the current list.
#insert(): inserts an item at a specified position in the list.
#remove(): removes the first occurrence of an item from the list.
#pop(): removes and returns an item at a specified index in the list.
#index(): returns the index of the first occurrence of an item in the list.
#count(): returns the number of times an item appears in the list.
#sort(): sorts the items in the list in ascending order.
#reverse(): reverses the order of the items in the list.

student_name =["rahul","raj","rakesh"]
rolle_number =[10,20,30,40,50]
print(student_name)
print(rolle_number)

#indexing:
print(student_name[0]) #indexing 0,1,2,3
print(student_name[-1]) #indexing -4,-3,-2,-1 

#Delete list names:using the indexing 
print("before deleting", student_name)
del student_name[0]    #indexing position
print("after deleting", student_name)   
student_name.remove("rakesh")
print("after remove", student_name)

#append :add at the end
student_name.append("rahul")
print("after append", student_name)

#insert: insert the value string using indexing
student_name.insert(0,"dhanashree")
print("after inserting", student_name)

#To check lenth of list:
print(len(student_name))
print(len(rolle_number))

#pop operation : last element remove
student_name.pop()
print("after pop", student_name)

student_name.reverse()   #reverse :check after last element remove using pop
print("after reverse", student_name)

#sorted
sorted(student_name)  
print("after sorting", student_name)\

#extend()
student_name.extend("rahul")
print("after extending",student_name)

#count()
student_name.count("")
print("after count",student_name)

#sort()
student_name.sort()
print("after sort",student_name)
