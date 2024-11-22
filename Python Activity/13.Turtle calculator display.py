import turtle

"""This code was created for the purpose of me trying new things i wanted to change the turtle movement depending on the userinput
i have learned how to use different turtles and i have made mistakes in my code when creating functions so i took more lines. 
I also wanted to learn about functions this uses around 27 of them"""

t1 = turtle.Turtle()
length = 20                            #120
seperation = 6                         #40
c_h = 500
c_w = 400
d_h = 90
d_w = 345
first_digit = 125
digit_y = 140
b_w = 70
second_digit = first_digit - 45
third_digit = second_digit - 45
forth_digit = third_digit - 45
fifth_digit = forth_digit - 45
sixth_digit = fifth_digit - 45
seventh_digit = sixth_digit - 45
Smol_display_L = 14    
Smol_display_S = 4  
t1.speed(250)
turtle.shape("arrow")
turtle.setup(600, 700)
turtle.speed(250)
def button():
    for x in range (2):                         #button
        turtle.pendown()
        turtle.forward(b_w)
        turtle.right(90)
        turtle.forward(b_w)
        turtle.right(90)
def number8(x,y,seperation,length):  
    t1.penup()            # Raise the pen
    t1.setposition(x, y)         # Move to (X,Y)
    t1.pensize(5)
    t1.pendown()        
    t1.setheading(0)  
    t1.forward(length)      #base
    t1.setheading(45)
    t1.penup()
    t1.forward(seperation)
    t1.pendown()
    t1.setheading(90)
    t1.forward(length)      #bottom right base
    t1.setheading(180-45)
    t1.penup()
    t1.forward(seperation)
    t1.setheading(180)
    t1.pendown()
    t1.forward(length)      #middle base
    t1.setheading(180+45)
    t1.penup()
    t1.forward(seperation)
    t1.setheading(270)
    t1.pendown()
    t1.forward(length)      #bottom left base
    t1.setheading(90)       #traceback
    t1.penup()
    t1.forward(length)
    t1.setheading(45)
    t1.forward(seperation)  #traceback
    t1.setheading(90+45)
    t1.forward(seperation)
    t1.pendown()
    t1.setheading(90)
    t1.forward(length)    #base top left
    t1.penup()
    t1.setheading(45)
    t1.forward(seperation)
    t1.setheading(0)
    t1.pendown()
    t1.forward(length)
    t1.setheading(-45)
    t1.penup()
    t1.forward(seperation)
    t1.pendown()
    t1.setheading(-90)
    t1.forward(length)
def number1(x,y,seperation,length):
    t1.penup()            # Raise the pen
    t1.setposition(x, y)         # Move to (X,Y)
    t1.pensize(5)
    t1.penup()  
    t1.setheading(0)        
    t1.forward(length)      #base
    t1.setheading(45)
    t1.forward(seperation)
    t1.setheading(90)
    t1.pendown()
    t1.forward(length)
    t1.penup()
    t1.setheading(90+45)
    t1.forward(seperation)
    t1.setheading(45)
    t1.forward(seperation)
    t1.setheading(90)
    t1.pendown()
    t1.forward(length)
def number2(x,y,seperation,length):
    t1.penup()            # Raise the pen
    t1.setposition(x + length, y)         # Move to (X,Y)
    t1.pensize(5)
    t1.penup()  
    t1.setheading(180)
    t1.pendown()   
    t1.forward(length)
    t1.setheading (90+45)
    t1.penup()
    t1.forward(seperation)
    t1.setheading(90)
    t1.pendown()
    t1.forward(length)
    t1.setheading(45)
    t1.penup()
    t1.forward(seperation)
    t1.pendown()
    t1.setheading(0)
    t1.forward(length)
    t1.setheading(45)
    t1.penup()
    t1.forward(seperation)
    t1.pendown()
    t1.setheading(90)
    t1.forward(length)
    t1.setheading(90+45)
    t1.penup()
    t1.forward(seperation)
    t1.pendown()
    t1.setheading(180)
    t1.forward(length)
def number3(x,y,seperation,length):
    t1.penup()            # Raise the pen
    t1.setposition(x, y)         # Move to (X,Y)
    t1.pensize(5)
    t1.pendown()
    t1.setheading(0)
    t1.forward(length)
    t1.setheading(45)
    t1.penup()
    t1.forward(seperation)
    t1.setheading(90)
    t1.pendown()
    t1.forward(length)
    t1.penup()
    t1.setheading(90+45)
    t1.forward(seperation)
    t1.setheading(180)
    t1.pendown()
    t1.forward(length)
    t1.setheading(0)            #traceback
    t1.forward(length)          #traceback
    t1.setheading(45)
    t1.penup()
    t1.forward(seperation)
    t1.setheading(90)
    t1.pendown()
    t1.forward(length)
    t1.setheading(90+45)
    t1.penup()
    t1.forward(seperation)
    t1.setheading(180)
    t1.pendown()
    t1.forward(length)
def number4(x,y,seperation,length):
    t1.penup()            # Raise the pen
    t1.setposition(x, y)         # Move to (X,Y)
    t1.pensize(5)
    t1.penup()  
    t1.setheading(0)        
    t1.forward(length)      #base
    t1.setheading(45)
    t1.forward(seperation)
    t1.setheading(90)
    t1.pendown()
    t1.forward(length)
    t1.penup()
    t1.setheading(90+45)
    t1.forward(seperation)
    t1.pendown()
    t1.setheading(180)
    t1.forward(length)
    t1.setheading(0)        #traceback
    t1.forward(length)
    t1.setheading(45)
    t1.penup()
    t1.forward(seperation)
    t1.setheading(90)
    t1.pendown()
    t1.forward(length)
    t1.setheading(-90)
    t1.forward(length)
    t1.setheading(-90-45)
    t1.penup()
    t1.forward(seperation)
    t1.setheading(180)
    t1.forward(length)
    t1.setheading(90+45)
    t1.forward(seperation)
    t1.setheading(90)
    t1.pendown()
    t1.forward(length)
