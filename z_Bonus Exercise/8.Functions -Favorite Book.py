user_book = input("Whats your favorite book: ")
user_compair = user_book                                    #saves the user input into another variable which is turned into a bool
def favortite_book(book = "Toy Story"):
    print(f"One of my favorite books is {book} ")
user_compair = bool(user_compair) 

if user_compair == False:
    favortite_book()

else:
    favortite_book(user_book)