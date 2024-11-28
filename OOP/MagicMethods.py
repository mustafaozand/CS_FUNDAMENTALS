class CustomizedInteger:

    def __init__(self, integer):
        self.integer = integer

    def __repr__(self):
        return f'CustomizedInteger({self.integer})'



int1 = CustomizedInteger(4)

print(int1)