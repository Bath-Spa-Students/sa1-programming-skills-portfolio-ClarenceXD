"""Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.

### Instructions:
1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.

### Advanced Requirement:
Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user if the year is a leap year and adjust the number of days accordingly."""
January = 31
February = 28
March = 31
April = 30
May = 31
June = 30
July = 31
August = 31
September = 30
October = 31
November = 30
December = 31
LFebruary = 29

#List of the months days in variables

months = {  1 : January,                                        #A python Dictonarie is used to store data with key:value in pairs of 2
            2 : February,
            3 : March,
            4 : April,
            5 : May,
            6 : June,
            7 : July,
            8 : August,
            9 : September,
            10 :October,
            11 : November,
            12 : December,
            13 : LFebruary}

while True:                                                             
    try:
        user_input= int(input("input a month 1-12: "))                   #Asks the user for the month  
        if 1 <= user_input <= 12:                                        #checks if the user_input is equal to 1 or 12 and not greater then 12 or less then 1 if the condition is not broken will break out of loop
            break
        else:
            print ("Enter the number of the month from 1 to 12")
    except ValueError:                                                  #if the user does not input a interger will print the following "Enter the number of the month 1-12: " and loop
        print("Enter the number of the month from 1 to 12")


if user_input == 2:                                        #if the month is February ask the user what year it is
    year = int(input("What year is it: "))
    while True:
        year -=4
        if year == 4:
            leapyear= True                                  #if the year is =(equal) to 4 set leapyear to True
            break

        elif year <=0:                                      #if year is <(less) then 4 set leapyear to False
            leapyear= False
            break

    if leapyear == False:                                                           #if leapyear is False will print 28 days (non leap year)
        print(f"It is not a leap year. The days is {months.get(user_input)}.")

    elif leapyear == True:                                                        
        user_input = 13
        print(f"It is a leap year. The days is {months.get(user_input)}.")          #if leapyear is True will print 29 days (leap year)

else:
    print (f"The days is {months.get(user_input)}.")