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
july = 31
August = 31
September = 30
October = 31
November = 30
December = 31
LFebruary = 29

#List of the months days in variables

months = {  1 : January,                                        #Python Dictionarie used to store data
            2 : February,
            3 : March,
            4 : April,
            5 : May,
            6 : June,
            7 : july,
            8 : August,
            9 : September,
            10 :October,
            11 : November,
            12 : December,
            13 : LFebruary}

while True:
    try:
        userinput= int(input("input a month 1-12: "))                   #lets the user pick a month depending on the input   
        if 1 <= userinput <= 12:                                        #makes sure the user does not enter a number below 1 or above 12
            break
        else:
            print ("Enter the number of the month 1-12: ")
    except ValueError:                     
        print("Enter the number of the month 1-12: ")


if userinput == 2:                                        #if the month is February ask the user what year it is
    year = int(input("What year is it: "))
    while True:
        year -=4
        if year == 4:
            leapyear= True                                  #if year is = to 4 set leapyear to True
            break

        elif year <=0:                                      #if year is <(less) then 4 set leapyear to False
            leapyear= False
            break

    if leapyear == False:                                   #if leapyear is False will print February(nonleap year)
        print(f"The days is {months.get(userinput)}.")

    elif leapyear == True:                                                        
        userinput = 13
        print(f"It is a leap year days is {months.get(userinput)}.")        #if leapyear is True will print February(leap year)
else:
    print (f"The days is {months.get(userinput)}.")