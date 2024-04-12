import numpy as np
import matplotlib.pyplot as plt

def dichotomy(func,a=-3,b=7,delta=0.2,eps=0.5):
    k = 0
    while True:
        y = (a+b-delta)/2
        z = (a+b+delta)/2
        if func(y)<=func(z):
            if(abs(b-z)>eps/2):
                b = z
            else:
                break
        else:
            if(abs(a-y)>eps/2):
                a = y
            else:
                break
        print(f"{k} итерация: a = {a}, b = {b}\nf(a) = {func(a)} ; f(b) = {func(b)}")
        if abs(b-a)<=eps*2:
            break
        k+=1

    print(f"R(N) = {1/(2**(k/2))}")
    return (a+b)/2

def f_examp(x,a=1,b=2,c=4):
    return a * pow(x,2) + b * x + c



print("xmin= ", dichotomy(f_examp))

x_res = np.arange(-3,7+0.01,0.01)
y_res = f_examp(x_res)

plt.plot(x_res,y_res, label="Функция на отрезке [-3,7]")
x_min = dichotomy(f_examp)
plt.plot(x_min, f_examp(x_min), 'ro',label=f"Точка min = {x_min}; f(min) = {f_examp(x_min)}")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
