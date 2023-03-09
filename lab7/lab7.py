def make_byte(powers):
    byte = [0 for _ in range(8)]
    for power in powers:
        byte[power] = 1
    return byte[::-1]


def make_powers(lst):

    powers_list = []
    
    for i, value in enumerate(lst):
        if value:
            powers_list.append(len(lst) - i - 1)
    return powers_list


def print_x_powers(lst):
    for power in lst:
        if power == 0:
            print('1', end='')
        elif power == lst[-1]:
            print(f'x^{power}', end='')
        else:
            print(f'x^{power} + ', end='')


def print_byte(lst):
    for i, value in enumerate(lst):
        if value:
            print(f'x^{len(lst) - i - 1} + ', end='')


def multiplication_in_modula(input_list1, input_list2):
     
    all_probable__powers = [0 for _ in range(15)]
  
    for i, value in enumerate(input_list1):
        current_power1 = len(input_list1) - i - 1

        for i1, value1 in enumerate(input_list2):
            current_power2 = len(input_list2) - i1 - 1
            if value and value1:
                all_probable__powers[current_power1 + current_power2] += 1
  
    return [i for i, value in enumerate(all_probable__powers) if value % 2 == 1][::-1]


def power_f_x(f_x, power):
    return [i + power for i in f_x]


def division_in_modula(divident, f_x):

    used_powers = []
    
    while max(divident) >= 8:
        for i in divident:
            if i >= 8:
                power = i - 8
                used_powers.append(power)
    
                for value in power_f_x(f_x, power):
                    if value in divident:
                        divident.remove(value)
                    else:
                        divident.append(value)
                break

    return sorted([i for i in divident])[::-1], sorted(used_powers)[::-1]


def choose_value():

    chosen_value = None

    while True:
        try:
            chosen_value = int(input('Введите число: '))
            break
        except:
            print('Вы ввели не число')

    return chosen_value

    
def main():
    f_x = [8, 4, 3, 1, 0]
    print('Выберите опцию:')
    print('Проверка примеров: 1')
    print('Собственные значения перемножаемых байтов: 2')
   
    byte1 = None
    byte2 = None
   
    chosen_value = choose_value()
    if chosen_value == 1:

        print('Выберите опцию:')
        print('Проверка примера 1: 1')
        print('Проверка примера 2: 2')

        chosen_value = choose_value()
        if chosen_value == 1:
            # byte1 = [0, 1, 1, 0, 1, 1, 1, 0]
            # byte2 = [1, 0, 0, 1, 1, 0, 1, 1]
            byte1 = [1, 1, 0, 1, 0, 0, 1, 1]
            byte2 = [0, 1, 1, 1, 0, 0, 1, 1]
        if chosen_value == 2:
            byte1 = [0, 1, 0, 1, 0, 1, 0, 1]
            byte2 = [1, 0, 1, 0, 1, 0, 1, 0]

    elif chosen_value == 2:
        byte1 = [int(value) for value in input('Введите 8 бит, разделенных пробелами: ').split()]
        byte2 = [int(value) for value in input('Введите 8 бит, разделенных пробелами: ').split()]
    
    
    print(f'''Для того, чтобы найти произведение байтов {tuple(byte1)} * {tuple(byte2)}, \
запишем их в виде многочленов и выполним умножение в кольце Z_2[x]: \n''')
    print('(', end='')
    print_x_powers(make_powers(byte1))
    print(') * (', end='')
    print_x_powers(make_powers(byte2))
    print(') = ', end='')
    mul_modula = multiplication_in_modula(byte1, byte2)
    print_x_powers(mul_modula)

    print('\n\nЗатем вычислим остаток при делении полученного многочлена на f(x):')
    print_x_powers(mul_modula)
    print('',end=' = ')
    
    remainder, used_powers = division_in_modula(mul_modula, f_x)
    print('(', end='')
    print_x_powers(f_x)
    print(') * (', end='')
    print_x_powers(used_powers)
    print(') + (', end='')
    print_x_powers(remainder)
    print(')')
    print(f'\nЗначит, произведением будет байт {tuple(make_byte(remainder))}')

if __name__ == "__main__":
    main()

# input_list1 = [0, 1, 1, 0, 1, 1, 1, 0]
# input_list2 = [1, 0, 0, 1, 1, 0, 1, 1]

