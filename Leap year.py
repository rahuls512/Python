#leap year:Using if_else and elif statement
#normal year has 365,leap year have 366,with an extra day is february
#Example the year 2000
#2000/4=500 (leap)
#2000/100=20 (Not Leap)
#2000/400=5 (Leap)

print("Check leap year!")
year = int(input("which year do you want to check ?"))
if year % 4 == 0:
    if year % 100 ==0:
        if year % 400 ==0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")                    