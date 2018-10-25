class Client:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def check_client(self, client_name):
        flag = False
        try:
            with open('clients.txt', encoding='utf-8') as opened_file:
                clients = opened_file.readlines()
                if str(client_name + '\n') in clients:
                    flag = True
        except FileNotFoundError as error:
            print(error)
        return flag

    def create_client(self, client_name):
        with open('clients.txt', 'a', encoding='utf-8') as opened_file:
            opened_file.write(client_name + '\n')


class Pizza:
    price = 0

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.__set_price()

    def __small(self):
        return 10

    def __medium(self):
        return 20

    def __large(self):
        return 30

    def __set_price(self):
        price_list = {
            'small': self.__small(),
            'medium': self.__medium(),
            'large': self.__large()
        }
        self.price = price_list.get(self.size, 0)
