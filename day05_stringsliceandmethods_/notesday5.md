# String Slicing

## Length of a String

finding length of a string using len(function)

   fruit = "Mango"
   len1 = len(fruit)
   print("Mango is a", len1, "letter word.")

-> Output: Mango is a 5 letter word.

   rint(fruit[0:4]) = gives output as Mang
   print(fruit[:5]) = assumes the empty field is 0 and gives Mango
   print(fruit[0:-3]) = gives output as Ma

How does negative numbers work??

We can understand it better once we breakdown the function

   print(fruit[0:-3]) = print(fruit[0:len(fruit)-3])

## String Methods

Some cool in built methods we can use to alter and modify the strings


1.) Upper():
    The upper methods converts a string to upper case. A new string is created, the old one remains as it is cus its immutable..


    a = "Lekish"
    print(len(a))
    print(a.upper()) 