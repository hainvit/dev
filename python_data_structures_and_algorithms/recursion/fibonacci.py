def calc_fibonacci(n):
    if n < 0:
        return -1
    elif n == 0 or n == 1:
        return n
    else:
        return calc_fibonacci(n-1) + calc_fibonacci(n-2)


def calc_fatorial(n):
    if n < 2:
        return n
    else:
        return n*calc_fatorial(n-1)


print('* 3! = ', calc_fatorial(3))
