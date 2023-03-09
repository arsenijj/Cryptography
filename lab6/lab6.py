import math


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def coprime(a, b):
    return gcd(a, b) == 1


def is_prime(number):
    d = math.ceil(math.sqrt(number))
    x = 2
    while x <= d:
        if number % x == 0:
            return False
        x += 1
    return True


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

    return res, counter


def order(elems):
    sl = {}
    for i in range(len(elems)):
        sl[elems[i-1]] = elems[i:] + elems[:i]
    return sl


def encrypt_message(message, full_key):
    encrypted_message = ""

    for symbol in message:
        encrypted_message += chr(ord(symbol) + full_key)
    return encrypted_message


def get_secret_number(subscriber):
    while True:
        try:
            secret_number = int(input(f'Введите секретное число для ' \
                f'пользователя {subscriber}: '))
            if secret_number > 0:
                return secret_number
            else:
                print('Вы ввели не положительное целое число')
        except ValueError:
            print('Вы ввели не число')


def make_secret_value(sub_order, subscribers_secret_numbers, p, g):
    
    current_value = (g ** subscribers_secret_numbers[sub_order[0]]) % p

    print(f'Пользователь {sub_order[0]} вычислил {g} ^ ' \
        f'{subscribers_secret_numbers[sub_order[0]]} mod {p} и получил ' \
            f'{current_value}, затем передал это значение пользователю ' \
            f'{sub_order[1]};')

    for current_sub in sub_order[1:]:

        print(f'Пользователь {current_sub} вычислил {current_value} ^ ' \
            f'{subscribers_secret_numbers[current_sub]} mod {p} ', end ='')
        
        current_value = (current_value ** \
            subscribers_secret_numbers[current_sub]) % p
       
        if current_sub != sub_order[-1]:
            print(f'и получил {current_value}, затем предал это значение ' \
                f'пользователю {sub_order[sub_order.index(current_sub) + 1]};')
        else:
            print(f'и получил секретный ключ {current_value}.\n')


def main():

    while True:
        try:
            p = int(input('Введите простое число p: '))
            if not is_prime(p):
                print('Вы ввели не простое число')
            else:
                break
        except ValueError:
            print('Вы ввели не число')
    
    parent_elements, counter = get_parent_elements(p)

    while True:
        try:
            g = int(input(f'Введите любое число из множества порождающих ' \
                f'элементов {tuple(parent_elements)}: '))
            if not g in parent_elements:
                print('Вы ввели не порождающий элемент')
            else:
                print(f'Порядок: {counter}')
                break
        except ValueError:
            print('Вы ввели не число')

    while True:
        try:
            number_of_subscribers = int(input('Введите количество ' \
                'пользователей: '))
            break
        
        except ValueError:
            print('Вы ввели не число')
    
    subscribers = list(range(1, number_of_subscribers + 1))

    subscribers_secret_numbers = {i: get_secret_number(i) for i in subscribers}
    
    subscribers_order = order(subscribers)
    
    for subscriber in subscribers:
        print(f'{subscriber}: ' + ' -> '.join(str(elem) for elem in \
            subscribers_order[subscriber]))
        make_secret_value(subscribers_order[subscriber], \
            subscribers_secret_numbers, p, g)
        

if __name__ == '__main__':
    main()
