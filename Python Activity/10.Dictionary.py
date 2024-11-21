#Dictionarys are used to store data by creating pairs the left value is the calling value 

dictionary = { "age" :20,
               "name":"Clarence",
               "town": "Rak"}

print(dictionary["age"])                                        #printing the value of "age"
print("--------------------------------------------")
print(dictionary.keys())                                        #prints all the keys(calling values)
print("--------------------------------------------")
print(dictionary)                                               #prints both the keys and value in pairs
print("--------------------------------------------")
print(*dictionary.values(), sep='\n')                           #prints the values with a seperation of new lines
