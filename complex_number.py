import numpy as np
import matplotlib.pyplot as plt

def complex_function(z):
    return z**2 + 2*z + 1

# Create a grid of points
x = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x, y)

# Create complex numbers
Z = X + 1j*Y

# Apply the function
W = complex_function(Z)

# Calculate the absolute value (magnitude) of the result
abs_W = np.abs(W)

# Create the plot
plt.figure(figsize=(12, 8))

# Plot the magnitude of the function
plt.subplot(121)
plt.title('Magnitude of f(z) = z^2 + 2z + 1')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
magnitude_plot = plt.pcolormesh(X, Y, abs_W, cmap='viridis', shading='auto')
plt.colorbar(magnitude_plot, label='|f(z)|')

# Plot the real part of the function
plt.subplot(122)
plt.title('Real part of f(z) = z^2 + 2z + 1')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
real_plot = plt.pcolormesh(X, Y, W.real, cmap='RdBu', shading='auto')
plt.colorbar(real_plot, label='Re(f(z))')

plt.tight_layout()
plt.show()

# Demonstrate some operations with complex numbers
z1 = 2 + 3j
z2 = 1 - 2j

print(f"z1 = {z1}")
print(f"z2 = {z2}")
print(f"z1 + z2 = {z1 + z2}")
print(f"z1 * z2 = {z1 * z2}")
print(f"z1 / z2 = {z1 / z2}")
print(f"|z1| = {abs(z1)}")
print(f"f(z1) = {complex_function(z1)}")
