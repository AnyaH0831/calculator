import sympy as sp


s, q, k, p, t, h, a, b = sp.symbols('s q k p t h a b')


expr = t*(k-p) - h*(s-q)
sqrt_lhs = sp.sqrt((k-p)**2 + (s-q)**2)
rhs = sp.Abs(a*t - b*h) / sp.sqrt(a**2 + b**2)

# Case 1: expr is positive
equation_case1 = sp.Eq(expr / sqrt_lhs, rhs)
s_solution_case1 = sp.solve(equation_case1, s)

# Case 2: expr is negative
equation_case2 = sp.Eq(-expr / sqrt_lhs, rhs)
s_solution_case2 = sp.solve(equation_case2, s)


# s_solution_case1, s_solution_case2

print("Solution for Case 1 (expr >= 0):", s_solution_case1)
print("Solution for Case 2 (expr < 0):", s_solution_case2)

