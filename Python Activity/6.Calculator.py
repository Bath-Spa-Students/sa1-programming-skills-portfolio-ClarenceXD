operation= input("enter (+, -, /, *,): ")                   #BODMAS

num1= float(input("enter first number: "))

num2= float(input("enter second number: "))                  #float allows an interger to have a decimal point

if operation == "+":
    results = (num1 + num2)
elif operation == "-":
    results = (num1 - num2)
elif operation == "*":
    results = (num1 * num2)
elif operation == "/":
    results = (num1 / num2)

    print (f"your answer is {results}")                       #f is used in string to add variables