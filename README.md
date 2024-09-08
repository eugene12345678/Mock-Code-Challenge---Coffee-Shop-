# Mock Code Challenge - Coffee Shop (Object Relationships) 
## Overview
This project simulates a simple coffee shop management system using Object-Oriented Programming (OOP) in Python. It includes three main classes:

- Customer
- Coffee
- Order

The relationships between these models are as follows:

- A Customer can have multiple Orders.
- A Coffee can be part of multiple Orders.
- An Order is associated with both a Customer and a Coffee.

## Features
- **Customer Management:** Create and manage customers, track their orders, and identify the customer who has spent the most on a specific coffee.
- **Coffee Management:** Create coffee types, track orders for each coffee, and calculate the number of orders and average price for each coffee.
- **Order Management:** Link customers and coffee with a price, ensuring data integrity and enabling various queries.

## Getting Started
### Requirements
- Python 3.x installed on your machine.
- An IDE or text editor of your choice (such as VS Code, PyCharm, or Sublime Text).

### Installation
1. **Clone the Repository**

```bash
git clone https://github.com/eugene12345678/Mock-Code-Challenge---Coffee-Shop-.git
cd Mock-Code-Challenge---Coffee-Shop
```

2. **Create a Virtual Environment**
```bash
python -m venv venv
```
3. **Activate the Virtual Environment**
- On Windows:
```bash
venv\Scripts\activate
```
- On macOS/Linux:
```bash
source venv/bin/activate
```

4. Create Project Files and Folders
- Organize your project structure as follows:
```css
coffee_shop/
├── models/
│   ├── coffee.py
│   ├── customer.py
│   └── order.py
├── venv/
├── requirements.txt
├── README.md
```
5. Install Dependencies

There are no external dependencies for this project. If you add any in the future, you can use a `requirements.txt` file to list them.

## Example Usage
Here’s a quick guide on how to use the classes in this project:

1. Create Coffee Instances:
```python
from models.coffee import Coffee

latte = Coffee("Latte")
espresso = Coffee("Espresso")
```
2. Create Customer Instances:
```python
from models.customer import Customer

eugene = Customer("Eugene")
cate = Customer("Cate")
```
3. Place Orders:
```python
from models.order import Order

# Eugene places orders
order1 = eugene.new_order(latte, 5.0)  # Eugene orders a Latte for $5.00
order2 = eugene.new_order(espresso, 4.5)  # Eugene orders an Espresso for $4.50

# Cate places an order
order3 = cate.new_order(latte, 5.5)  # Cate orders a Latte for $5.50
```
4. View Orders and Coffees:
```python
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
from models.customer import Customer
most_aficionado = Customer.most_aficionado(latte)
print("Most Aficionado for Latte:", most_aficionado.name) # Should print "Eugene" or "Cate" depending on who spent more on Latte
```
### Running Tests
To ensure everything is working correctly, you can run the provided test suite. Assuming you have pytest installed, use the following command:
```bash
python3 test_coffee_shop.py
```

## Contributing
Feel free to contribute to this project by submitting issues, pull requests, or suggestions. Please follow standard Git workflow practices.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
[Eugene Mathenge](https://github.com/eugene12345678)


