class Coffee:
    def __init__(self, name):
         self.name = name
         self._orders = []
    @property
    def name (self):
        return self.value
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self.value = value
        else:
            raise ValueError("Name must be a string with at least 3 characters")
# coffee1 = Coffee("coffee")
# print(coffee1.name)

    def orders(self):
        return self._orders
    
    def customers(self):
    # Returns a list of all customers who have placed orders for this coffee
        all_customers = []
        for order in self._orders:
          if order.customer not in all_customers:
            all_customers.append(order.customer)
        return all_customers
    
    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        # Returns the average price for a coffee based on its orders
        if len(self._orders) == 0:
            return 0

        total_price = 0
        for order in self._orders:
            total_price += order.price

        return total_price / len(self._orders)


