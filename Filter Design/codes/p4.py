import numpy as np
import matplotlib.pyplot as plt

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

G_LP = 0.6251
num = G_LP

Omega_p1 = 0.2736
Omega_p2 = 0.3600

Omega_s1 = 0.2467
Omega_s2 = 0.3760

# Define parameters for transformation
B = 0.0864
Omega0 = 0.3138

# Perform transformation to get s_L
s_L = (1j * w)**2 + Omega0**2
s_L = s_L / (B * (1j * w))

# Band pass gain
G_bp = 896.08

# Substitute s = jw into H(s)
H = G_bp * (num / np.polyval(den, s_L))

# Plot magnitude response for H(s)
plt.figure()
plt.plot(w, abs(H), linewidth=1)
plt.title('Band Pass Filter')
plt.xlabel('Analog Frequency ($\Omega$)')
plt.ylabel('|H_{a,BP}($\Omega$)|')
plt.grid(True)
plt.ylim(0, 1.2)
plt.savefig("p4.png")
