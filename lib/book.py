#!/usr/bin/env python3

class Book:
    def __init__(self, title , page_count , turn_page):
        self.title = title
        self.turn_page = turn_page
        if type(page_count) is int :

          self.page_count = page_count
        else:
          print("page_count must be an integer\n")  

    def turn_page(self , value):
        self. value=  value
        print("Flipping the page...wow, you read fast")
        

book1 = Book("And Then There were None" , 272)
print(book1.title, book1.page_count)
    
        