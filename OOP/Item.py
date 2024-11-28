import csv

class Item:
    # Class attribute
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price:float, quantity:int=0):
        # Run Validations to the recieved arguments
        assert price >= 0, f"Price {price}  is not greater than or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0"

        # Assign to self object 
        self.name = name
        self.price = price 
        self.quantity = quantity 

        # For each instance an object is created, that instance object is appended onto my list, all
        Item.all.append(self) 

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate


    @classmethod
    def instantiate_from_csv(cls): #Class object is passed as the first argument
        with open('items.csv', 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)

       
        
        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity"))
            )

    @staticmethod
    def is_integer(num): 
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float): # check if the num is a float
            # Count out the float that are point zero
            return num.is_integer()
        
        elif isinstance(num, int):
            return True
        
        else:
            return False


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.price}, {self.quantity})"
    





        
        
# the object itself is passed in as the first argument, every time, that is why we can't create methods, that will never recieve parameters. 


