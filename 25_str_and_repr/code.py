class Person:
    def __init__(self, name, age):              #special method - по умолчанию если мы вызываем класс,питон сам вызывает метод инит
        self.name = name
        self.age = age

    def __str__(self):                          #__str__ - method which called when we want to tuen object tot string
        return f"Person {self.name} , {self.age} years old"
    
    def __repr__(self):                         #to be returning string that allow recreate object very easy
        return f"<Person ('{self.name}' , {self.age} )>"


bob = Person("bob",35)                          #bob is an object which we had created

bob.name = "Suka"

#print(bob)


class Store:
    def __init__(self, name, items):
        self.name = name
        self.items = []
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
    
    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        suka = {'name': name , "price": price}
        self.items.append(suka)

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        total = 0
        for item in self.items:
            total +=item['price']
        return total
        return sum([item['price'] for item in self.items])


