class Book:

    def __init__(self, pavadinimas, autorius, prieinamumas):

        self.title = pavadinimas
        self.author = autorius
        self.availability = prieinamumas
        
    def read_book(self):
        return print(f'Title: {self.title} Author: {self.author} Availability: {self.availability}')
        
    def change_availability(self, availabilty):
        self.availability = availabilty
        return print(f'Availability changed to: {self.availability}')





book1 = Book(pavadinimas="AAAs", autorius="Get", prieinamumas=False)

book1.read_book()

book1.change_availability(True)

book1.read_book()
