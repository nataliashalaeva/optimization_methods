import matplotlib.pyplot as plt
import numpy as np
import math

def fibonacci(func,a=-3,b=7,eps=0.2):
    def fib(n):
        if n in (0, 1):
            return 1
        return fib(n - 1) + fib(n - 2)

    n = 0
    while (b - a) / eps > fib(n):
        n += 1

    y = a + fib(n-2)/fib(n)*(b - a)
    z = a + fib(n-1)/fib(n)*(b - a)
    for k in range(0, n-3):
        if func(y)<=func(z):
            b = z
            y1=a+fib(n-k-3)/fib(n-k-1)*(b-a)
            z1=y
        else:
            a = y
            y1=z
            z1=a+fib(n-k-2)/fib(n-k-1)*(b-a)
        y=y1
        z=z1
        print(f"{k} итерация: a = {a}, b = {b}\nf(a) = {func(a)} ; f(b) = {func(b)}")

        k+=1

    print(f"R(N) = {1/fib(n)}", n)
    return (a+b)/2

def f_examp(x,a=1,b=2,c=4):
    return a * pow(x,2) + b * x + c




x_res = np.arange(-3,7+0.01,0.01)
y_res = f_examp(x_res)


plt.plot(x_res,y_res, label="Функция на отрезке [-3,7]")
x_min = fibonacci(f_examp)
plt.plot(x_min, f_examp(x_min), 'ro',label=f"Точка min = {x_min}; f(min) = {f_examp(x_min)}")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