def number5(x,y,seperation,length):
    t1.penup()            # Raise the pen
    t1.setposition(x, y)         # Move to (X,Y)
    t1.pensize(5)
    t1.pendown()  
    t1.setheading(0)        
    t1.forward(length)      #base
    t1.setheading(45)
    t1.penup()
    t1.forward(seperation)
    t1.setheading(90)
    t1.pendown()
    t1.forward(length)
    t1.setheading(90+45)
    t1.penup()
    t1.forward(seperation)
    t1.pendown()
    t1.setheading(180)
    t1.forward(length)
    t1.setheading(90+45)
    t1.penup()
    t1.forward(seperation)
    t1.setheading(90)
    t1.pendown()
    t1.forward(length)
    t1.setheading(45)
    t1.penup()
    t1.forward(seperation)
    t1.setheading(0)
    t1.pendown()
    t1.forward(length)
def number6(x,y,seperation,length):
    t1.penup()            # Raise the pen
    t1.setposition(x, y)         # Move to (X,Y)
    t1.pensize(5)
    t1.pendown()        
    t1.setheading(0)  
    t1.forward(length)      #base
    t1.setheading(45)
    t1.penup()
    t1.forward(seperation)
    t1.pendown()
    t1.setheading(90)
    t1.forward(length)      #bottom right base
    t1.setheading(180-45)
    t1.penup()
    t1.forward(seperation)
    t1.setheading(180)
    t1.pendown()
    t1.forward(length)      #middle base
    t1.setheading(180+45)
    t1.penup()
    t1.forward(seperation)
    t1.setheading(270)
    t1.pendown()
    t1.forward(length)      #bottom left base
    t1.setheading(90)       #traceback
    t1.penup()
    t1.forward(length)
    t1.setheading(45)
    t1.forward(seperation)  #traceback
    t1.setheading(90+45)
    t1.forward(seperation)
    t1.pendown()
    t1.setheading(90)
    t1.forward(length)    #base top left
    t1.penup()
    t1.setheading(45)
    t1.forward(seperation)
    t1.setheading(0)
    t1.pendown()
    t1.forward(length)
def number7(x,y,seperation,length):
    t1.penup()            # Raise the pen
    t1.setposition(x, y)         # Move to (X,Y)
    t1.pensize(5)
    t1.penup()  
    t1.setheading(0)        
    t1.forward(length)      #base
    t1.setheading(45)
    t1.forward(seperation)
    t1.setheading(90)
    t1.pendown()
    t1.forward(length)
    t1.penup()
    t1.setheading(90+45)
    t1.forward(seperation)
    t1.setheading(45)
    t1.forward(seperation)
    t1.setheading(90)
    t1.pendown()
    t1.forward(length)
    t1.setheading(90+45)
    t1.penup()
    t1.forward(seperation)
    t1.pendown()
    t1.setheading(180)
    t1.forward(length)
    t1.penup()
    t1.setheading(180+45)
    t1.forward(seperation)
    t1.pendown()
    t1.setheading(-90)
    t1.forward(length)
def number9(x,y,seperation,length):
    t1.penup()            # Raise the pen
    t1.setposition(x, y)         # Move to (X,Y)
    t1.pensize(5)
    t1.pendown()        
    t1.setheading(0)  
    t1.forward(length)      #base
    t1.setheading(45)
    t1.penup()
    t1.forward(seperation)
    t1.pendown()
    t1.setheading(90)
    t1.forward(length)      #bottom right base
    t1.setheading(180-45)
    t1.penup()
    t1.forward(seperation)
    t1.setheading(180)
    t1.pendown()
    t1.forward(length)      #middle base
    t1.setheading(90+45)
    t1.penup()
    t1.forward(seperation)
    t1.setheading(90)
    t1.pendown()
    t1.forward(length)      #top left base
    t1.penup()
    t1.setheading(90-45)
    t1.forward(seperation)
    t1.setheading(0)
    t1.pendown()
    t1.forward(length)
    t1.setheading(-45)
    t1.penup()
    t1.forward(seperation)
    t1.pendown()
    t1.setheading(-90)
    t1.forward(length)
def number0(x,y,seperation,length):
    t1.penup()            # Raise the pen
    t1.setposition(x, y)         # Move to (X,Y)
    t1.pensize(5)
    t1.pendown()        
    t1.setheading(0)  
    t1.forward(length)      #base
    t1.setheading(45)
    t1.penup()
    t1.forward(seperation)
    t1.pendown()
    t1.setheading(90)
    t1.forward(length)      #bottom right base
    t1.setheading(180-45)
    t1.penup()
    t1.forward(seperation)
    t1.setheading(180)
    t1.penup()
    t1.forward(length)      #middle base
    t1.setheading(180+45)
    t1.forward(seperation)
    t1.setheading(270)
    t1.pendown()
    t1.forward(length)      #bottom left base
    t1.setheading(90)       #traceback
    t1.penup()
    t1.forward(length)
    t1.setheading(45)
    t1.forward(seperation)  #traceback
    t1.setheading(90+45)
    t1.forward(seperation)
    t1.pendown()
    t1.setheading(90)
    t1.forward(length)    #base top left
    t1.penup()
    t1.setheading(45)
    t1.forward(seperation)
    t1.setheading(0)
    t1.pendown()
    t1.forward(length)
    t1.setheading(-45)
    t1.penup()
    t1.forward(seperation)
    t1.pendown()
    t1.setheading(-90)
    t1.forward(length)
