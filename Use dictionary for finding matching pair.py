# define a dictionary with usernames and passwords
users = {
    "Rahul": "password123",
    "Raj": "Admin12345",
    "Rakesh": "123456",
    "Roosu": "abcdefg"
}

# get the username and password from the user
username = input("Enter your username: ")
password = input("Enter your password: ")

# check if the username and password match a pair in the dictionary
if username in users and users[username] == password:
    print("Login successful!")
else:
    print("Login failed.")
