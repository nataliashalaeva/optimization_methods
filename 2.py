import matplotlib.pyplot as plt
import numpy as np
import math


def golden_section_search(func,a=-3,b=7,eps=0.2):
    golden_ratio = (3-math.sqrt(5)) / 2
    k = 0
    y = a + (b - a) * golden_ratio
    z = a + b - y
    while b - a > eps:
       # print(func(y) ," ",func(z))
        if func(y)<=func(z):
            b = z
            y1=a+b-y
            z1=y
        else:
            a = y
            y1=z
            z1=a+b-z
        y=y1
        z=z1
        print(f"{k} итерация: a = {a}, b = {b}\nf(a) = {func(a)} ; f(b) = {func(b)}")

        k+=1

    print(f"R(N) = {float((0.618)**k)}")
    return (a+b)/2

def f_examp(x,a=1,b=2,c=4):
    return a * pow(x,2) + b * x + c


print("xmin= ", golden_section_search(f_examp))

x_res = np.arange(-3,7+0.01,0.01)
y_res = f_examp(x_res)

plt.plot(x_res,y_res, label="Функция на отрезке [-3,7]")
x_min = golden_section_search(f_examp)
plt.plot(x_min, f_examp(x_min), 'ro',label=f"Точка min = {x_min}; f(min) = {f_examp(x_min)}")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
