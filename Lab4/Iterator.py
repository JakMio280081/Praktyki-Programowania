#Interfejs iteratora
class Iterator:
    def has_next(self):
        pass

    def next(self):
        pass

#Interfejs kolekcji
class Collection:
    def create_iterator(self):
        pass

#Konkretna kolekcja
class NumberCollection(Collection):
    def __init__(self, numbers):
        self.numbers = numbers

    def create_iterator(self):
        return NumberIterator(self)

#Konkretny iterator
class NumberIterator(Iterator):
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def has_next(self):
        return self.index < len(self.collection.numbers)

    def next(self):
        value = self.collection.numbers[self.index]
        self.index += 1
        return value

#Klient
numbers = NumberCollection([10, 20, 30, 40])
iterator = numbers.create_iterator()

while iterator.has_next():
    print(iterator.next())