def number8_d(x,y,Smol_display_S,Smol_display_L):  
    turtle.penup()            # Raise the pen
    turtle.setposition(x, y)         # Move to (X,Y)
    turtle.pensize(5)
    turtle.pendown()        
    turtle.setheading(0)  
    turtle.forward(Smol_display_L)      #base
    turtle.setheading(45)
    turtle.penup()
    turtle.forward(Smol_display_S)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(Smol_display_L)      #bottom right base
    turtle.setheading(180-45)
    turtle.penup()
    turtle.forward(Smol_display_S)
    turtle.setheading(180)
    turtle.pendown()
    turtle.forward(Smol_display_L)      #middle base
    turtle.setheading(180+45)
    turtle.penup()
    turtle.forward(Smol_display_S)
    turtle.setheading(270)
    turtle.pendown()
    turtle.forward(Smol_display_L)      #bottom left base
    turtle.setheading(90)       #traceback
    turtle.penup()
    turtle.forward(Smol_display_L)
    turtle.setheading(45)
    turtle.forward(Smol_display_S)  #traceback
    turtle.setheading(90+45)
    turtle.forward(Smol_display_S)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(Smol_display_L)    #base top left
    turtle.penup()
    turtle.setheading(45)
    turtle.forward(Smol_display_S)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(Smol_display_L)
    turtle.setheading(-45)
    turtle.penup()
    turtle.forward(Smol_display_S)
    turtle.pendown()
    turtle.setheading(-90)
    turtle.forward(Smol_display_L)
def number1_d(x,y,Smol_display_S,Smol_display_L):
    turtle.penup()            # Raise the pen
    turtle.setposition(x, y)         # Move to (X,Y)
    turtle.pensize(5)
    turtle.penup()  
    turtle.setheading(0)        
    turtle.forward(Smol_display_L)      #base
    turtle.setheading(45)
    turtle.forward(Smol_display_S)
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(Smol_display_L)
    turtle.penup()
    turtle.setheading(90+45)
    turtle.forward(Smol_display_S)
    turtle.setheading(45)
    turtle.forward(Smol_display_S)
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(Smol_display_L)
def number2_d(x,y,Smol_display_S,Smol_display_L):
    turtle.penup()            # Raise the pen
    turtle.setposition(x + Smol_display_L, y)         # Move to (X,Y)
    turtle.pensize(5)
    turtle.penup()  
    turtle.setheading(180)
    turtle.pendown()   
    turtle.forward(Smol_display_L)
    turtle.setheading (90+45)
    turtle.penup()
    turtle.forward(Smol_display_S)
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(Smol_display_L)
    turtle.setheading(45)
    turtle.penup()
    turtle.forward(Smol_display_S)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(Smol_display_L)
    turtle.setheading(45)
    turtle.penup()
    turtle.forward(Smol_display_S)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(Smol_display_L)
    turtle.setheading(90+45)
    turtle.penup()
    turtle.forward(Smol_display_S)
    turtle.pendown()
    turtle.setheading(180)
    turtle.forward(Smol_display_L)
def number3_d(x,y,Smol_display_S,Smol_display_L):
    turtle.penup()            # Raise the pen
    turtle.setposition(x, y)         # Move to (X,Y)
    turtle.pensize(5)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(Smol_display_L)
    turtle.setheading(45)
    turtle.penup()
    turtle.forward(Smol_display_S)
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(Smol_display_L)
    turtle.penup()
    turtle.setheading(90+45)
    turtle.forward(Smol_display_S)
    turtle.setheading(180)
    turtle.pendown()
    turtle.forward(Smol_display_L)
    turtle.setheading(0)            #traceback
    turtle.forward(Smol_display_L)          #traceback
    turtle.setheading(45)
    turtle.penup()
    turtle.forward(Smol_display_S)
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(Smol_display_L)
    turtle.setheading(90+45)
    turtle.penup()
    turtle.forward(Smol_display_S)
    turtle.setheading(180)
    turtle.pendown()
    turtle.forward(Smol_display_L)
def number4_d(x,y,Smol_display_S,Smol_display_L):
    turtle.penup()            # Raise the pen
    turtle.setposition(x, y)         # Move to (X,Y)
    turtle.pensize(5)
    turtle.penup()  
    turtle.setheading(0)        
    turtle.forward(Smol_display_L)      #base
    turtle.setheading(45)
    turtle.forward(Smol_display_S)
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(Smol_display_L)
    turtle.penup()
    turtle.setheading(90+45)
    turtle.forward(Smol_display_S)
    turtle.pendown()
    turtle.setheading(180)
    turtle.forward(Smol_display_L)
    turtle.setheading(0)        #traceback
    turtle.forward(Smol_display_L)
    turtle.setheading(45)
    turtle.penup()
    turtle.forward(Smol_display_S)
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(Smol_display_L)
    turtle.setheading(-90)
    turtle.forward(Smol_display_L)
    turtle.setheading(-90-45)
    turtle.penup()
    turtle.forward(Smol_display_S)
    turtle.setheading(180)
    turtle.forward(Smol_display_L)
    turtle.setheading(90+45)
    turtle.forward(Smol_display_S)
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(Smol_display_L)
def number5_d(x,y,Smol_display_S,Smol_display_L):
    turtle.penup()            # Raise the pen
    turtle.setposition(x, y)         # Move to (X,Y)
    turtle.pensize(5)
    turtle.pendown()  
    turtle.setheading(0)        
    turtle.forward(Smol_display_L)      #base
    turtle.setheading(45)
    turtle.penup()
    turtle.forward(Smol_display_S)
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(Smol_display_L)
    turtle.setheading(90+45)
    turtle.penup()
    turtle.forward(Smol_display_S)
    turtle.pendown()
    turtle.setheading(180)
    turtle.forward(Smol_display_L)
    turtle.setheading(90+45)
    turtle.penup()
    turtle.forward(Smol_display_S)
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(Smol_display_L)
    turtle.setheading(45)
    turtle.penup()
    turtle.forward(Smol_display_S)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(Smol_display_L)
