letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random
password = []
for letter in range(1, nr_letters + 1):
    password_letter = random.choice(letters)
    password.append(password_letter)

for symbol in range(1, nr_symbols + 1):
    password_symbol = random.choice(symbols)
    password.append(password_symbol)

for number in range(1, nr_numbers + 1):
    password_number = random.choice(numbers)
    password.append(password_number)

print(password)
random.shuffle(password)
final_password = "".join(password)
print(f" Yor password is {final_password}")


