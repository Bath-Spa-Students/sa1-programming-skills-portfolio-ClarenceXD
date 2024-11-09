"""Write a program that searches for a specific string within a list of strings. The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam".

Optional Requirements:
Allow the user to input the search term instead of using a predefined value.
Implement the search functionality based on user input."""

names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]                                                        #names variable in list type
  
user_choice = input("Who would you like to find in the list (Jake, Zac, Ian, Ron, Sam, Dave): ").lower()    #.lower to lower case the user input
#the following code checks the users input, if the input is in the list will print the corresponding output
if user_choice == "sam":                                                                                    
    user_choice = 4
    print("You found",(names[user_choice]))

elif user_choice == "jake":
    user_choice = 0
    print("You found",(names[user_choice]))

elif user_choice == "zac":
    user_choice = 1
    print("You found",(names[user_choice]))

elif user_choice == "ian":
    user_choice = 2
    print("You found",(names[user_choice]))

elif user_choice == "ron":
    user_choice = 3
    print("You found",(names[user_choice]))

elif user_choice == "dave":
    user_choice = 5
    print("You found",(names[user_choice]))
else:
    print("Your choice was not in the list or was misspelled")
