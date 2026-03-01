def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: division by zero" ##Exception: Division by 0
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
from art import logo
print(logo)
number_1 = float(input("Enter the first number: "))
while True:
    for symbol in operations:
        print(symbol)
    sign = str(input("Enter the operation:"))
    while sign not in ["+", "-", "*", "/"]:
        print("Invalid Operation")
        sign = input("Enter the operation: \n + \n - \n * \n / \n")
    number_2 = float(input("Enter the second number: "))
    result = operations[sign](number_1, number_2)
    print(F"Result {number_1} {sign} {number_2} = {result}")
    number_1 = result
    restart = input("Type 'yes' if you want to continue calculation. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        print("\n" * 100)
        break
