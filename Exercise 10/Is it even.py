"""Write a program that tests if a value is even or odd. Follow the instructions outlined below:

Instructions:
The program should ask the user for a number from within the main function.
The entered number should be passed to a function that determines if the value is even or odd.
The function should return a message indicating whether the number is even or odd.
The message returned by the function should be printed from within the main function."""

user_number = int(input("Input a number to check if its even or odd: "))        #ask for a number to check if its even or odd

def main(user_number):                                                          #function to check the user_number 
    code(user_number)
    if code(user_number) == True:                                                   #user_number is even if true
        print(f"The number {user_number} is Even")

    elif code(user_number) == False:                                                #user_number is odd if false
        print(f"The number {user_number} is Odd")
    
def code(user_number):
    while True:
        user_number -=2                                                             
        if user_number == 0:                                                    #if user_number is == to 0 the number return True
            return True

        elif user_number < 0:                                                   #if user_number is less then 0 the number return False
            return False

main(user_number)                                                               #calls(runs) the function 