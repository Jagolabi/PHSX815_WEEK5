import numpy as np
import matplotlib.pyplot as plt
def target_dist(x, y):
    return np.exp(-(x**2/2 + y**2/8))
def proposal_dist():
    x = np.random.uniform(-4, 4)
    y = np.random.uniform(-2, 2)
    return x, y
def rejection_sampling(target_dist, proposal_dist, num_samples):
    samples = []
    while len(samples) < num_samples:
        x, y = proposal_dist()
        u = np.random.uniform(0, 1)
        if u < target_dist(x, y):
            samples.append((x, y))
    return np.array(samples)
# Generate 200 random samples using rejection sampling
samples = rejection_sampling(target_dist, proposal_dist, num_samples=200)

# Plot the target and proposal distributions
x = np.linspace(-4, 4, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = target_dist(X, Y)
plt.contour(X, Y, Z, cmap='Blues')
plt.xlim(-4, 4)
plt.ylim(-2, 2)
plt.gca().set_aspect('equal')

rect_x = [-4, 4, 4, -4, -4]
rect_y = [-2, -2, 2, 2, -2]
plt.plot(rect_x, rect_y, 'k--', lw=1)

# Plot the random samples
plt.scatter(samples[:, 0], samples[:, 1], s=10, c='red')

plt.show()
