from itertools import product

def preprocess_expression(expression):
    return(expression.replace("AND", "and")
                    .replace("OR", "or")
                    .replace("NOT", "not"))

def generate_truth_table(expression):
    expression = preprocess_expression(expression)

    tokens = expression.replace('(',' ( ').replace(')', ' ) ').split( )
    
    variables_set = set()

    for token in tokens:
        if token.isalpha() and token not in {"and", "or", "not"}:
            variables_set.add(token)


    
    variables = sorted(list(variables_set))

    values = [0,1]

    num_variables = len(variables)
    combinations = product(values, repeat = num_variables)

    truth_combinations = list(combinations)

    print(" | ".join(variables) + " | Result")
    print("-" * ( 4 *len(variables) + 10))

    for combination in truth_combinations:
        local_vars = dict(zip(variables, combination))
        result = eval(expression, {}, local_vars)
        print(" | ".join(map(str, combination)) + f" | {int(result)}")

        

expression = "( A AND B ) OR ( NOT ( C OR D ) )"

print(generate_truth_table(expression))
## Comments

















my_expression = " ( A AND B ) OR ( NOT ( C OR D ) ) "




