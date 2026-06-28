import math

number = int(input("Enter any number: "))

result = math.sqrt(number)

print(f"The square root of {number} is", math.sqrt(number))

if math.sqrt(number) %2 == 0:
    print("this is an even number")

else:
    print("This is an odd number")
