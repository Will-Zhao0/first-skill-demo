# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:44:54 2020
CSCI project1 phase1

@author: Will Zhao 
         Ding Zhang
"""

import csv


'''
The read_file function takes csv files as input and return a nested list
containing all the data from all different csv files.
'''

def read_file(csvf):
    with open(csvf, newline='') as f:
        title_line = f.readline()
        title_fields = title_line.split(',')
        
        reader = csv.reader(f)
        your_list = list(reader)
    return your_list



class Inventory:
    def __init__(self):
        self.items = []
        self.create_inventory()
        self.count = 0
    def create_inventory(self):
        #read data from the 'book' csv file and convert data into class
        count = 0
        book_list = read_file('book.csv')
        for i in book_list:
            my_item = Book(count,i[0],i[4],i[1],i[6],i[2],i[3],i[5])
            self.items.append(my_item)
            count += 1
        
        #read data from the 'CD' csv file and implement data into class object
        cd_list = read_file('cd_vinyl.csv')
        for i in cd_list:
            my_item = Cd_vinyl(count,i[0],i[5],i[4],i[6],i[1],i[2],i[3])
            self.items.append(my_item)
            count+=1
        
        #read data from the 'collectible' csv file and implement data into class object
        collectible_list = read_file('collectible.csv')
        for i in collectible_list:
            my_item = Collectible(count,i[0],i[1],i[2],i[4],i[3])
            self.items.append(my_item)
            count+=1
        
        
        #read data from the 'electronics' csv file and implement data into class object
        electronics_list = read_file('electronics.csv')
        for i in electronics_list:
            my_item = Electronics(count,i[0],i[1],i[2],i[4],i[3])
            self.items.append(my_item)
            count+=1

        #read data from the 'fashion' csv file and implement data into class object
        fashion_list = read_file('fashion.csv')
        for i in fashion_list:
            my_item = Fashion(count,i[0],i[1],i[2],i[4],i[3])
            self.items.append(my_item)
            count+=1
        
        #read data from the 'Home garden' csv file and implement data into class object
        home_garden_list = read_file('home_garden.csv')
        for i in home_garden_list:
            my_item = Home_garden(count,i[0],i[1],i[2],i[4],i[3])
            self.items.append(my_item)
            count+=1
        
    def check_type(self,item):
        #The check_type method take an specific object(eg book) as input and
        #return a string that is the object's name
        if isinstance(item, Book)==True:
            return 'Book'
        elif isinstance(item, Cd_vinyl)==True:
            return "CD_Vinyl"
        elif isinstance(item, Collectible)==True:
            return "Collectible"
        elif isinstance(item, Electronics)==True:
            return "Electronics"
        elif isinstance(item, Fashion)==True:
            return "fashion"
        elif isinstance(item, Home_garden)==True:
            return "HomeGarden"
        
    def search_item(self, item_name):
        #The search_item method takes a string as an input and print objects
        #which attributes contain the partial item name
        print('---------Search for all items with', item_name, 'in name\n')
        output_list = list()
        for i in self.items:
            if item_name in str(i.name):
                output_list.append(i)
        for item in output_list:
            print(item)
        
        
    def compute_inventory(self):
        #The compute_inventory method computes the total inventory value, and
        #returns a float of that value
        total = 0
        for i in self.items:
            total += float(i.price)*int(i.quantity)
        return total
    
    def print_inventory(self, begin = 0, end = -1):
        #The print_inventory method takes two integers as inputs: begin and end,
        #which specify the range of objects and print those specific objects
        self.begin = begin
        self.end = end
        for i in range(self.begin, self.end):
            print(self.items[i])
    
    def print_category(self, cat_name):
        #The print_category method takes one input, which represents a specific
        #object, and this function prints that whole object
        print('\n', '------Print information of items of the type: ', cat_name, '\n')
        for i in self.items:
            if self.check_type(i) == cat_name:
                print(i)
        print('---------Print Completes-----------\n')
        
            
class Item:
    def __init__(self,count,name, price, date, quantity):
        #The constructor contains five attributes which share similarities\
        #between subclasses
        self.name = name
        self.date = date
        self.price = price
        self.quantity = quantity
        self.count = count
        
    def __str__(self):
        #The str method prints all the related information in the file
        s = '******************\n'+ 'ID: '+ str(self.count) + '\n' + 'Name: ' + \
            self.name + '\n' + 'Price: ' + self.price + '\n' + 'Date: ' + \
                self.date + '\n' + 'Quantity: '+ self.quantity
        return s

class Book(Item):
    def __init__(self,count,name, price, date, quantity, publisher, author, ISBN):
        #The Book class is a subclass of Item class
        super().__init__(count,name, price, date, quantity)
        self.publisher = publisher
        self.author = author
        self.isbn = ISBN
    
    def __str__(self):
        s = super().__str__() + '\n' + 'Publisher: ' + self.publisher + '\n'\
            + 'Author: ' + self.author + '\n' + 'ISBN: ' + self.isbn
        return s
        
class Cd_vinyl(Item):
    #The Cd_vinyl class is a subclass of Item class
    def __init__(self,count,name, price, date, quantity, artist, label, ASIN):
        super().__init__(count,name, price, date, quantity)
        self.artist = artist
        self.label = label
        self.asin = ASIN
    
    def __str__(self):
        s = super().__str__() + '\n' + 'Artist: ' + self.artist + '\n' +\
            'Label: ' + self.label + '\n' + 'ASIN: ' + self.asin
        return s
        
class Collectible(Item):
    #The Collectible class is a subclass of Item class
    def __init__(self,count, name, price, date, quantity, owner):
        super().__init__(count,name, price, date, quantity)
        self.owner = owner
        
    def __str__(self):
        s = super().__str__() + '\n' + 'Owner: ' + self.owner
        return s

class Ebay(Item):
    #The Ebay class is a subclass of Item class
    def __init__(self, count,name, price, date, quantity, manufacturer):
        super().__init__(count,name, price, date, quantity)
        self.manufacturer = manufacturer
    
    def __str__(self):
        s = super().__str__() + '\n' + 'Manufacturer: ' + self.manufacturer
        return s

class Electronics(Ebay):
    #The Electronics class is a subclass of Ebay class
    def __init__(self,count, name, price, date, quantity, manufacturer):
        super().__init__(count,name, price, date, quantity, manufacturer)
    
    def __str__(self):
        return super().__str__()
        
class Fashion(Ebay):
    #The Fashion class is a subclass of Ebay class
    def __init__(self,count, name, price, date, quantity, manufacturer):
        super().__init__(count,name, price, date, quantity, manufacturer)
    
    def __str__(self):
        return super().__str__()
    
class Home_garden(Ebay):
    #The Home_garden class is a subclass of Ebay class
    def __init__(self,count, name, price, date, quantity, manufacturer):
        super().__init__(count,name, price, date, quantity, manufacturer)
    
    def __str__(self):
        return super().__str__()
