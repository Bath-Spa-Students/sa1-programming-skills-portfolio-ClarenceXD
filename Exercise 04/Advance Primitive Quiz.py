"""In this exercise, you'll create a simple program that asks the user a question, evaluates their answer, and provides feedback.

### Steps:
1. Write a program that asks the user "What is the capital of France?" and waits for their response.
2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
3. If the answer is incorrect, the program should print a message saying the answer is wrong.

### Advanced Requirements:
Ignore Capitalization: Modify your program to accept answers regardless of the capitalization (e.g., "paris", "Paris", and "PaRis" should all be considered correct).
Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries. Provide feedback for each question."""

counter = 0                                                 #a counter used to keep track on how many answers are correct

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

#converts all user input to lowercase 

q1 = q1.lower()
q2 = q2.lower()
q3 = q3.lower()
q4 = q4.lower()
q5 = q5.lower()
q6 = q6.lower()
q7 = q7.lower()
q8 = q8.lower()
q9 = q9.lower()
q10 = q10.lower()

#checks users inputs on each question each one that is correct adds a 1 to the counter variable

if q1== "paris":
    print ("The capital of France is Paris. Correct")
    counter +=1
else:
    print ("The capital of France is Paris. Incorrect")
    
if q2== "berlin":
    print ("The capital of Germany is Berlin Correct")
    counter +=1
else:
    print ("The capital of Germany is Berlin. Incorrect")

if q3== "rome":
    print ("The capital of Italy is Rome. Correct")
    counter +=1
else:
    print ("The capital of Italy is Rome. Incorrect")

if q4== "madrid":
    print ("The capital of Spainis Madrid. Correct")
    counter +=1
else:
    print ("The capital of Spainis Madrid. Incorrect")
    
if q5== "lisbon":
    print ("The capital of Portugal is Lisbon. Correct")
    counter +=1
else:
    print ("The capital of Portugal is Lisbon. Incorrect")

if q6== "athens":
    print ("The capital of Greece is Athens. Correct")
    counter +=1
else:
    print ("The capital of Greece is Athens. Incorrect")

if q7== "vienna":
    print ("The capital of Austria is Vienna. Correct")
    counter +=1
else:
    print ("The capital of Austria is Vienna. Incorrect")

if q8== "brussels":
    print ("The capital of Belgium is Brussels. Correct")
    counter +=1
else:
    print ("The capital of Belgium is Brussels. Incorrect")

if q9== "amsterdam":
    print ("The capital of Netherlands is Amsterdam. Correct")
    counter +=1
else:
    print ("The capital of Netherlands is Amsterdam. Incorrect")

if q10== "bern":
    print ("The capital of Switzerland is Bern. Correct")
    counter +=1
else:
    print ("The capital of Switzerland is Bern. Incorrect")

print(f"you got {counter} out of 10 capitals correct")      #prints the total amount of correct answers using the counter variable





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
    