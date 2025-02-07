
#? This coding exercise requires you to complete an implementation of three methods of a class:
#? 
#? The __init__  method, which should take an argument, name . It should initialise self.name  to be the argument, and self.items  to be an empty list.
#? 
#? The add_item  method, which should append a dictionary representing an item to the store's items  property. The dictionary should have keys name  and price .
#? 
#? The stock_price  method, which should add up each item price inside self.items  to come up with a total, and return that.

class Store: 
    def __init__(self, name):
        # You'll need 'name' as an argument to this method.
        self.name = name
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.items = []
    def add_item(self, name, price):
    # Create a dictionary with keys name and price, and append that to self.items.
        item = {'name': name, 'price': price}
        self.items.append(item)

    def stock_price(self):
        # Add together all item prices in self.items and return the total
        return sum([item['price'] for item in self.items])
