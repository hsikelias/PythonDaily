''' First try
print("This is a very cool caluclator, replacing your TI 84 caluclator hehe")
print("Enter your two numbers: ")
a = float(input("Enter number 1: "))
b = float(input("Enter number 2: "))
print("Select an operation :")
print("enter 1 for addition")
print("enter 2 for subtraction")
print("enter 3 for multiplication")
print("enter 4 for division")

operation = int(input("Choose an operation from(1-4): "))

if operation == 1:
    print(a+b)
elif operation ==2:
    print(a-b)
elif operation ==3:
    print(a*b)
elif operation ==4:
    print(a/b)
else:
    print("Make sure you have entered numbers only from 1-4 and dont use a string") 

    '''


print("This is a very cool calculator, replacing your TI-84 calculator hehe")

while True:
    try:
        a = float(input("Enter number 1: "))
        b = float(input("Enter number 2: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    print("\nSelect an operation:")
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")

    try:
        operation = int(input("Choose an operation (1-4): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        continue

    if operation == 1:
        result = a + b
        print(f"Result: {result}")
    elif operation == 2:
        result = a - b
        print(f"Result: {result}")
    elif operation == 3:
        result = a * b
        print(f"Result: {result}")
    elif operation == 4:
        if b == 0:
            print(" Cannot divide by zero!")
            continue
        result = a / b
        print(f"Result: {result}")
    else:
        print("Invalid operation. Please select from 1 to 4.")
        continue

    repeat = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
    if repeat != "yes":
        print("Goodbye!")
        break
