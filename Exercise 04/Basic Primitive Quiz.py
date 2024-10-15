"""In this exercise, you'll create a simple program that asks the user a question, evaluates their answer, and provides feedback.

### Steps:
1. Write a program that asks the user "What is the capital of France?" and waits for their response.
2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
3. If the answer is incorrect, the program should print a message saying the answer is wrong.

### Advanced Requirements:
Ignore Capitalization: Modify your program to accept answers regardless of the capitalization (e.g., "paris", "Paris", and "PaRis" should all be considered correct).
Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries. Provide feedback for each question."""

q1 = input("What is the capital of France?: ")      #question the user what is the capital of France and get the input            

if q1== "Paris":                                        #if the input is Paris will print Correct if not Incorrect
    print ("The capital of France is Paris. Correct")
else:
    print ("The capital of France is Paris. Incorrect")