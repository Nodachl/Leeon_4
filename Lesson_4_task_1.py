string =input("enter string \t")
digits = 0
letters = 0
for char in string:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

print(f'digits: {digits}, letters: {letters}')
