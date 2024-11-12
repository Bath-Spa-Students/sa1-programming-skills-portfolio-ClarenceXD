while True:                                                         #while true is a loop
    try:
        user_number = int(input("Enter a number and i will tell you if its over or below the number 50 i can guess hehe: "))                   
        break
    except ValueError:                                              #used if an error happenes will run a code and loop back
        print("Trying to dodge the game huh just enter a number o(〃＾▽＾〃)o")

if user_number > 50:
    print("Your number is more then 50")
elif user_number == 50:
    print("Your number is equal to 50")
else:
    print("Your number is less then 50")