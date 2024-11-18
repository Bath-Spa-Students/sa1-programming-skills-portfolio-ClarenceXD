fav_num = "3"
correct_guess = f"You guessed correct it is {fav_num} because the third alphabet is C the first letter of my name"
message = "Do you know what my favorite number is?"
incorrect_guess = f"You guessed wrong it is {fav_num} because the third alphabet is C the first letter of my name"
print(message)

user_message = input("Try to guess the number: ")

if user_message == fav_num:
    print (correct_guess)

else:
    print(incorrect_guess)