import os
from datetime import datetime as dt

class PizzaOrder:
    def __init__(self, customername: str,
                       pizzaType: str,
                       toppings: list,
                       orderTime=None,
                       isDelivered=False):
        self.customername = customername
        self.pizzaType = pizzaType
        self.toppings = toppings
        self.orderTime = orderTime if orderTime else dt.now()
        self.isDelivered = isDelivered

def createOrder():
    customername = input("Type your name: ")
    pizzaType = input("What pizza looks good? ")
    toppings = input("Would you like to add toppings? (split toppings with comma)").split(",")
    return PizzaOrder(customername, pizzaType, toppings)

def saveOrdersToFile(orderList):
    with open("./orders.txt", 'w') as file:
        for pizza in orderList:
            file.write(f"{pizza.customername}, {pizza.pizzaType}, {'|'.join(pizza.toppings)}, {pizza.orderTime}, {pizza.isDelivered}\n")

def loadOrdersFromFile():
    orders = []
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'orders.txt')

    try:
        with open(file_path, 'r') as file:
            for line in file:
                orderData = line.strip().split(', ')
                if len(orderData) == 5:
                    customername, pizzaType, toppings, orderTime, isDelivered = orderData
                    toppings = toppings.split('|')
                    orderTime = dt.strptime(orderTime, '%Y-%m-%d %H:%M:%S.%f')
                    isDelivered = isDelivered == "True"
                    order = PizzaOrder(customername, pizzaType, toppings, orderTime, isDelivered)
                    orders.append(order)
                else:
                    print(f"Invalid data format in the line: {line.strip()}")
    except FileNotFoundError:
        print("FileNotFoundError: 'orders.txt' not found. Create the file and try again.")

    return orders

