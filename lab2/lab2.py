from sympy import *

from functools import reduce

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def coprime(a, b):
    return gcd(a, b) == 1


def get_parent_elements(m):

    counter = 1
    res = []

    for i in [i for i in range(2, m) if coprime(i, m)]:

        current_counter = 1
        elem_save = elem = i

        while elem != 1:
            elem *= elem_save
            elem %= m
            current_counter += 1

        if current_counter == counter:
            res.append(i)
        elif current_counter > counter:
            res = [i]
            counter = current_counter

    return res

# number, modula!
def gcdExtended(a, b):
    if a == 0 :
        return b, 0, 1
   
    gcd, x1, y1 = gcdExtended(b % a, a)
    
    x = y1 - (b // a) * x1
    y = x1
    
    return gcd, x, y


def chinese_remainder(pairs):

    mod_list, remainder_list = [p[0] for p in pairs], [p[1] for p in pairs]
    mod_product = reduce(lambda x, y: x * y, mod_list)
    mi_list = [mod_product // x for x in mod_list]
    mi_inverse = [gcdExtended(mi_list[i], mod_list[i])[1] for i in range(len(mi_list))]
    x = 0
    for i in range(len(remainder_list)):
        x += mi_list[i] * mi_inverse[i] * remainder_list[i]
        x %= mod_product
    return x


def factor(p):
   
    d, factors, unique_factors = 2, [], set()

    while d*d <= p:

        if isprime(d):
            while (p % d) == 0:
                factors.append(d)
                unique_factors.add(d)
                p //= d
            
        d += 1


    if p > 1:
       unique_factors.add(p)
       factors.append(p)
    
    return [(i, factors.count(i)) for i in unique_factors]


def modula_power(a, power, modula):
    
    b = 1
    while power:
        if not power % 2:
            power //= 2
            a = (a * a) % modula
        else:
            power -= 1
            b = (b * a) % modula
    return b


def powers_table(factors_powers, a, p):

    table = []

    for (factor, _) in factors_powers:
        
        subres = []
        
        for i in range(factor):
            
            probable_value = ((factor, i, modula_power(a, ((i * (p - 1)) // factor ), p)))

            if (k := probable_value[2]) not in subres:
                table.append(probable_value)
                subres.append(k)
                
    return table


def find_in_table(table, q, value):
    for (a, b, c) in table:
        if a == q and c == value:
            return b


def decomposition(a_inversed, b, q_power, p, table):

    q, power = q_power[0], q_power[1]

    right = modula_power(b, (p - 1) // q, p)

    x_0 = find_in_table(table, q, right)
 

    if power == 1:
    
        print(f'x \u2261 {x_0} (mod {q ** power})')
        return x_0
    
    else:
        congruence = [x_0]

        for i in range(1, power):
        
            b = (b * modula_power(a_inversed, x_0 * (q ** (i - 1)), p)) % p
            right = modula_power(b, (p - 1) // (q ** (i + 1)), p)

            x_0 = find_in_table(table, q, right)
            congruence.append(x_0 * (q ** i))
        
        res = sum(congruence) % (q ** power)
        print(f'x \u2261 {res} (mod {q ** power})')

        return res


def get_number(pos, parent_elems = None):

    while True:
        try:
            if pos == 'a':
                print('Порождающие элементы циклической группы: ', *parent_elems)

            number = int(input(f'Введите {pos}: '))
            
            if number > 0:
                
                if pos == 'p':
                    if isprime(number):
                        return number
                    else:
                        print('Вы ввели не простое число')
                elif pos == 'a':
                    # if number in parent_elems:
                        # return number
                    # else:
                        # print('Вы ввели не порождающий элемент')
                        return number
                else:
                    return number

            else:
                print('Вы ввели не положительное целое число')
        except ValueError:
            print('Вы ввели не число')


def main():
    
    while True:
        
        print('\nВыполнить дискретное логарифмирование алгоритмом '\
            'Сильвера-Полига-Хеллмана - \enter')
        print('Выход из программы - 2')

        try:
            value = int(input('Введите значение: '))
        except ValueError:
            value = 1
        
        if value == 1:
            
            b = get_number('b')
            p = get_number('p')
            a = get_number('a', get_parent_elements(p))
            
            # if a not in get_parent_elements(p):
            if modula_power(a, p - 1, p) != 1:
                print(f'Число {a} не является порождающим элементом циклической группы F_{p}')
                continue

            factors_powers = factor(p - 1)

            table = powers_table(factors_powers, a, p)

            a_inversed = (gcdExtended(a, p)[1] % p + p) % p

            congruences = [(q_power[0] ** q_power[1], \
                decomposition(a_inversed, b, q_power, p, table))  \
                    for q_power in factors_powers]

            print(f'x \u2261 {chinese_remainder(congruences)} (mod {p})')

        if value == 2:
            print('Работа программы завершена!')
            break


if __name__ == "__main__":
    main()
    
