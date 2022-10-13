ans = input("What operation would you like to do? (add, modulo, multiply, divide) ") # assigning the answer to the variable ans
num1 = int(input("Pick your first number: ")) # taking user's first num
num2 = int(input("Pick your second number: ")) # taking user's second num

def add(num1, num2):
    return num1 + num2 # created a function that takes two arguments and adds them together


def modulo(num1, num2):
    return num1 % num2 # created a function that takes two arguments and subtracts them


def multiply(num1, num2):
    return num1 * num2 # created a function that takes two arguments and multiplies them together


def divide(num1, num2):
    return num1 / num2 # created a function that takes two arguments and divides them

if ans == "add": # checks the users answer to determine what operation to carry out
    print(add(num1, num2))
elif ans == "modulo":
    print(modulo(num1, num2))
elif ans == "multiply":
    print(multiply(num1, num2))
elif ans == "divide":
    print(divide(num1, num2))
else:
    print("please enter a valid operation!")