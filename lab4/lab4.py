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
            return False, x
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


def write_sequence(a, x_0, sequence, f):
    f.write(f'a = {a} , x_0 = {x_0}, {sequence}' + '\n')


def get_sequence(a, x_0, p, f=None, flag=False):
    sequence = [a * x_0 % p]
    counter = 1
    while True:
        new_x = a * sequence[-1] % p
        if new_x in sequence:
            if not flag:
                return write_sequence(a, x_0, sequence, f) 
            else:
                print(f'Период равен {counter}, элементы последовательности: {sequence}')
                return
        else:
            sequence.append(new_x)
            counter += 1


def get_option():
    print('Выберите опцию работы программы: ')
    print('1 - получить максимально достижимый период для данного элемента')
    print('2 - ввести числа x_0 и a и получить период')
    while True:
        try:
            number = int(input('Введите число: '))
            return number
        except:
            print('Вы ввели не число')
            continue


def get_all_maximal_sequences(elems, m):

    chosen_value = int(input('Если вы желаете получить все возможные максимальные последовательности, введите 1, иначе введите 0: '))
    if chosen_value:
        f = open(f'Number_{m}.txt', 'w')
        for a in elems:
            for x_0 in elems:
                get_sequence(a, x_0, m, f)
    else:
        return

def main():
    while True:
        n = int(input())
        print(get_parent_elements(n))

        m = x_0 = a = None

        try:
            m = int(input('Введите целое число m, по модулю вычетов которого будет строиться последовательность: '))
        except:
            print('Вы ввели не целое число')
            return main()
    
        option = get_option()

        elems, order = get_parent_elements(m)
    
        if option == 1:
            print(f'Период равен {order}')
            print(f'Порождающие элементы: {elems}')
            get_all_maximal_sequences(elems, m)
        
        if option == 2:
            while True:
                print('Введите число x_0, взаимнопростое с m: ', end='')
                try:
                    x_0 = int(input())
                    break
                except ValueError:
                    print('Вы ввели не число')
            if not coprime(x_0, m):
                print('Введено число, не взаимнопростое с m')
        
            while True:
                print(f'Введите число a (первообразные элементы в данном случае {elems}): ', end='')
                try:
                    a = int(input())
                    break
                except ValueError:
                    print('Вы ввели не число')

            get_sequence(a, x_0, m, flag=True)
        

if __name__ == "__main__":
    main()