```python
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

```

This Python script demonstrates several key concepts from our Complex Analysis courseware:

1. It defines a complex function f(z) = z^2 + 2z + 1.
2. It creates a grid of complex numbers using NumPy.
3. It applies the function to this grid and visualizes the results using Matplotlib.
4. It shows two plots:
   - The magnitude of the function (|f(z)|) using a color map.
   - The real part of the function (Re(f(z))) using a different color map.
5. It demonstrates basic operations with complex numbers.

To run this script, you'll need Python installed with NumPy and Matplotlib libraries. Here's how you can use this in your courseware:

1. Introduction to Complex Numbers (Section 1): Use the latter part of the script to demonstrate basic operations with complex numbers.

2. Complex Functions and Mappings (Section 2): Use the visualization to explain how complex functions map points from one complex plane to another. The magnitude plot can help students understand how the function transforms distances, while the real part plot can show how the function warps the complex plane.

3. Analytic Functions (Section 2.3): This example function is analytic everywhere. You can use it to discuss properties of analytic functions, such as smoothness and continuity, which are visible in the plots.

4. Visualization Tools (Section 10.2): This script serves as an example of how computational tools can aid in understanding complex analysis concepts.

Would you like me to explain any part of this code in more detail, or suggest ways to extend it for other topics in the courseware?
