import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# numbers as character
numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','@','$','%', '*']


number_letters = int(input("enter the number of characters in the password"))

number_numbers = int(input("enter the number of number in the password"))

number_symbol = int(input("enter the number of symbols in the password"))

password_list = []
for l in range(0,number_letters):
    password_list.append(random.choice(letters))

for l in range(0,number_numbers):
    password_list.append(random.choice(numbers))

for l in range(0,number_symbol):
    password_list.append(random.choice(symbols))

print(password_list)

#shuffle the characters in the list
random.shuffle(password_list)
print(password_list)

password =""
for char in password_list:
    password += char
print(password)



