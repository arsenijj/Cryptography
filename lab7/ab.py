def make_powers(lst):

    powers_list = []
    
    for i, value in enumerate(lst):
        if value:
            powers_list.append(len(lst) - i - 1)
    return powers_list


def make_mul(lst1, lst2):
    res = []
    for elem in lst1:
        for elem2 in lst2:
            res.append(elem + elem2)
    print(res)
    print(sorted(set([i for i in res if res.count(i) % 2]))[::-1])


make_mul(make_powers([0,1,0,1,0,1,0,1]),make_powers([1,0,1,0,1,0,1,0]))