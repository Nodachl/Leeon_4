string=input("enter string")
symbol=input("enter character")
counter=0
for char in string:
    if symbol in string:
        counter+=1

print(counter)