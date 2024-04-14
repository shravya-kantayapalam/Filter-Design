from sympy import symbols, simplify

# Define symbolic variable s
s = symbols('s')

# Constants
omega0_val = 0.3138
B_val =0.0864




# Given roots
s1 = -0.2338 - 1.0826j 
s2 = -0.5644 - 0.4484j
s3 = -0.5644 + 0.4484j  
s4 = -0.2338 + 1.0826j
# Define the given polynomial expression
polynomial_expr = 0.6251/ ((s - s1) * (s - s2) * (s - s3) * (s - s4))

# Simplify the expression
simplified_expr = simplify(polynomial_expr)

# Print the simplified expression
print("Simplified Polynomial in terms of s:")
print(simplified_expr)
