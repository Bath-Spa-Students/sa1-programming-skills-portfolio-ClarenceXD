"""This code will keep looping untill a interger is inputed 
if a string was inputed the code will get a ValueError but run print("Type your age in numerical") looping the code"""
while True:                                                         #loop code and break if the input is int
    try:
        userage = int(input("Whats your age: "))                   #takes int input or value error will happen
        break
    except ValueError:                                              #print "Type your age in numerical" if a ValueError has happened
        print("Type your age in numerical")