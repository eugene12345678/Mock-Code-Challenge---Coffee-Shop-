class Customer:
    def __init__(self, name):
        self.name = name
    @property
    def name(self)  :
        return self.value 
    @name.setter 
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self.value = value
        else:
            raise ValueError("Name must be a string between 1 and 15")
        
name1 = Customer("eugene")
print(name1.name)
        