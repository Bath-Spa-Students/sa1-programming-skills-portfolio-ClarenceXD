"""Fill in the blanks in the code below so that the function hello() prints "Hello" to the console."""

def hello(name = "guest"):                          #creating a function with the attribute (name = "guest") that prints Hello 
    print(f"Hello {name}")                          

def main():
    hello("Professor")                              #calling the function hello() when main() is called added the attribute Professor to the varible name

if __name__ == "__main__":                          #__name__ is a pyhton variable that is equal to __main__ causing the function to run
    main()
