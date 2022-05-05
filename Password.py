import random

list1 = list("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890")
list2 = list("#$%^&*():|/''AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz")
list3 = list("#$%^&*():|/''AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890")

n1 = int(input("1 - символы и цифры\n2 - символы и спец символы\n3 спец символы + символы и цифры\n"))
n2 = int(input('Длина пароля:\n'))

password = ""
if n1 == 1:
    for j in range(n2):
        password += random.choice(list1)
    print("\n" + password)
if n1 == 2:
    for j in range(n2):
        password += random.choice(list2)
    print("\n" + password)
if n1 == 3:
    for j in range(n2):
        password += random.choice(list3)
    print("\n" + password)





























