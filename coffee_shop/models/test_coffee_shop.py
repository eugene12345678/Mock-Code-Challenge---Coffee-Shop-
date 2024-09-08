from customer import Customer
from coffee import Coffee
from order import Order

# Create coffee instances
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create customer instances
eugene = Customer("Eugene")
bob = Customer("Cate")

# Eugene places orders
order1 = eugene.new_order(latte, 5.0)
order2 = eugene.new_order(espresso, 4.5)

# Bob places an order
order3 = bob.new_order(latte, 5.5)

# Check Eugene's orders
print("Eugene's Orders:", eugene.orders())  # Should display detailed Order objects

# Check unique coffees Eugene has ordered
print("Eugene's Coffees:", eugene.coffees())  # Should display detailed Coffee objects

# Check Coffee instances' data
print("Latte Orders:", latte.orders())  # Should display detailed Order objects
print("Espresso Orders:", espresso.orders())  # Should display detailed Order objects

# Get the average price of Latte
print("Latte Average Price:", latte.average_price())  # Should print average price of Latte

# Get the most aficionado customer for Latte
most_aficionado = Customer.most_aficionado(latte)
print("Most Aficionado for Latte:", most_aficionado.name)  # Should print "Eugene" or "Bob" depending on who spent more on Latte
