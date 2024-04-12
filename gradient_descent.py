import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x):
    x1, x2 = x
    return x1**2 + 6*x2**2 + x1*x2 + x1

def gradient(x):
    x1, x2 = x
    grad_x1 = 2*x1 + x2 + 1
    grad_x2 = 12*x2 + x1
    return np.array([grad_x1, grad_x2])

def gradient_descent(x0, delta, eps, max_iter):
    x = np.array(x0)
    for i in range(max_iter):
        grad = gradient(x)
        norm_grad = np.linalg.norm(grad)
        if norm_grad < eps:
            print(f"Converged after {i+1} iterations")
            break
        direction = -grad / np.linalg.norm(grad)
        x_new = x + delta * direction
        if np.linalg.norm(x_new - x) < eps:
            print(f"Converged after {i+1} iterations")
            break
        x = x_new
    else:
        print("Did not converge after", max_iter, "iterations")
    return x

x0 = [1.5, 1.1]
delta = 0.15
eps = 0.1
max_iter = 50

minimum = gradient_descent(x0, delta, eps, max_iter)
print("Minimum point:", minimum)
print("Minimum value:", f(minimum))

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x1_vals = np.linspace(-2, 2, 100)
x2_vals = np.linspace(-2, 2, 100)
x1_mesh, x2_mesh = np.meshgrid(x1_vals, x2_vals)
f_vals = f([x1_mesh, x2_mesh])

ax.plot_surface(x1_mesh, x2_mesh, f_vals, cmap='viridis', alpha=0.8)
ax.scatter(minimum[0], minimum[1], f(minimum), color='red', s=100, label='Minimum')

ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('f(x)')
ax.legend()
plt.show()
