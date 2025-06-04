# F STRINGS

- Used to format selected parts of a string,to specify a string as an f-string, simply put an f in front of the string literal, like this:

             txt = f"The price is 49 dollars"
             print(txt) 


# Multi line Strings

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
- Use the """ to create multi strings like this

# For loops
- Simple looping thru string 
alphabets = "abcdefghijklmnopqrstuvwxyz"
for character in alphabets:
    print (character)

- ## Placeholders and Modifiers

To format values in an f-string, add placeholders {}, a placeholder can contain variables, operations, functions, and modifiers to format the value.
      
       # Place holders {}
         price = 59
         txt = f"The price is {price} dollars"
         print(txt)

- Everything inside {} is treated as python code and you can add variables, conditions, math to it.

- not going much deeper with this yet, saving it for later.

- ## Performing operations in f-strings

ex 1: txt = f"The price is {20 * 59} dollars"
      print(txt)

ex 2: price = 59
      tax = 0.25
      txt = f"The price is {price + (price * tax)} dollars"
      print(txt)

- ## Indexing 

String is like an array of Characters. We can access parts of the string using its index whichs starts with 0

Square brackets can be used to access these elements of a string.

print(list[0])