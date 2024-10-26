"""Use your newly acquired knowledge of the for loop to complete the following tasks. Print all values to the console in each case.

Write a loop that counts up from 0 to 50 in increments of 1.
Write a loop that counts down from 50 to 0 in decrements of 1.
Write a loop that counts up from 30 to 50 in increments of 1.
Write a loop that counts down from 50 to 10 in decrements of 2.
Write a loop that counts up from 100 to 200 in increments of 5. You may include all loops in a single project"""

choice = int(input("-Type 1 for 0 to 50 in increments of 1 \n-Type 2 for 50 to 0 in decrements of 1 \n-Type 3 for 30 to 50 in increaments of 1 \n-Type 4 for 50 to 10 in decrements of 2 \n-Type 5 for 100 to 200 in increments of 5 \n\nPlease Input your choice: "))

number0 = 0
number50 = 50
number30 = 30
number100 = 100

"""The code checks the choice the user has made and displays the output depending on what the user wants.
The code uses loops to decrease or increase the numbers to the goals of the instructor"""

if choice == 1:                                         #from number0 to 50 increments of 1
    for first in range(50):                             
        number0 +=1
        print (number0)

elif choice == 2:                                       #from number50 to 0 decrements of 1
    for second in range(50):                             
        number50 -=1
        print (number50)

elif choice == 3:                                       #from number30 to 50 increments of 1
    for third in range(20):                            
        number30 +=1
        print (number30)

elif choice == 4:                                       #from number50 to 10 decrements of 2
    for forth in range(20):                             
        number50 -=2
        print (number50)
    
elif choice == 5:                                       #from number100 to 200 increments of 5
    for fifth in range(20):                            
        number100 +=5
        print (number100)


else:
    print("Please Enter a number from 1 to 5")

#This code uses for loops to loop a certain amount of times