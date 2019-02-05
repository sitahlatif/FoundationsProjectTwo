# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart
from components import Store

site_name = "Sitah's Site"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!

    for l in stores:
        print ("- %s"%(l.name))

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
    for l in stores:
       if store_name == l.name:
        return l
    
    return False
    #print_products()

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    print_stores()
    print('Pick a Store by typing its name. Or type "checkout" to pay your bills and say your goodbyes.')
    user= input()
    while True:
        if user == "checkout" or user == "Checkout":
             return "checkout"
        else:
            if get_store(user):
                return get_store(user)
            else:
              print("There is no store with that name, try again \n")
             
        user= input()


def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!
    print("-----------------------")
    print("%s"%(picked_store.name))
    picked_store.print_products()
    print("Pick the items you'd like to add in your cart by typing the product name exactly as it was spelled above. Type 'back' to go back to tha main mwnu where you can checkout")
    user = input("")
    while True:
        if user == "back" or user == "Back":
           break
        for p in picked_store.products :
            if user== p.name:
               cart.add_to_cart(p)
        user = input("")
       

def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    # your code goes here!
    while True:
        picked_store = pick_store()
        if picked_store == "checkout":
          break
        elif picked_store != False:
            pick_products(cart, picked_store)
    cart.checkout()


def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
