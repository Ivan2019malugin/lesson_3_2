def my_round(number, ndigits):
    number = number*(10**ndigits)+0.5
    number = number//1
    return number/(10**ndigits)
print(my_round(25.45646658, 4))