user_info_name = ("Erlinda Fajardo")
names = user_info_name.split()                           #code was first made to grab input from user
user_age = ("70")

Dictionarie = {"first_name":names[-2], "last_name": names[-1],"age": user_age}     
print(*Dictionarie.values(), sep = '\n')