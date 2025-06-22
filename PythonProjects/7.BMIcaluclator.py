print("Welcome to BMI Caluclator")
print("Enter your height(meter) and weight(kilogram) for your BMI")

weight = float(input("Enter your weight in Kilogram: "))
height = float(input("Enter your height in meter: "))
height2 = height*height
BMI = float(weight/height)
print("your BMI is",round(BMI))

