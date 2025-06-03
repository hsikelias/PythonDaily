
'''
a = str("3.14")
b = float(2.8888)
c = b
c = int(c)
print(b)
print (c)

print( b + c)

'''


# Using the type() function to check the data types of variables

'''
print(type(a))
print(type(b))
print(type(c))  

Myvar = 5

x = y = z = "Orange"
print(x)
print(y)
print(z)

list1 = ["book","chair","diamond"]
x, y, z = list1
print(x)
print(y)
print(z)


bookName = input("Enter the book name:")
print(bookName)  '''


# Practice problems

# 1.) Print Your Info
     # Take name, age, and print: Hi {name}, next year you'll be {age+1}
     #(Covers: input, type casting, strings)


name = str(input("Please enter your name"))
age =  int(input("What is your age?"))

print("Hi"+ name,"next year you'll be" , age) 

name = input("Please enter your name: ")
age = int(input("What is your age? "))

print(f"Hi {name}, next year you'll be {age + 1}")




#2.) Escape Practice
# Print:
   # This is line 1\nThis is line 2
   # He said: "Python is fun!"

'''
print("He said : \nPython is fun")
'''

#3.) List Basics
# Create a list of 5 numbers. Print the second and last numbers.


FavEldenRingBosses = ["Maliketh", "Radagon", "Rykard", "Malenia", "Elden beast"]

print(FavEldenRingBosses[0])
print(FavEldenRingBosses[3])
print(FavEldenRingBosses[4])

