from PizzaManagement import createOrder, saveOrdersToFile, loadOrdersFromFile

def displayMenu():
    print("Pizza Menu:")
    print("1. Create new order")
    print("2. Save orders to file")
    print("3. View existing orders")
    print("4. Exit")


pizzaOrderList = []
while True:
    displayMenu()
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        newOrder = createOrder()
        pizzaOrderList.append(newOrder)
    elif choice == "2":
        saveOrdersToFile(pizzaOrderList)
        print("Orders saved to file.")
    elif choice == "3":
        orders = loadOrdersFromFile()
        print("Existing Orders:")
        for idx, order in enumerate(orders, start=1):
            print(f"{idx}. {order.customername} ordered {order.pizzaType} with toppings {','.join(order.toppings)}")
    elif choice == "4":
        break

    else:
        print("Invalid choice, choose wisely one option")