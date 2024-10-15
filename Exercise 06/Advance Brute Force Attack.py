"""## Exercise 6: Brute Force Attack - 30 Marks

Write a program that simulates a password entry system. The correct password is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.

### Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
3. Output an appropriate message when the correct password is entered.

### Optional Requirements:

Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining attempts. If the maximum number of attempts is reached, inform the user that the authorities have been alerted."""

password = "12345"                                              #password
attempt = 5                                                     #attempt left 

while True:                                                     #used to loop till either the access is granted or the authorities are alerted
    userinput = input("What is the password: ")
    
    if userinput == "12345":                                    #check if the userinput is = to the passowrd
        print ("Access Granted")
        exit()                                  
    elif attempt == 1:
        print ("Access Denied. Authorities have been alerted.")
        exit()                                                  #using exit() to end the code when authorities are alerted
    else:                                                       #every access denied runs a "attempt -=1" to remove a attempt
        attempt -=1  
        print (f"Access Denied {attempt} left")                