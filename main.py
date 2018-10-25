import classes


def order(client_name, client_address, pizza_name, pizza_size):
    client = classes.Client(client_name, client_address)
    pizza = classes.Pizza(pizza_name, pizza_size)
    if pizza.price > 0:
        if client.check_client(client.name):
            register_order(client.name, pizza)
        else:
            client.create_client(client.name)
            register_order(client.name, pizza)
    else:
        print('Invalid size')


def register_order(client_name, pizza):
    with open('clients.txt', encoding='utf-8') as registered_clients:
        clients = registered_clients.readlines()
        index = clients.index(str(client_name + '\n'))
        with open('orders.txt', 'a', encoding='utf-8') as opened_file:
            registry = clients[index].rstrip('\n') + ' -> ' + pizza.name + ' - ' + pizza.size + ' - ' + str(pizza.price)
            opened_file.write(registry + '\n')


def check_orders():
    try:
        with open('orders.txt', encoding='utf-8') as registered_orders:
            orders = registered_orders.read()
            print(orders)
    except FileNotFoundError as error:
        print('There are no orders')


check_orders()
order('Daniel', 'somewhere1', 'Neapolitan', 'medium')
order('Daniel', 'somewhere2', 'Italian', 'medium')
order('Daniel', 'somewhere3', 'Sicilian', 'medium')
order('Liss', 'somewhere4', 'Hawaiian', 'small')
order('Liss', 'somewhere8', 'Hawaiian', 'medium')
order('Liss', 'somewhere5', 'Maltese', 'large')
order('Pedro', 'somewhere6', 'Jumbo', 'large')
order('Pedro', 'somewhere9', 'Jumbo', 'giant')
order('Andrés', 'somewhere7', 'Mexican', 'medium')
check_orders()
