def factor(num):
    factors = []
    for i in range(1, num + 1):
        if num%i == 0:
            factors.append(i)
    print('Factors of {} = {}'.format(num,factors))
x = 1
while x != 0:
    num = int(input('Enter number to be factored (entering 0 will exit):'))
    x = num
    if x == 0:
        print('0 entered. Exiting...')
        break
    else:
        factor(num)


def GCF(x, y):
    #Use the Euclidean Algorithm until y equals zero
    while y > 0:
        x, y = y, abs(x - y)
    return x
z = 1
while z != 0:
    x = int(input('First integer (0 to exit):'))
    if x == 0:
        print('0 entered. Exiting...')
        break
    else:
        y = int(input('Second integer (0 to exit):'))
        if y == 0:
            print('0 entered. Exiting...')
            break
        else:
            print('the Greatest Common Factor is:',GCF(x,y))
            print("\n")


import math
z = 1
while z != 0:
    a = int(input('First integer:'))
    if a == 0:
        print('0 entered. Exiting...')
        break
    else:
        b = int(input('Second integer:'))
        c = int(input('Third integer:'))
        print("\n")
        print(f'The least common multiple of {a}, {b}, and {c}, is:', math.lcm(a, b, c))
        print("\n")