'''
The eval() funciton is used to evaluate and execute expressions which are passed as a string. It can evaluate valid expressions
e.g. arithemtic and logical operations, and function calls, and retuns the result.

'''
import ast

expression = "3 + ((5 * 6) * 4)"

result = eval(expression)

print(result)

A = 0
B = 1

new_expression = eval("A and B")

print(new_expression)

expression = "42"
result = ast.literal_eval(expression)
print(result)  # Output: 42