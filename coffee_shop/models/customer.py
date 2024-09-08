class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []
    
    @property
    def name(self)  :
        return self.value 
    @name.setter 
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self.value = value
        else:
            raise ValueError("Name must be a string between 1 and 15")
        
# name1 = Customer("eugene")
# print(name1.name)
    def orders(self):
        return self._orders
     
    def coffees(self):
        unique_coffees = []
        for order in self._orders:
            if order.coffee not in unique_coffees:
                unique_coffees.append(order.coffee)
        return unique_coffees
    
    def new_order(self, coffee, price):
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee._orders.append(order)
        return order
