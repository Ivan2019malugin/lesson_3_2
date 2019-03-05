def fibonacci(n, m):
    a, b = 1, 1
    f_list = [1, ]

    for i in range(m):
        a, b = b, a + b
        f_list.append(a)

    return f_list[n - 1:m]


print(fibonacci(5, 8))