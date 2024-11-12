"""In this exercise, you'll create a program that stores and prints your name, hometown, and age to the console using a Python dictionary.
 
### Steps:
1. Store the information (name, hometown, and age) as key-value pairs in a dictionary.
2. Print the values on separate lines using a single `print()` statement.
3. Use variables with appropriate data types for each piece of information.



### Advanced Requirements:
Have the user input their name, hometown, and age instead of hardcoding the values.
Try giving both your first and second name when asked for your name. What happens? How can you handle multiple words in Python?
Test the program by entering a string value for age (e.g., "twenty"). What happens? How can you prevent this issue?"""

username = str(input("Whats your name: "))
userhome = str(input("Whats your hometown: "))             

while True:                                                         #loop code and break if the input is int
    try:
        userage = int(input("Whats your age: "))                   #takes int input or value error will happen
        break
    except ValueError:                                              #print "Type your age in numerical" if a ValueError has happened
        print("Type your age in numerical")

userinfo = {"name" : username,                                      #A python dictionary is used to store the information
            "age" : userage,
            "hometown" : userhome}

print(*userinfo.values(), sep='\n')
