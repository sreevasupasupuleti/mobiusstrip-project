import numpy as np
import matplotlib.pyplot as plt


# Parameters
R, w = 1.0, 0.5  # Radius & Width
n_u, n_v = 200, 100  # Resolution in u and v

# Generate mesh grid
u = np.linspace(0, 2 * np.pi, n_u)[:, None]  # Column vector
v = np.linspace(-w / 2, w / 2, n_v)  # Row vector

# Parametric equations
X = (R + v * np.cos(u / 2)) * np.cos(u)
Y = (R + v * np.cos(u / 2)) * np.sin(u)
Z = v * np.sin(u / 2)


# Compute surface area using numerical integration
def surface_element(u, v):
    xu = (-v / 2 * np.sin(u / 2) * np.cos(u) - (R + v * np.cos(u / 2)) * np.sin(u))
    yu = (-v / 2 * np.sin(u / 2) * np.sin(u) + (R + v * np.cos(u / 2)) * np.cos(u))
    zu = v / 2 * np.cos(u / 2)

    xv = np.cos(u / 2) * np.cos(u)
    yv = np.cos(u / 2) * np.sin(u)
    zv = np.sin(u / 2)

    normal = np.sqrt((yu * zv - zu * yv) ** 2 + (zu * xv - xu * zv) ** 2 + (xu * yv - yu * xv) ** 2)
    return normal




# Compute edge length (numerical integration along u)
edge_length = np.trapz(np.sqrt(X[:, -1] ** 2 + Y[:, -1] ** 2 + Z[:, -1] ** 2), u.flatten())

# Plotting Möbius Strip
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='k')

ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
plt.title("Möbius Strip")

plt.show()

# Display computed properties
print(f"Computed Surface Area: {surface_area:.4f}")
print(f"Computed Edge Length: {edge_length:.4f}")
