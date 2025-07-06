def common_elements():
    multiples_of_3 = set()
    for x in range(100):
        if x % 3 == 0:
            multiples_of_3.add(x)
    multiples_of_5 = set()
    for x in range(100):
        if x % 5 == 0:
            multiples_of_5.add(x)
    common = set()
    for num in multiples_of_3:
        if num in multiples_of_5:
            common.add(num)
    return common

assert common_elements() == {0, 15, 30, 45, 60, 75, 90}

