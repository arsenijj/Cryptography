import random
import math


def make_ords(text):
    return tuple(ord(symbol) for symbol in text)


def make_chars(text):
    return ''.join(chr(number) for number in text)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def make_inverse_element(a, m):
    for i in range(2, m):
        if a * i % m == 1:
            return i

def make_coprime(p, q):

    p = (p - 1) * (q - 1)
    for i in range(2, p):
        if gcd(i, p) == 1:
            return i


def is_prime(number):
    d = math.ceil(math.sqrt(number))
    x = 2
    while x <= d:
        if number % x == 0:
            return False
        x += 1
    return True


def make_primes():
    primes = []
    for target_num in range(14000, 20000):
        if is_prime(target_num):
            primes.append(target_num)
    return primes


def make_p_q_n(primes):
    p = primes[random.randint(0, len(primes) - 1)]
    q = primes[random.randint(0, len(primes) - 1)]
    return p, q, p * q

def modula_power(number, power, modula):
    number_save = number
    for i in range(power-1):
        number = number * number_save % modula
    return number

def encrypt_message(m, e, n):
    return [modula_power(symbol, e, n) for symbol in m]


def decrypt_message(m, d, n):
    return [modula_power(symbol, d , n) for symbol in m]



m = 'Привет'
m = make_ords(m)
# Создание p, q, a, d, n, e для пользователя a
p_a, q_a, n_a = make_p_q_n(make_primes())
d_a = make_coprime(p_a, q_a)
e_a = make_inverse_element(d_a, (p_a - 1) * (q_a - 1))
print(f'Пользователь a выбрал два простых числа p = {p_a} и q = {q_a}')
print(f'Затем пользователь a выбрал секретный ключ d_a = {d_a}' \
    ' (взаимнопростое c (p - 1) * (q - 1))')
print(f'Затем пользователь а вычислил значение e_a = {e_a}: e_a * d_a = 1 (mod' \
    ' ((q_a - 1) * (p_a - 1)) )\n')

# Создание p, q, a, d, n, e для пользователя c
p_b, q_b, n_b = make_p_q_n(make_primes())
d_b = make_coprime(p_b, q_b)
e_b = make_inverse_element(d_b, (p_b - 1) * (q_b - 1))
print(f'Пользователь b выбрал два простых числа p = {p_b} и q = {q_b}')
print(f'Затем пользователь a выбрал секретный ключ d_b = {d_b}'\
    ' (взаимнопростое c (p - 1) * (q - 1))')
print(f'Затем пользователь а вычислил значение e_b = {e_b}: e_b * d_b = 1' \
    ' (mod ((q_b - 1) * (p_b - 1)) )\n')

# Создание p, q, a, d, n, e для пользователя c

p_c, q_c, n_c = make_p_q_n(make_primes())
d_c = make_coprime(p_c, q_c)
e_c = make_inverse_element(d_c, (p_c - 1) * (q_c - 1))
print(f'Пользователь a выбрал два простых числа p = {p_c} и q = {q_c}')
print(f'Затем пользователь a выбрал секретный ключ d_c = {d_c}'\
    ' (взаимнопростое c (p - 1) * (q - 1))')
print(f'Затем пользователь а вычислил значение e_c = {e_c}: e_c * d_c = 1'\
    ' (mod ((q_c - 1) * (p_c - 1)))\n')

# Пользователь a шифрует сообщение e_b:
encrypted = encrypt_message(m, e_b, n_b)
print(f'Пользователь a передал сообщение m пользователю B в виде (e_b(m), B),'\
    f' то есть ({encrypted}, B)')
print(f'Пользователь c перехватил сообщение и передал его пользователю b в'\
    f' виде (e_b(m), С), то есть ({encrypted}, С)')
decrypted = decrypt_message(encrypted, d_b, n_b)

print(f'Пользователь b расшифровал сообщение d_b(e_b(m), то есть'\
    f' получил {m}')

# Пользователь b шифрует сообщение b_e:
encrypted = encrypt_message(m, e_c, n_c)
print(f'Пользователь b передал сообщение m пользователю c в виде '\
    f'(e_c(m), C), то есть ({encrypted}, C)')

#Пользователь c расшифровывает сообщение:
decrypted = make_chars(decrypt_message(encrypted, d_c, n_c))
print(f'Пользователь b расшифровал сообщение d_c(e_c(m), то есть получил '\
    f'{decrypted}')

