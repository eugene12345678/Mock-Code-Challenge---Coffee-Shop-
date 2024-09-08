class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        
    @property
    def cost(self):
        return self._price
    
    @cost.setter
    def cost(self, value):
        if isinstance(value, float) and 1.0 <= value <= 10.0:
            self._price = value
        else:
            raise ValueError("Price must bea a float between 1.0 and 10.0.")
order1 = Order("Eugene", "Black coffee", 7.5)
print(order1.price)
        