class Coffee:
    def __init__(self, name):
         self.name = name
         
    @property
    def name (self):
        return self.value
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self.value = value
        else:
            raise ValueError("Name must be a string with at least 3 characters")
coffee1 = Coffee("coffee")
print(coffee1.name)