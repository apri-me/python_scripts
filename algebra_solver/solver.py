from sympy import sympify, solve	

eq = input("Enter Your Equation: ")
seq = sympify(f"Eq({eq.replace('=', ',')})")
result = solve(seq)
result = ", ".join(str(x) for x in result)
print(f"X can be : {{ {result} }}")