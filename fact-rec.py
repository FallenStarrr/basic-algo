#ВЫЧИСЛЕНИЕ ФАКТОРИАЛА ЧИСЛА

num = 5

def fact(n):
    if n == 0:
        return 1

    return fact(n - 1) * n


print("Факториал числа {n} равен {f}".format(n=num, f = fact(num)))
