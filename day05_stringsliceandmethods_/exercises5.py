name = "Lekish, Podili"

print(name[0:5])

fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")


print(len(name))

print(name[:5])   # python assumes empty is 0

#quick quiz
nm = "Harry"
print(nm[-4:-2])
print(len(nm))
# so total len of char is  5
# 1:2 = ar

str3 = "Hello???????"
print(str3.rstrip("?"))

str4 = "????Hello?????"
print(str4.rstrip("?"))

print(str3.replace("Hello","Hey"))

str5 = "Silver Spoon"
print(str5.split(" "))

say = "hello"
capSay = say.capitalize()
print(capSay)      
say2 = "hello world"
capSay2= say2.capitalize()
print(capSay2)

blogHeading = "Introduction tO priNt"

print(blogHeading.capitalize())


str1 = " Welcome Welcome!!! "
print(str1.center(50, "-"))

a = "aaaaaabbbbcccdddd"
print(a.count("a"))

str1 = " Welcome to the console !!!!"
print(str1.endswith("!!!!"))

str2 = " Welcome to the console 1 !!!!"
print(str2.endswith("!!!!",1,))

str2 = "His name is Dan. He is an honest man."
print(str2.find("is")) 

str3 = "Checking isalnum method "
print(str3.isalnum())

str4 = "test"
print(str4.isalpha())

str1 = "it is small"
print(str1.islower())


str1 = "We wish you a Merry Christmas\n"    
print(str1.isprintable())  

str1 = "   "
print(str1.isspace())