#Salary must be greater then 4000 and the amount of years you have works must be more then 4 years in order to take a load

Salary = int(input("Please input a Salary(number only): "))
Years_Job = int(input("Please input the amount of years you have been working: "))

if Salary > 4000:
    if Years_Job > 4:
        print("You are able to take a loan")

    else:
        print("You must be working for more then 4 years to take a loan")


else:
    print("Your Salary is to low to take a loan")

#A if statement inside another if statement is known as a nested if