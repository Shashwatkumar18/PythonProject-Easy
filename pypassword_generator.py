import random

print("Welcome To Python Password Generator!")

num_letters = int(input("\n\nPlease enter the numbers of letter you want in your password? "))
num_symbols = int(input("Please enter the numbers of symbol that you want in your password? "))
num_numbers = int(input("Please enter the numbers of number that you want in your password? "))

letters_list = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]
numbers_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols_list = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "[", "}", "]", ":", ";", "'","<", ",", ">", ".", "/", "?", "|"]

final_letters_selected = ""
final_numbers_selected = ""
final_symbols_selected = ""


for i in range (num_letters):
    final_letters_selected += (random.choice(letters_list))
for j in range (num_symbols):
    final_symbols_selected += (random.choice(symbols_list))
for k in range (num_numbers):
    final_numbers_selected += (random.choice(numbers_list))


print("\n\nHere is a random strong password according to your choices: ", (final_letters_selected+final_symbols_selected+final_numbers_selected))