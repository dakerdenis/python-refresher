class Book:
    TYPES = ("hardcover", "paperback")  #in class u can also put variables and it becomes class properties

    def __init__(self, name,book_type,weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"Book is {self.name}, {self.book_type }, weight {self.weight} gram"

    @classmethod
    def hardcover(cls,name,page_weight):
        return Book(name, Book.TYPES[0], page_weight + 100)  #hardcover adding 100 grams cs it's havier 
                                                            #берётся класс внутри метода ,который внутри класса - и возвращает значения обратно в главный класс
    @classmethod
    def paperback(cls,name,page_weight):
        return Book(name, Book.TYPES[1], page_weight)  


book = Book.hardcover("Harry Potter", 1500)

book2 = Book.paperback("Suka yebanaya", 1500)


#paperback вставляются значнеия   - - - проверка с TYPES - - - операции необходимые - - - затем после обработки данные возвращаются обратно в сам класс гд еджальше уже с ними делаю твсе необходимое
#
#print(book)
#print(book2)
#

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        name = Store(store.name + " - franchise")
        return name

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'

        return '{}, total stock price is:{}  '.format(store.name, int(store.stock_price()))

store = Store("Test")
store2 = Store("Amazon")
store2.add_item("Keyboard", 160)
 
Store.franchise(store)  # returns a Store with name "Test - franchise"
Store.franchise(store2)  # returns a Store with name "Amazon - franchise"
 
Store.store_details(store)  # returns "Test, total stock price: 0"
Store.store_details(store2)  # returns "Amazon, total stock price: 160"