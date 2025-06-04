'''txt = f"The price is 49 dollars"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.1f} dollars"
print(txt)'''


# Operations in f strings
''''
x = float(input("what is your x value?"))
y = f"If {x},y = {x *3}"
print(y)

print("Enter your values and caluclate the area of your triangle!!")
base =  float(input("What is your base value?"))
height = float(input("What is your height value?"))
area = 0.5*base*height
print(f"Area of the triangle is {area}")

'''
'''
#if...else statements in f strings
availableSpaceinGb = 50
gametoplay = f"Space left is{' enough' if availableSpaceinGb>=60 else ' not enough'}"
print(gametoplay)


''' 
'''
## F STRINGS BASED PROBLEMS:

#1.You have a name and an age:
name = "Jamie"
age = 17
Output = f"Your name is {name}, you are {age} years old"
print(Output)

'''
'''
#2 Baking cookies

cookies = 12
Output = f"You baked {12} cookies today!!"
print(Output)

'''
'''
#3. Math with Variables

a = 6
b = 4
Output = f"The product of a and b is {a*b}"
print(Output)

'''
'''
#4. Create a sentence

animal = "dog"
sound = "bark"
Output = f"A {animal} goes {sound}!"
print(Output)
# → Output: A dog goes bark!

'''
'''
#5. Conditional expression inside f-string:

score = 60
Output = f"You {'failed.' if score < 60 else'passed'}"
print(Output)
# → Output: You failed. (if score < 60) or You passed. (if score >= 60)

'''
#6. 
space_left = 45
needed_space = 50
Output = ( f"You have enough space"
if space_left > needed_space
else f"Not enough space. You need {needed_space - space_left} more GB.")
   
# (Hint: Use a conditional f-string that calculates and prints the difference)


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

b = "Lorem ipsum dolor sit amet,consectetur adipiscing elit,sed do eiusmod tempor incididuntut labore et dolore magna aliqua."
print(b)

c = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua. '''

print(c[5])

# so ''' or """ doesnt matter


alphabets = "abcdefghijklmnopqrstuvwxyz"
for character in alphabets:
    print (character)

# Some more problems based on studies

#1 Basic f-strings
name = "Alex"
age = 18

print (f"My name is {name} and I am {age} years old")

#2 Multi line strings

# Create a multi-line string with:
# "Good night!"
# "See you tomorrow."
msg = '''
"Good night!"
"See you tomorrow."         
'''
print(msg)

#3 For loop over string 

# Print each letter in the word "Hi!"
word = "Hi!"
for character in word :
    print (character)

#4 Math inside F-String

apples = 5
price_per_apple = 2
# Use an f-string to print: Total cost is 10 dollars.
print(f"Total cost is {apples*price_per_apple} dollars")

#5 Indexing 

quote = "Python"
# Print the third letter (should be 't')
print(quote[2])

#6 Conditional F-string

battery = 15
# Print "Battery low!" if < 20, else "Battery OK"
print(f"Battery is {'low!' if battery>15 else 'OK'}")

#7 Placeholder with expression 

x = 8
y = 2
# Print: The result is 4.0
print(f"The result is {x/y}")
