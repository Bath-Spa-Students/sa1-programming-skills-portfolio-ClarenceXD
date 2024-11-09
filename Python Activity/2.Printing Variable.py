#Variable

user_age = 19
user_gender = "Male"
user_familystatus = "Unknown"
user_location = "RAK"
user_position = "Student"
user_hobbys = "playing games"

username = input("Enter Your Name: ")

print (f"""Hello there {username}. How was your day?
{user_gender}
{user_age}
{user_familystatus}
{user_location}
{user_position}
{user_hobbys}""")     

"""adding f before the quotation marks makes it possible to print a variable with other data such as string.
When printing a variable the variable should be contained inside a {}"""