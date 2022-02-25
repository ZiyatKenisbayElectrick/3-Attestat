"""
xor шифрование
"""

def form_dict():
    alphabet = list(ascii_letters) + list(digits)
    return dict([(i, alphabet[i]) for i in range(len(alphabet))])

def encode_val(word):
    d = form_dict()
    return [k for c in word for k, v in d.items() if v == c]

def comparator(value, key):
    return dict([(index, list(character))
                 for index, character in enumerate(zip(value, cycle(key)))])

def full_encode(value, key):
    d = comparator(value, key)
    l = len(form_dict())
    return [(v[0] ^ v[1]) % l for v in d.values()]

def full_decode(value, key):
    d = comparator(value, key)
    l = len(form_dict())
    return [(v[0] - v[1]) % l for v in d.values()]

word = 'habrahabrru'
key = 'occaZZion9'
print 'Слово: ' + word
print 'Ключ: ' + key
key_encoded = encode_val(key)
value_encoded = encode_val(word)
encoded_text = full_encode(value_encoded, key_encoded)

decoded = full_decode(encoded_text, key_encoded)

"""
Цезарь
"""

a = int(input("Введите число сдвига: "))
b = input("Введите строку для шифрования/дешифрования: ")
c = 'abcdefghijklmnopqrstuvwxyz' * 2
d = int(input("Выберите операцию - 1) Шифрование; 2) Дешифрование: "))

res = []
len_c = len(c)

if (d == 1):
    for i in b:
        res.append(c[(c.find(i)+a)%len_c]) 
    print('Зашифрованная строка: ',''.join(res))

elif (d == 2):
    for i in b:
        res.append(c[(c.find(i)-a)%len_c]) 
    print('Расшифрованная строка: ',''.join(res))

else:
    print('Данной операции нет.')

"""
Гронсфельд
"""

a = 'abcdefghijklmnopqrstuvwxyz' * 2
message = str(input("Введите строку для шифрования: "))
key = str(input("Введите ключ: "))
d = int(input("Выберите операцию - 1) Шифрование; 2) Дешифрование: "))

if (d == 1):
    def encrypt(message, key):
        return f(message, key, 1)

    def f(text, k, op):
        k *= len(text) // len(k) + 1
        text = text.upper()
        return ''.join([a[a.index(j) + int(k[i]) * op] for i, j in enumerate(text)])

    print("Зашифрованная строка: ", encrypt(message, key))

elif (d == 2):
    def encrypt(message, key):
        return d(message, key, 1)

    def d(text, k, op):
        k *= len(text) // len(k) + 1
        text = text.upper()
        return ''.join([a[a.index(j) - int(k[i]) * op] for i, j in enumerate(text)])
    print("Рашифрованная строка: ", encrypt(message, key))

else:
    print('Данной операции нет.')

"""
Виженер
"""

from itertools import cycle

alp = 'abcdefghijklmnopqrstuvwxyz'
a = str(input("Введите строку для шифрования: "))
b = str(input("Введите ключ шифрования: "))
d = int(input("Выберите операцию - 1) Шифрование; 2) Дешифрование: "))

text = a.lower()
key = b.lower()

if (d == 1):
    def encode_vijn(text, key):
        f = lambda arg: alp[(alp.index(arg[0])+alp.index(arg[1])%26)%26]
        return ''.join(map(f, zip(text, cycle(key))))
    print("Зашифрованная строка: ", encode_vijn(text, key))

elif (d == 2):
    def encode_vijn(text, key):
        f = lambda arg: alp[(alp.index(arg[0])-alp.index(arg[1])%26)%26]
        return ''.join(map(f, zip(text, cycle(key))))
    print("Расшифрованная строка: ", encode_vijn(text, key))

else:
    print('Данной операции нет.')