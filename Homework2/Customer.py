import Productcheck as pc

def buy(product,num,price):
    if pc.check(product, num):
        print("You bought", product, "and spent", num*price)
    else:
        print("Sorry! We are out of this product.")
        
        
if __name__ == '__main__':
    buy('pen', 4, 100)
