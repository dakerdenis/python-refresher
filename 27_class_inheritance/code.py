class Device:
    def __init__(self,name,connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print('Disconnected.')


class Printer(Device):   #Inheritance - mean that this class copypast all this methods to itself
    def __init__(self,name,connected_by,capacity):
        super().__init__(name,connected_by)   #super() - вызывает метод такой же со своими параметрами из Device
        self.capacity = capacity
        self.remaining_pages = capacity
    
    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self,pages):
        if not self.connected:
            print("Your printer not connected")
            return
        print(f"Printing pages {pages} pages")
        self.remaining_pages -= pages



printer = Printer("Printer", "USB",200)
printer.print(20)

print(printer)

printer.disconnect()
printer.print(30)