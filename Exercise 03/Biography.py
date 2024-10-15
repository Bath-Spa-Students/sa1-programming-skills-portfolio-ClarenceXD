username = str(input("Whats your name: "))
userhome = str(input("Whats your hometown: "))             

while True:                                                         #loop code and break if the input is int
    try:
        userage = int(input("Whats your age: "))                   #takes int input or value error will happen
        break
    except ValueError:                                              #print "Type your age in numerical" if a ValueError has happened
        print("Type your age in numerical")

userinfo = {"name" : username,                                      #A python dictionary is used to store the information
            "age" : userage,
            "hometown" : userhome}

print(*userinfo.values(), sep='\n')