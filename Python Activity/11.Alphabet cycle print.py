#Title: alphabet cycle print 
User_word = input("Enter 10 lowercase Letters: ")
"""This code using For loops to cycle though the string creating a peaceful changing effect. 
The current max letters the user is able to input is 10
space included as a letter"""

def fun(wewant):
    letters = (len(wewant))
    for F_letter in "abcdefghijklmnopqrstuvwxyz!? ":              #alphabet = 'abcdefghijklmnopqrstuvwxyz'
        if F_letter == wewant[0]:
            print (F_letter)
            if letters == 1:
                exit()
            break
        print (F_letter)
    for S_letter in "abcdefghijklmnopqrstuvwxyz!? ":
        if S_letter == wewant[1]:
            print(f"{F_letter}{S_letter}")
            if letters == 2:
                exit()
            break
        
        print (f"{F_letter}{S_letter}")
    for T_letter in "abcdefghijklmnopqrstuvwxyz!? ":
        if T_letter == wewant[2]:
            print(f"{F_letter}{S_letter}{T_letter}")
            if letters == 3:
                exit()
            break
        print (f"{F_letter}{S_letter}{T_letter}")
    for FO_letter in "abcdefghijklmnopqrstuvwxyz!? ":
        if FO_letter == wewant[3]:
            print(f"{F_letter}{S_letter}{T_letter}{FO_letter}")
            if letters == 4:
                exit()
            break
        print (f"{F_letter}{S_letter}{T_letter}{FO_letter}")
    for Fi_letter in "abcdefghijklmnopqrstuvwxyz!? ":
        if Fi_letter == wewant[4]:
            print(f"{F_letter}{S_letter}{T_letter}{FO_letter}{Fi_letter}")
            if letters == 5:
                exit()
            break
        print (f"{F_letter}{S_letter}{T_letter}{FO_letter}{Fi_letter}")
    for Si_letter in "abcdefghijklmnopqrstuvwxyz!? ":
        if Si_letter == wewant[5]:
            print(f"{F_letter}{S_letter}{T_letter}{FO_letter}{Fi_letter}{Si_letter}")
            if letters == 6:
                exit()
            break
        print (f"{F_letter}{S_letter}{T_letter}{FO_letter}{Fi_letter}{Si_letter}")
    for Sev_letter in "abcdefghijklmnopqrstuvwxyz!? ":
        if Sev_letter == wewant[6]:
            print(f"{F_letter}{S_letter}{T_letter}{FO_letter}{Fi_letter}{Si_letter}{Sev_letter}")
            if letters == 7:
                exit()
            break
        print (f"{F_letter}{S_letter}{T_letter}{FO_letter}{Fi_letter}{Si_letter}{Sev_letter}")
    for E_letter in "abcdefghijklmnopqrstuvwxyz!? ":
        if E_letter == wewant[7]:
            print(f"{F_letter}{S_letter}{T_letter}{FO_letter}{Fi_letter}{Si_letter}{Sev_letter}{E_letter}")
            if letters == 8:
                exit()
            break
        print (f"{F_letter}{S_letter}{T_letter}{FO_letter}{Fi_letter}{Si_letter}{Sev_letter}{E_letter}")
    for Nine_letter in "abcdefghijklmnopqrstuvwxyz!? ":
        if Nine_letter == wewant[8]:
            print(f"{F_letter}{S_letter}{T_letter}{FO_letter}{Fi_letter}{Si_letter}{Sev_letter}{E_letter}{Nine_letter}")
            if letters == 9:
                exit()
            break
        print (f"{F_letter}{S_letter}{T_letter}{FO_letter}{Fi_letter}{Si_letter}{Sev_letter}{E_letter}{Nine_letter}")
    for Ten_letter in "abcdefghijklmnopqrstuvwxyz!? ":
        if Ten_letter == wewant[9]:
            print(f"{F_letter}{S_letter}{T_letter}{FO_letter}{Fi_letter}{Si_letter}{Sev_letter}{E_letter}{Nine_letter}{Ten_letter}")
            if letters >= 10:
                exit()
            break
        print (f"{F_letter}{S_letter}{T_letter}{FO_letter}{Fi_letter}{Si_letter}{Sev_letter}{E_letter}{Nine_letter}{Ten_letter}")
fun(User_word)