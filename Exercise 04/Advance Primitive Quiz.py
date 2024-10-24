"""In this exercise, you'll create a simple program that asks the user a question, evaluates their answer, and provides feedback.

### Steps:
1. Write a program that asks the user "What is the capital of France?" and waits for their response.
2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
3. If the answer is incorrect, the program should print a message saying the answer is wrong.

### Advanced Requirements:
Ignore Capitalization: Modify your program to accept answers regardless of the capitalization (e.g., "paris", "Paris", and "PaRis" should all be considered correct).
Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries. Provide feedback for each question."""

counter = 0                                                 #A counter used to keep track on how many answers are correct

#List of the questions the user will be answering

q1 = input("What is the capital of France?: ")
q2 = input("What is the capital of Germany?: ")
q3 = input("What is the capital of Italy?: ")
q4 = input("What is the capital of Spain?: ")
q5 = input("What is the capital of Portugal?: ")
q6 = input("What is the capital of Greece?: ")
q7 = input("What is the capital of Austria?: ")
q8 = input("What is the capital of Belgium?: ")
q9 = input("What is the capital of Netherlands?: ")
q10 =input("What is the capital of Switzerland?: ")

"""checks users inputs on each question each one that is correct adds a 1 to the counter variable
.lower() converts all user input to lowercase allowing the code to not be case sensitive"""

if q1.lower()== "paris":
    print ("\nThe capital of France is Paris. Correct")
    counter +=1                                                         #for every correct answer will add 1 to the counter. Added \n to create a new line after each output
else:
    print ("\nThe capital of France is Paris. Incorrect")
    
if q2.lower()== "berlin":
    print ("\nThe capital of Germany is Berlin Correct")
    counter +=1
else:
    print ("\nThe capital of Germany is Berlin. Incorrect")

if q3.lower()== "rome":
    print ("\nThe capital of Italy is Rome. Correct")
    counter +=1
else:
    print ("\nThe capital of Italy is Rome. Incorrect")

if q4.lower()== "madrid":
    print ("\nThe capital of Spainis Madrid. Correct")
    counter +=1
else:
    print ("\nThe capital of Spainis Madrid. Incorrect")
    
if q5.lower()== "lisbon":
    print ("\nThe capital of Portugal is Lisbon. Correct")
    counter +=1
else:
    print ("\nThe capital of Portugal is Lisbon. Incorrect")

if q6.lower()== "athens":
    print ("\nThe capital of Greece is Athens. Correct")
    counter +=1
else:
    print ("\nThe capital of Greece is Athens. Incorrect")

if q7.lower()== "vienna":
    print ("\nThe capital of Austria is Vienna. Correct")
    counter +=1
else:
    print ("\nThe capital of Austria is Vienna. Incorrect")

if q8.lower()== "brussels":
    print ("\nThe capital of Belgium is Brussels. Correct")
    counter +=1
else:
    print ("\nThe capital of Belgium is Brussels. Incorrect")

if q9.lower()== "amsterdam":
    print ("The capital of Netherlands is Amsterdam. Correct")
    counter +=1
else:
    print ("\nThe capital of Netherlands is Amsterdam. Incorrect")

if q10.lower()== "bern":
    print ("The capital of Switzerland is Bern. Correct")
    counter +=1
else:
    print ("\nThe capital of Switzerland is Bern. Incorrect")

print(f"\nYou got {counter} out of 10 capitals correct")      #prints the total amount of correct answers using the counter variable

""""The answers are the following:
    q1 "Paris",
    q2 "Berlin",
    q3 "Rome",
    q4 "Madrid",
    q5 "Lisbon",
    q6 "Athens",
    q7 "Vienna",
    q8 "Brussels",
    q9 "Amsterdam
    q10 "Bern"""
    