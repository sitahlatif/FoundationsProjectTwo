# CLASSES AND METHODS
class Store():
    def __init__(self, name):
       
        self.name = name
        self.products = []

    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        # your code goes here!
        self.product = product
        self.products.append(product)

    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        # your code goes here!
        print("%s:"%(self.name))
        for p in self.products:
          print("\t Product Name: %s" %(p.name))
          print("\t Description: %s"%(p.description))
          print("\t Price: %s \n"%(str(p.price)))

class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        # your code goes here!
        self.name = name
        self.description = description
        self.price = price 

    def __str__(self):
        # your code goes here!
        return "Product Name: %s \n Description: %S \n Price: %d"%(self.name,self.description,str(self.price))


class Cart():
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        # your code goes here!
        self.products = []

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        # your code goes here!
        #if product not in self.products:

        self.products.append(product)

    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        # your code goes here!
        total = 0
        for p in self.products:
           total += p.price
        return total

    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        # your code goes here!
        print()
        print("-------------------------------------------")
        print("Here's your receipt:")
        for i in self.products:
            print("\n Product Name: %s \n Description: %s \n Price %d" %(i.name, i.description,i.price))
        print ("Your Total price is:%s"%(self.get_total_price()))

    def checkout(self):
        """
        Does the checkout.
        """
        # your code goes here!
        self.print_receipt()
        confirm = input("Confirm? (yes/no)")
        if confirm == "yes" or confirm=="Yes":
            print("Your order has been placed")
        else:
            print("Your order has been cancled")


