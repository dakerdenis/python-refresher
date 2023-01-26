class Test__learning:
    def print_name(self,name):
        print("message1:{}  message2: {}".format(name , name + ' changed'))

    def say_hello(self):
        self.print_name("stalker")


test1 = Test__learning()













class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}   Age: {self.age}")


tom  = Person("Tom",23)
bob = Person("Bob", 38)

#tom.display_info()
#bob.display_info()


class Store:
    def __init__(self,name):
        self.name = name
        self.items = []

    def add_item(self,name,price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock__price(self):
        total = 0
        for item in self.items:
            total +=item['price']
        return total
    
    @classmethod
    def franchise(cls, store):
        return cls(store.name + " - franchise")
    
    @staticmethod
    def store_details(store):
        return '{} , total stock price: {}'.format(store.name, int(store.stock_price()))

    @staticmethod
    def all_items_and_name(store):
        print("Shop: {}".format(store.name))
        i=1
        list1 = store.items
        for n in list1:

            print("{}) {} , with price {} $".format(i, n['name'] , n['price']))
            i+=1
        print("Total amount of orders: {}".format(store.stock__price()))


#создаём обьекты
store = Store("Test")
store2 = Store("Amazon")

#добавляем 3 элемента в магазин

store2.add_item("Keyboard", 100)
store2.add_item("Rx 6600xt", 160)
store2.add_item("Book", 130)
store2.add_item("Table", 420)
store2.add_item("Stalker", 50)






#выдаёт количество товаров в магазине
Store.all_items_and_name(store2)