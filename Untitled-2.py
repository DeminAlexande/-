import random
a = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
b = int(input("Введите длину пароля "))
c = " "
for i in range(b):
    c += random.choice(a)
print(c) 