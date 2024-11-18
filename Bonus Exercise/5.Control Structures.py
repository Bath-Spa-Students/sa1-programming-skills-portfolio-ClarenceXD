print("Sir We have shot down the alien\nThe bets are starting now on what color the alien blood color is\nThey gave us 3 options Red, Green or Yellow.")
user_choice = input("What are you betting on?(R,G,Y): ")

if user_choice.lower() == "g":
    print("You won the bet adding 5 million to your account")

else:
    print("Haha man you lost. The blood was Green")