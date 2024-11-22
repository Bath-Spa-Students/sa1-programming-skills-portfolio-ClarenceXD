#Check 11.Alphabet cycle print.py for more examples

def this_is_a_function():
    print("I am a print statement inside a function.")
    print("We use functions as a block of code that will run the code when it is called.")

def local_variable():
    cant_be_used_outside = "This variable cannot be called outside the function as it is a local variable\nThis variable cannot be override by a external code"
    print(cant_be_used_outside)

def external_change(name = "Clarence D'Souza"):
    print(name)

external_name = input("Enter your name: ")   
external_name_saved = external_name
"""putting your external variable inside will change the last variable
but not putting a external variable and calling the function will create the code to output Hallo"""
external_name = bool(external_name)

if external_name == False:
    external_change()   
else:
    external_change(external_name_saved)                                                  
print("----------------------------------------------------------------") #sep line
this_is_a_function()
print("----------------------------------------------------------------") #sep line
local_variable()

