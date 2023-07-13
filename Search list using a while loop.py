my_list = [1, 3, 5, 7, 9]

# search for the value 5 in the list using a while loop
i = 0
while i < len(my_list):
    if my_list[i] == 5:
        print("Found 5 at index", i)
        break
    i += 1
else:
    print("5 not found in the list")