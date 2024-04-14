import sympy as sp

# Define symbols
s, z = sp.symbols('s z')

# Given transfer function
Ha_BP_s =896.08 * s**4 / (1745.06*s**8 + 2475.14*s**7 + 7372.87*s**6 + 750.02*s**5 + 1104.65*s**4 + 73.85*s**3 + 71.49*s**2 + 2.36*s + 1.68)
# Perform substitution
substitution = ((1 - z**-1) / (1 + z**-1))
substituted_expression = Ha_BP_s.subs(s, substitution)

# Simplify the expression
simplified_expression = sp.simplify(substituted_expression)

# Print the result
print("Expression in z:")
print(simplified_expression)


