history = {}

def register_sale():

    product = input("Product name: ")

    price = input("Product price: ")
    while not price.replace(".", "", 1).isdigit():
        print("Only numbers are allowed")
        price = input("Product price: ")

    quantity = input("Quantity sold: ")
    while not quantity.isdigit():
        print("Only numbers are allowed")
        quantity = input("Quantity sold: ")

    price = float(price)
    quantity = int(quantity)

    total = price * quantity

    history[product] = history.get(product, 0) + quantity

    return total