"""In this exercise, you'll create a program that stores and prints your name, hometown, and age to the console using a Python dictionary.
 
### Steps:
1. Store the information (name, hometown, and age) as key-value pairs in a dictionary.
2. Print the values on separate lines using a single `print()` statement.
3. Use variables with appropriate data types for each piece of information.



### Advanced Requirements:
Have the user input their name, hometown, and age instead of hardcoding the values.
Try giving both your first and second name when asked for your name. What happens? How can you handle multiple words in Python?
Test the program by entering a string value for age (e.g., "twenty"). What happens? How can you prevent this issue?"""

username = "Clarence"
userage = 19
usertown = "RAK"

userinfo = {"name" : username,                                      #A python dictionary is used to store the information
            "age" : userage,
            "hometown" : usertown}

print(*userinfo.values(), sep='\n')                                 #prints userinfo with a new line to seperate the output