def number6_d(x,y,Smol_display_S,Smol_display_L):
    turtle.penup()            # Raise the pen
    turtle.setposition(x, y)         # Move to (X,Y)
    turtle.pensize(5)
    turtle.pendown()        
    turtle.setheading(0)  
    turtle.forward(Smol_display_L)      #base
    turtle.setheading(45)
    turtle.penup()
    turtle.forward(Smol_display_S)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(Smol_display_L)      #bottom right base
    turtle.setheading(180-45)
    turtle.penup()
    turtle.forward(Smol_display_S)
    turtle.setheading(180)
    turtle.pendown()
    turtle.forward(Smol_display_L)      #middle base
    turtle.setheading(180+45)
    turtle.penup()
    turtle.forward(Smol_display_S)
    turtle.setheading(270)
    turtle.pendown()
    turtle.forward(Smol_display_L)      #bottom left base
    turtle.setheading(90)       #traceback
    turtle.penup()
    turtle.forward(Smol_display_L)
    turtle.setheading(45)
    turtle.forward(Smol_display_S)  #traceback
    turtle.setheading(90+45)
    turtle.forward(Smol_display_S)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(Smol_display_L)    #base top left
    turtle.penup()
    turtle.setheading(45)
    turtle.forward(Smol_display_S)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(Smol_display_L)
def number7_d(x,y,Smol_display_S,Smol_display_L):
    turtle.penup()            # Raise the pen
    turtle.setposition(x, y)         # Move to (X,Y)
    turtle.pensize(5)
    turtle.penup()  
    turtle.setheading(0)        
    turtle.forward(Smol_display_L)      #base
    turtle.setheading(45)
    turtle.forward(Smol_display_S)
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(Smol_display_L)
    turtle.penup()
    turtle.setheading(90+45)
    turtle.forward(Smol_display_S)
    turtle.setheading(45)
    turtle.forward(Smol_display_S)
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(Smol_display_L)
    turtle.setheading(90+45)
    turtle.penup()
    turtle.forward(Smol_display_S)
    turtle.pendown()
    turtle.setheading(180)
    turtle.forward(Smol_display_L)
    turtle.penup()
    turtle.setheading(180+45)
    turtle.forward(Smol_display_S)
    turtle.pendown()
    turtle.setheading(-90)
    turtle.forward(Smol_display_L)
def number9_d(x,y,Smol_display_S,Smol_display_L):
    turtle.penup()            # Raise the pen
    turtle.setposition(x, y)         # Move to (X,Y)
    turtle.pensize(5)
    turtle.pendown()        
    turtle.setheading(0)  
    turtle.forward(Smol_display_L)      #base
    turtle.setheading(45)
    turtle.penup()
    turtle.forward(Smol_display_S)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(Smol_display_L)      #bottom right base
    turtle.setheading(180-45)
    turtle.penup()
    turtle.forward(Smol_display_S)
    turtle.setheading(180)
    turtle.pendown()
    turtle.forward(Smol_display_L)      #middle base
    turtle.setheading(90+45)
    turtle.penup()
    turtle.forward(Smol_display_S)
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(Smol_display_L)      #top left base
    turtle.penup()
    turtle.setheading(90-45)
    turtle.forward(Smol_display_S)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(Smol_display_L)
    turtle.setheading(-45)
    turtle.penup()
    turtle.forward(Smol_display_S)
    turtle.pendown()
    turtle.setheading(-90)
    turtle.forward(Smol_display_L)
def number0_d(x,y,Smol_display_S,Smol_display_L):
    turtle.penup()            # Raise the pen
    turtle.setposition(x, y)         # Move to (X,Y)
    turtle.pensize(5)
    turtle.pendown()        
    turtle.setheading(0)  
    turtle.forward(Smol_display_L)      #base
    turtle.setheading(45)
    turtle.penup()
    turtle.forward(Smol_display_S)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(Smol_display_L)      #bottom right base
    turtle.setheading(180-45)
    turtle.penup()
    turtle.forward(Smol_display_S)
    turtle.setheading(180)
    turtle.penup()
    turtle.forward(Smol_display_L)      #middle base
    turtle.setheading(180+45)
    turtle.forward(Smol_display_S)
    turtle.setheading(270)
    turtle.pendown()
    turtle.forward(Smol_display_L)      #bottom left base
    turtle.setheading(90)       #traceback
    turtle.penup()
    turtle.forward(Smol_display_L)
    turtle.setheading(45)
    turtle.forward(Smol_display_S)  #traceback
    turtle.setheading(90+45)
    turtle.forward(Smol_display_S)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(Smol_display_L)    #base top left
    turtle.penup()
    turtle.setheading(45)
    turtle.forward(Smol_display_S)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(Smol_display_L)
    turtle.setheading(-45)
    turtle.penup()
    turtle.forward(Smol_display_S)
    turtle.pendown()
    turtle.setheading(-90)
    turtle.forward(Smol_display_L)
def add(x,y):
    turtle.penup()            # Raise the pen
    turtle.setposition(x, y)         # Move to (X,Y)
    turtle.pensize(5)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(40)
    turtle.setheading(180)
    turtle.forward(20)
    turtle.setheading(90)
    turtle.forward(20)
    turtle.setheading(-90)
    turtle.forward(40)
def equal(x,y):
    turtle.penup()            # Raise the pen
    turtle.setposition(x, y)         # Move to (X,Y)
    turtle.pensize(5)
    turtle.setheading(90)
    turtle.forward(15)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(30)
    turtle.setheading(-90)
    turtle.penup()
    turtle.forward(30)
    turtle.setheading(180)
    turtle.pendown()
    turtle.forward(30)
def sub(x,y):
    turtle.penup()            # Raise the pen
    turtle.setposition(x, y)         # Move to (X,Y)
    turtle.pensize(5)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(30)
