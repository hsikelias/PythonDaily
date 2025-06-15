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


1. Upper():
    The upper methods converts a string to upper case. A new string is created, the old one remains as it is cus strings are immutable..


    a = "Lekish"
    print(len(a))
    print(a.upper()) 
    Output = LEKISH

2. lower(): 
    
    print(a.lower())
    Output = lekish

3. rstrip():
   this method removes any trailing characters.Example: 

     str3 = "Hello???????"
     print(str3.rstrip("?"))
     Output = Hello

what if 
     str4 = "????Hello?????"
     print(str4.rstrip("?"))
     Output = ????Hello

4. replace():
 replaces all occurences of a string with another string

     print(str3.replace("Hello","Hey"))
     Output = Hey???????

5. split():
  This method splits the given string at the specified instance and returns the seperated strings as list items

     str5 = "Silver Spoon"
     print(str5.split(" "))   #splits the string at the whitespace " "
                              # Output: ['Silver', 'Spoon']

6. capitalize():
  This method turns only the irst character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.

     say = "hello"
     capSay = say.capitalize()
     print(capSay)      
     say2 = "hello world"
     capSay2= say2.capitalize()
     print(capSay2)     #Output: Hello
                                 Hello world

7. Center(): The center() method aligns the string to the center as per the parameters give by the user.

     str1 = "Welcome Welcome!!!"
     print(str1.center(50))

     output:  Welcome Welcome!!! 

   you can also provide paddingcharacter. It will fill the rest of the fill char provided  by the user.  
      
       str1 = " Welcome Welcome!!! "
       print(str1.center(50, "-"))

       Output: --------------- Welcome Welcome!!! ---------------

8. count()
   this method returns the number of times the given values has occurred within the given string.

       a = "aaaaaabbbbcccdddd"
       print(a.count("a"))
       output = 6

9. endswith()
    The endswith() method checks if the string ends with a given value. If yes then return True, else return False.

         str1 = " Welcome to the console !!!!"
         print(str1.endswith("!!!!"))
         Output = True

    We can even also cehck for a value in-between the string by providing start and index positions 

         str2 = " Welcome to the console 1 !!!!"
         print(str2.endswith("!!!!",1, "t"))
         Output = True

10. find(): 
    This method searches for the first occurance of the given value and returns the index where it is present. If given value is absent from the string then returns -1.

         str2 = "His name is Dan. He is an honest man."
         print(str2.find("is"))               
         output = 1

11. index(): Very similar to find() method.. only thing different is that when the given value is not present in the string it just stops running the program. "ValueError : string not found"

12. isalnum(): The isalum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.

        str1 = "WelcomeToTheConsole"
        print(str1.isalnum()) 
        Output = True

13. ialpha(): method returns True only if the entire string consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns false.
     
       str1 = "Welcome"
       print(str1.isalpha())
       Output = True

14. islower(): returns True if all characters in the string are lower case, else False
       str1 = "it is small"
       print(str1.islower())
       Output = True

15. isprintable(): returns True if all the values within the given string are printable, if not, then returns False.

       str1 = "We wish you a Merry Christmas\n"    
       print(str1.isprintable())   
       Output = False

16. isspace(): returns True if the string contains white spaces, else returns False     

       str1 = "Is there a space"
       print(str1.isspace())
       Output = False

       str2 = "   "
       print(str1.isspace())
       Output = True

17. istitle(): returns True only if the first letter of each word of each word of the string is capitalized, else it returns False.

        str1 = " Code For Fun"
        print(str1.istitle())
        Output = True

        str2 = "Code for fun"
        print(str2.istitle())
        Output = False