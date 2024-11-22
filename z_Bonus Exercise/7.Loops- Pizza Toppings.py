toppings = 0

print("What toppings would you like on your pizza we currently have the following")
print("""-Pepperoni 
-Sausage
-Mushrooms
-Onions
-Green peppers
-Extra cheese""")

while toppings < 5:
    user_input = input("Enter the toppings you would like and type stop when you are done: ")
    if user_input.lower() == "sausage":
        print("added Sausage to your pizza")
    elif user_input.lower() == "mushrooms":
        print("added Mushrooms to your pizza")
    elif user_input.lower() == "green peppers":
        print("added Green peppers to your pizza")
    elif user_input.lower() == "extra cheese":
        print("added Extra cheese to your pizza")
    elif user_input.lower() == "onions":
        print("added Onions cheese to your pizza")
    if toppings == 4:
        print("You have reached the maximum amount of toppings")
    toppings +=1