def div(x,y):
    turtle.penup()            # Raise the pen
    turtle.setposition(x, y)         # Move to (X,Y)
    turtle.pensize(5)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(30)
    turtle.setheading(180)
    turtle.forward(15)
    turtle.setheading(90)
    turtle.penup()
    turtle.forward(15)
    turtle.dot(7)
    turtle.setheading(-90)
    turtle.forward(30)
    turtle.dot(7)
def star(x,y):
    turtle.penup()            # Raise the pen
    turtle.setposition(x, y)         # Move to (X,Y)
    turtle.pensize(3)
    turtle.setheading(-90)
    turtle.forward(15)
    turtle.pendown()
    turtle.setheading(75)
    turtle.forward(25)
    turtle.setheading(-75)
    turtle.forward(25)
    turtle.setheading(135)
    turtle.forward(25)
    turtle.setheading(0)
    turtle.forward(25)
    turtle.setheading(220)
    turtle.forward(25)
def design():
    turtle.penup()
    turtle.goto(165,-200)
    button()
    turtle.penup()
    turtle.goto(165,-120)
    button()
    turtle.penup()
    turtle.goto(165,-40)
    button()
    turtle.penup()
    turtle.goto(165,40)
    button()
    turtle.penup()
    turtle.goto(85,-200)
    button()
    turtle.penup()
    turtle.goto(85,-120)
    button()
    turtle.penup()
    turtle.goto(85,-40)
    button()
    turtle.penup()
    turtle.goto(85,40)
    button()
    turtle.penup()
    turtle.goto(5,-200)
    button()
    turtle.penup()
    turtle.goto(5,-120)
    button()
    turtle.penup()
    turtle.goto(5,-40)
    button()
    turtle.penup()
    turtle.goto(5,40)
    button()
    turtle.penup()
    turtle.goto(-75,-120)
    button()
    turtle.penup()
    turtle.goto(-75,-40)
    button()
    turtle.penup()
    turtle.goto(-75,40)
    button()


    add(30,-165) 
    equal(115,-165)        
    sub(115,-85)
    div(115,-5)
    star(125,75)

    number0_d(-35,-185,Smol_display_S,Smol_display_L)                   #0,200

    number1_d(-110,-105,Smol_display_S,Smol_display_L)                   #-75,-120
    number2_d(-35,-105,Smol_display_S,Smol_display_L)                     #0,-120
    number3_d(40,-105,Smol_display_S,Smol_display_L)

    number4_d(-110,-25,Smol_display_S,Smol_display_L)
    number5_d(-35,-25,Smol_display_S,Smol_display_L)
    number6_d(40,-25,Smol_display_S,Smol_display_L)

    number7_d(-110,55,Smol_display_S,Smol_display_L)
    number8_d(-35,55,Smol_display_S,Smol_display_L)
    number9_d(40,55,Smol_display_S,Smol_display_L)
