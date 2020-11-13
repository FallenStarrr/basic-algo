# ВЫЧИСЛЕНИЕ ФАКТОРИАЛА ЧИСЛА


num = 1000

def fact(n):
    if n == 0:
        return 1

    f = 1
    i = 0

    while i < n:
      i += 1
      f = f * i
    return f  


print("Факториал числа {n} равен {f}".format(n=num, f = fact(num)))
