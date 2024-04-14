import numpy as np

# Given parameters
s1 = -0.2338 - 1.0826j 
s2 = -0.5644 - 0.4484j
s3 = -0.5644 + 0.4484j  
s4 = -0.2338 + 1.0826j
epsilon = 0.2
Omega_Lp = 1

# Define denominator polynomial
den = np.poly([s1, s2, s3, s4])

# Define frequency range
w = np.arange(-2, 2.01, 0.01)

num = 0.6251

# Define parameters for transformation
B = 0.0864
Omega0 = 0.3138
# Perform transformation to get s_L
s_L = (1j * 0.5913)**2 + Omega0**2
s_L /= B * (1j * 0.5913)

H = num / np.polyval(den, s_L)
print(1 / abs(H))