def calculator():
    turtle.penup()
    turtle.goto(-200,-250)
    turtle.setheading(90)
    for x in range (2):
        turtle.pendown()
        turtle.forward(c_h)
        turtle.right(90)
        turtle.forward(c_w)
        turtle.right(90)
    turtle.penup()
    turtle.goto(175,125)                            #    turtle.goto(125,125)
    turtle.setheading(180)
    turtle.pendown()
    for x in range (2):
        turtle.forward(d_w)
        turtle.right(90)
        turtle.forward(d_h)
        turtle.right(90)
    design()
    turtle.penup()
    turtle.goto(900,900)
    num1 = input("Enter the First number: ")
    if (len(num1)) > 0:                         #if total digits more then 0 run code
        if num1[-1] == "1":
            number1(first_digit,digit_y,seperation,length)
        elif num1[-1] == "2":
            number2(first_digit,digit_y,seperation,length)
        elif num1[-1] == "3":
            number3(first_digit,digit_y,seperation,length)
        elif num1[-1] == '4':
            number4(first_digit,digit_y,seperation,length)    
        elif num1[-1] == '5':
            number5(first_digit,digit_y,seperation,length)
        elif num1[-1] == '6':
            number6(first_digit,digit_y,seperation,length)
        elif num1[-1] == '7':
            number7(first_digit,digit_y,seperation,length)
        elif num1[-1] == '8':
            number8(first_digit,digit_y,seperation,length)
        elif num1[-1] == '9':
            number9(first_digit,digit_y,seperation,length)
        elif num1[-1] == '0':
            number0(first_digit,digit_y,seperation,length)
    if (len(num1)) > 1:                     #if total digits more then 1 run code
        if num1[-2] == "1":
            number1(second_digit,digit_y,seperation,length)
        elif num1[-2] == "2":
            number2(second_digit,digit_y,seperation,length)
        elif num1[-2] == "3":
            number3(second_digit,digit_y,seperation,length)
        elif num1[-2] == '4':
            number4(second_digit,digit_y,seperation,length)    
        elif num1[-2] == '5':
            number5(second_digit,digit_y,seperation,length)
        elif num1[-2] == '6':
            number6(second_digit,digit_y,seperation,length)
        elif num1[-2] == '7':
            number7(second_digit,digit_y,seperation,length)
        elif num1[-2] == '8':
            number8(second_digit,digit_y,seperation,length)
        elif num1[-2] == '9':
            number9(second_digit,digit_y,seperation,length)
        elif num1[-2] == '0':
            number0(second_digit,digit_y,seperation,length)
    if (len(num1)) > 2:
        if num1[-3] == "1":
            number1(third_digit,digit_y,seperation,length)
        elif num1[-3] == "2":
            number2(third_digit,digit_y,seperation,length)
        elif num1[-3] == "3":
            number3(third_digit,digit_y,seperation,length)
        elif num1[-3] == '4':
            number4(third_digit,digit_y,seperation,length)    
        elif num1[-3] == '5':
            number5(third_digit,digit_y,seperation,length)
        elif num1[-3] == '6':
            number6(third_digit,digit_y,seperation,length)
        elif num1[-3] == '7':
            number7(third_digit,digit_y,seperation,length)
        elif num1[-3] == '8':
            number8(third_digit,digit_y,seperation,length)
        elif num1[-3] == '9':
            number9(third_digit,digit_y,seperation,length)
        elif num1[-3] == '0':
            number0(third_digit,digit_y,seperation,length)
    if (len(num1)) > 3:
        if num1[-4] == "1":
            number1(forth_digit,digit_y,seperation,length)
        elif num1[-4] == "2":
            number2(forth_digit,digit_y,seperation,length)
        elif num1[-4] == "3":
            number3(forth_digit,digit_y,seperation,length)
        elif num1[-4] == '4':
            number4(forth_digit,digit_y,seperation,length)    
        elif num1[-4] == '5':
            number5(forth_digit,digit_y,seperation,length)
        elif num1[-4] == '6':
            number6(forth_digit,digit_y,seperation,length)
        elif num1[-4] == '7':
            number7(forth_digit,digit_y,seperation,length)
        elif num1[-4] == '8':
            number8(forth_digit,digit_y,seperation,length)
        elif num1[-4] == '9':
            number9(forth_digit,digit_y,seperation,length)
        elif num1[-4] == '0':
            number0(forth_digit,digit_y,seperation,length)
    if (len(num1)) > 4:
        if num1[-5] == "1":
            number1(fifth_digit,digit_y,seperation,length)
        elif num1[-5] == "2":
            number2(fifth_digit,digit_y,seperation,length)
        elif num1[-5] == "3":
            number3(fifth_digit,digit_y,seperation,length)
        elif num1[-5] == '4':
            number4(fifth_digit,digit_y,seperation,length)    
        elif num1[-5] == '5':
            number5(fifth_digit,digit_y,seperation,length)
        elif num1[-5] == '6':
            number6(fifth_digit,digit_y,seperation,length)
        elif num1[-5] == '7':
            number7(fifth_digit,digit_y,seperation,length)
        elif num1[-5] == '8':
            number8(fifth_digit,digit_y,seperation,length)
        elif num1[-5] == '9':
            number9(fifth_digit,digit_y,seperation,length)
        elif num1[-5] == '0':
            number0(fifth_digit,digit_y,seperation,length)
    if (len(num1)) >5:
        if num1[-6] == "1":
            number1(sixth_digit,digit_y,seperation,length)
        elif num1[-6] == "2":
            number2(sixth_digit,digit_y,seperation,length)
        elif num1[-6] == "3":
            number3(sixth_digit,digit_y,seperation,length)
        elif num1[-6] == '4':
            number4(sixth_digit,digit_y,seperation,length)    
        elif num1[-6] == '5':
            number5(sixth_digit,digit_y,seperation,length)
        elif num1[-6] == '6':
            number6(sixth_digit,digit_y,seperation,length)
        elif num1[-6] == '7':
            number7(sixth_digit,digit_y,seperation,length)
        elif num1[-6] == '8':
            number8(sixth_digit,digit_y,seperation,length)
        elif num1[-6] == '9':
            number9(sixth_digit,digit_y,seperation,length)
        elif num1[-6] == '0':
            number0(sixth_digit,digit_y,seperation,length)
    if (len(num1)) > 6:
        if num1[-7] == "1":
            number1(seventh_digit,digit_y,seperation,length)
        elif num1[-7] == "2":
            number2(seventh_digit,digit_y,seperation,length)
        elif num1[-7] == "3":
            number3(seventh_digit,digit_y,seperation,length)
        elif num1[-7] == '4':
            number4(seventh_digit,digit_y,seperation,length)    
        elif num1[-7] == '5':
            number5(seventh_digit,digit_y,seperation,length)
        elif num1[-7] == '6':
            number6(seventh_digit,digit_y,seperation,length)
        elif num1[-7] == '7':
            number7(seventh_digit,digit_y,seperation,length)
        elif num1[-7] == '8':
            number8(seventh_digit,digit_y,seperation,length)
        elif num1[-7] == '9':
            number9(seventh_digit,digit_y,seperation,length)
        elif num1[-7] == '0':
            number0(seventh_digit,digit_y,seperation,length)
    num2 = input("Enter the Second number: ")
    t1.clear()
    if (len(num2)) > 0:                         #if total digits more then 0 run code
        if num2[-1] == "1":
            number1(first_digit,digit_y,seperation,length)
        elif num2[-1] == "2":
            number2(first_digit,digit_y,seperation,length)
        elif num2[-1] == "3":
            number3(first_digit,digit_y,seperation,length)
        elif num2[-1] == '4':
            number4(first_digit,digit_y,seperation,length)    
        elif num2[-1] == '5':
            number5(first_digit,digit_y,seperation,length)
        elif num2[-1] == '6':
            number6(first_digit,digit_y,seperation,length)
        elif num2[-1] == '7':
            number7(first_digit,digit_y,seperation,length)
        elif num2[-1] == '8':
            number8(first_digit,digit_y,seperation,length)
        elif num2[-1] == '9':
            number9(first_digit,digit_y,seperation,length)
        elif num2[-1] == '0':
            number0(first_digit,digit_y,seperation,length)
    if (len(num2)) > 1:                     #if total digits more then 1 run code
        if num2[-2] == "1":
            number1(second_digit,digit_y,seperation,length)
        elif num2[-2] == "2":
            number2(second_digit,digit_y,seperation,length)
        elif num2[-2] == "3":
            number3(second_digit,digit_y,seperation,length)
        elif num2[-2] == '4':
            number4(second_digit,digit_y,seperation,length)    
        elif num2[-2] == '5':
            number5(second_digit,digit_y,seperation,length)
        elif num2[-2] == '6':
            number6(second_digit,digit_y,seperation,length)
        elif num2[-2] == '7':
            number7(second_digit,digit_y,seperation,length)
        elif num2[-2] == '8':
            number8(second_digit,digit_y,seperation,length)
        elif num2[-2] == '9':
            number9(second_digit,digit_y,seperation,length)
        elif num2[-2] == '0':
            number0(second_digit,digit_y,seperation,length)
    if (len(num2)) > 2:
        if num2[-3] == "1":
            number1(third_digit,digit_y,seperation,length)
        elif num2[-3] == "2":
            number2(third_digit,digit_y,seperation,length)
        elif num2[-3] == "3":
            number3(third_digit,digit_y,seperation,length)
        elif num2[-3] == '4':
            number4(third_digit,digit_y,seperation,length)    
        elif num2[-3] == '5':
            number5(third_digit,digit_y,seperation,length)
        elif num2[-3] == '6':
            number6(third_digit,digit_y,seperation,length)
        elif num2[-3] == '7':
            number7(third_digit,digit_y,seperation,length)
        elif num2[-3] == '8':
            number8(third_digit,digit_y,seperation,length)
        elif num2[-3] == '9':
            number9(third_digit,digit_y,seperation,length)
        elif num2[-3] == '0':
            number0(third_digit,digit_y,seperation,length)
    if (len(num2)) > 3:
        if num2[-4] == "1":
            number1(forth_digit,digit_y,seperation,length)
        elif num2[-4] == "2":
            number2(forth_digit,digit_y,seperation,length)
        elif num2[-4] == "3":
            number3(forth_digit,digit_y,seperation,length)
        elif num2[-4] == '4':
            number4(forth_digit,digit_y,seperation,length)    
        elif num2[-4] == '5':
            number5(forth_digit,digit_y,seperation,length)
        elif num2[-4] == '6':
            number6(forth_digit,digit_y,seperation,length)
        elif num2[-4] == '7':
            number7(forth_digit,digit_y,seperation,length)
        elif num2[-4] == '8':
            number8(forth_digit,digit_y,seperation,length)
        elif num2[-4] == '9':
            number9(forth_digit,digit_y,seperation,length)
        elif num2[-4] == '0':
            number0(forth_digit,digit_y,seperation,length)
    if (len(num2)) > 4:
        if num2[-5] == "1":
            number1(fifth_digit,digit_y,seperation,length)
        elif num2[-5] == "2":
            number2(fifth_digit,digit_y,seperation,length)
        elif num2[-5] == "3":
            number3(fifth_digit,digit_y,seperation,length)
        elif num2[-5] == '4':
            number4(fifth_digit,digit_y,seperation,length)    
        elif num2[-5] == '5':
            number5(fifth_digit,digit_y,seperation,length)
        elif num2[-5] == '6':
            number6(fifth_digit,digit_y,seperation,length)
        elif num2[-5] == '7':
            number7(fifth_digit,digit_y,seperation,length)
        elif num2[-5] == '8':
            number8(fifth_digit,digit_y,seperation,length)
        elif num2[-5] == '9':
            number9(fifth_digit,digit_y,seperation,length)
        elif num2[-5] == '0':
            number0(fifth_digit,digit_y,seperation,length)
    if (len(num2)) >5:
        if num2[-6] == "1":
            number1(sixth_digit,digit_y,seperation,length)
        elif num2[-6] == "2":
            number2(sixth_digit,digit_y,seperation,length)
        elif num2[-6] == "3":
            number3(sixth_digit,digit_y,seperation,length)
        elif num2[-6] == '4':
            number4(sixth_digit,digit_y,seperation,length)    
        elif num2[-6] == '5':
            number5(sixth_digit,digit_y,seperation,length)
        elif num2[-6] == '6':
            number6(sixth_digit,digit_y,seperation,length)
        elif num2[-6] == '7':
            number7(sixth_digit,digit_y,seperation,length)
        elif num2[-6] == '8':
            number8(sixth_digit,digit_y,seperation,length)
        elif num2[-6] == '9':
            number9(sixth_digit,digit_y,seperation,length)
        elif num2[-6] == '0':
            number0(sixth_digit,digit_y,seperation,length)
    if (len(num2)) > 6:
        if num2[-7] == "1":
            number1(seventh_digit,digit_y,seperation,length)
        elif num2[-7] == "2":
            number2(seventh_digit,digit_y,seperation,length)
        elif num2[-7] == "3":
            number3(seventh_digit,digit_y,seperation,length)
        elif num2[-7] == '4':
            number4(seventh_digit,digit_y,seperation,length)    
        elif num2[-7] == '5':
            number5(seventh_digit,digit_y,seperation,length)
        elif num2[-7] == '6':
            number6(seventh_digit,digit_y,seperation,length)
        elif num2[-7] == '7':
            number7(seventh_digit,digit_y,seperation,length)
        elif num2[-7] == '8':
            number8(seventh_digit,digit_y,seperation,length)
        elif num2[-7] == '9':
            number9(seventh_digit,digit_y,seperation,length)
        elif num2[-7] == '0':
            number0(seventh_digit,digit_y,seperation,length)

    
    operation= input("enter (+, -, /, *,): ")                   #BODMAS
    if operation == "+":
        results = (int(num1) + int(num2))
    elif operation == "-":
        results = (int(num1) - int(num2))
    elif operation == "*":
        results = (int(num1) * int(num2))
    elif operation == "/":
        (results) = (int(num1) / int(num2))
    t1.clear()
    results = int(results)
    results = str(results)
    if (len(results)) > 0:                         #if total digits more then 0 run code
        if results[-1] == "1":
            number1(first_digit,digit_y,seperation,length)
        elif results[-1] == "2":
            number2(first_digit,digit_y,seperation,length)
        elif results[-1] == "3":
            number3(first_digit,digit_y,seperation,length)
        elif results[-1] == '4':
            number4(first_digit,digit_y,seperation,length)    
        elif results[-1] == '5':
            number5(first_digit,digit_y,seperation,length)
        elif results[-1] == '6':
            number6(first_digit,digit_y,seperation,length)
        elif results[-1] == '7':
            number7(first_digit,digit_y,seperation,length)
        elif results[-1] == '8':
            number8(first_digit,digit_y,seperation,length)
        elif results[-1] == '9':
            number9(first_digit,digit_y,seperation,length)
        elif results[-1] == '0':
            number0(first_digit,digit_y,seperation,length)
    if (len(results)) > 1:                     #if total digits more then 1 run code
        if results[-2] == "1":
            number1(second_digit,digit_y,seperation,length)
        elif results[-2] == "2":
            number2(second_digit,digit_y,seperation,length)
        elif results[-2] == "3":
            number3(second_digit,digit_y,seperation,length)
        elif results[-2] == '4':
            number4(second_digit,digit_y,seperation,length)    
        elif results[-2] == '5':
            number5(second_digit,digit_y,seperation,length)
        elif results[-2] == '6':
            number6(second_digit,digit_y,seperation,length)
        elif results[-2] == '7':
            number7(second_digit,digit_y,seperation,length)
        elif results[-2] == '8':
            number8(second_digit,digit_y,seperation,length)
        elif results[-2] == '9':
            number9(second_digit,digit_y,seperation,length)
        elif results[-2] == '0':
            number0(second_digit,digit_y,seperation,length)
    if (len(results)) > 2:
        if results[-3] == "1":
            number1(third_digit,digit_y,seperation,length)
        elif results[-3] == "2":
            number2(third_digit,digit_y,seperation,length)
        elif results[-3] == "3":
            number3(third_digit,digit_y,seperation,length)
        elif results[-3] == '4':
            number4(third_digit,digit_y,seperation,length)    
        elif results[-3] == '5':
            number5(third_digit,digit_y,seperation,length)
        elif results[-3] == '6':
            number6(third_digit,digit_y,seperation,length)
        elif results[-3] == '7':
            number7(third_digit,digit_y,seperation,length)
        elif results[-3] == '8':
            number8(third_digit,digit_y,seperation,length)
        elif results[-3] == '9':
            number9(third_digit,digit_y,seperation,length)
        elif results[-3] == '0':
            number0(third_digit,digit_y,seperation,length)
    if (len(results)) > 3:
        if results[-4] == "1":
            number1(forth_digit,digit_y,seperation,length)
        elif results[-4] == "2":
            number2(forth_digit,digit_y,seperation,length)
        elif results[-4] == "3":
            number3(forth_digit,digit_y,seperation,length)
        elif results[-4] == '4':
            number4(forth_digit,digit_y,seperation,length)    
        elif results[-4] == '5':
            number5(forth_digit,digit_y,seperation,length)
        elif results[-4] == '6':
            number6(forth_digit,digit_y,seperation,length)
        elif results[-4] == '7':
            number7(forth_digit,digit_y,seperation,length)
        elif results[-4] == '8':
            number8(forth_digit,digit_y,seperation,length)
        elif results[-4] == '9':
            number9(forth_digit,digit_y,seperation,length)
        elif results[-4] == '0':
            number0(forth_digit,digit_y,seperation,length)
    if (len(results)) > 4:
        if results[-5] == "1":
            number1(fifth_digit,digit_y,seperation,length)
        elif results[-5] == "2":
            number2(fifth_digit,digit_y,seperation,length)
        elif results[-5] == "3":
            number3(fifth_digit,digit_y,seperation,length)
        elif results[-5] == '4':
            number4(fifth_digit,digit_y,seperation,length)    
        elif results[-5] == '5':
            number5(fifth_digit,digit_y,seperation,length)
        elif results[-5] == '6':
            number6(fifth_digit,digit_y,seperation,length)
        elif results[-5] == '7':
            number7(fifth_digit,digit_y,seperation,length)
        elif results[-5] == '8':
            number8(fifth_digit,digit_y,seperation,length)
        elif results[-5] == '9':
            number9(fifth_digit,digit_y,seperation,length)
        elif results[-5] == '0':
            number0(fifth_digit,digit_y,seperation,length)
    if (len(results)) >5:
        if results[-6] == "1":
            number1(sixth_digit,digit_y,seperation,length)
        elif results[-6] == "2":
            number2(sixth_digit,digit_y,seperation,length)
        elif results[-6] == "3":
            number3(sixth_digit,digit_y,seperation,length)
        elif results[-6] == '4':
            number4(sixth_digit,digit_y,seperation,length)    
        elif results[-6] == '5':
            number5(sixth_digit,digit_y,seperation,length)
        elif results[-6] == '6':
            number6(sixth_digit,digit_y,seperation,length)
        elif results[-6] == '7':
            number7(sixth_digit,digit_y,seperation,length)
        elif results[-6] == '8':
            number8(sixth_digit,digit_y,seperation,length)
        elif results[-6] == '9':
            number9(sixth_digit,digit_y,seperation,length)
        elif results[-6] == '0':
            number0(sixth_digit,digit_y,seperation,length)
    if (len(results)) > 6:
        if results[-7] == "1":
            number1(seventh_digit,digit_y,seperation,length)
        elif results[-7] == "2":
            number2(seventh_digit,digit_y,seperation,length)
        elif results[-7] == "3":
            number3(seventh_digit,digit_y,seperation,length)
        elif results[-7] == '4':
            number4(seventh_digit,digit_y,seperation,length)    
        elif results[-7] == '5':
            number5(seventh_digit,digit_y,seperation,length)
        elif results[-7] == '6':
            number6(seventh_digit,digit_y,seperation,length)
        elif results[-7] == '7':
            number7(seventh_digit,digit_y,seperation,length)
        elif results[-7] == '8':
            number8(seventh_digit,digit_y,seperation,length)
        elif results[-7] == '9':
            number9(seventh_digit,digit_y,seperation,length)
        elif results[-7] == '0':
            number0(seventh_digit,digit_y,seperation,length)
    print(results)


if True:    
    calculator()


turtle.done()


