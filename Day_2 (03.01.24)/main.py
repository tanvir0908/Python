# Slicing
# name = "Tanvir Hasan Emon"
# firstName = name[:6]
# lastName = name[7:]
# print("Full name: ",firstName, lastName)
# reverseName = name[::-1]
# print("Full name reverse: ",reverseName)
# totalUrl = "https//www.google.com"
# print(totalUrl[slice(11,-4)])

#---------------------------------------------------------------------------------------

# Conditional statement
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# if age == 24 and name=='Tanvir':
#     print('We are brothers')
# elif age >= 18:
#     print('Now you are a voter')
# elif 10 < age <18:
#     print('You can give vote but it will take some time')
# else:
#     print('You are still a child')

#---------------------------------------------------------------------------------------

# Loops
# While loop
# name = ""
# while name == "":
#     name = input("Enter your name: ")
# print("Hello", name)

# For loop
# import time
# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)
# print("Happy new year")

# Nested for loops
# row = int(input("Enter row number: "))
# column = int(input("Enter column number: "))
# symbol = input("Enter pattern symbol: ")
# for i in range(0,row):
#     for j in range(0, column):
#         print(symbol, end="")
#     print()

#---------------------------------------------------------------------------------------

# Break
# continue -> skips the next iteration of the loop
# pass -> does nothing acts as a placeholder
# name = "Tanvir Hasan Emon"
# for i in name:
#     if(i==" "):
#         continue
#     if(i == 'M' or i=='m'):
#         break
#     print(i)

#---------------------------------------------------------------------------------------

# Lists
# foods = ["fish", "cake", "rice", "fruits"]
# foods.append('tea')
# foods.insert(1, 'Chicken')
# print("popped item: ", foods.pop())
# for i in foods:
#     print(i)

#Array
# numbers = [4,2,5,10,3,30,1,9]
# numbers.sort()
# print(numbers)

# 2d list
# numbers = [[1,2,3],[4,5,6],[7,8,9]]
# for i in range(3):
#     for j in range(3):
#         print(numbers[i][j], end="")
#     print()

#---------------------------------------------------------------------------------------

# Tuples
# student = ("Tanvir Hasan Emon", 24, "tanvirhasan.th157@gmail.com", '011181077')
# if "Tanvir" in student:
#     print('True')
# else:
#     print('False')
# for i in student:
#     print(i)

#---------------------------------------------------------------------------------------

# Set
fruits = {"Orange", "Apple", "Grape","Mango"}
furnitures = {"chair","tabel", "desk"}

# fruits.update(furnitures)
# print(fruits)
# print(furnitures)
# homeFurnitures = fruits.intersection(furnitures)
# print(homeFurnitures)

print("Difference between fruits set and furnitures set: ", fruits.difference(furnitures))
print("Difference between furnitures set and fruits set: ", furnitures.difference(fruits))

