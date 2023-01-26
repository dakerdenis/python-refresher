from typing import List

def list_avg(sequence: List)-> float:   #this tells python that should be a list, and function returns float
    return sum(sequence) / len(sequence)


class Book:
    def __init__(self, name: str, page_count:int):
        self.name = name
        self.page_count = page_count
        
        
        
from typing import List

class BookShelf:
    def __init__(self,books: List[Book]):
        self.books = books
    def __str__(self) -> str:
        return f"{len(self.books)}"