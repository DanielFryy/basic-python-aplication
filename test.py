def create_file(path):
    try:
        with open(path, 'x', encoding='utf-8'):
            read_file(path)
    except FileExistsError as error:
        print(error)


def read_file(path):
    try:
        with open(path, encoding='utf-8') as opened_file:
            content = opened_file.read()
            print(content)
    except FileNotFoundError as error:
        create_file(path)


def write_file(path, *lines_to_write):
    with open(path, 'a', encoding='utf-8') as opened_file:
        # opened_file.writelines(lines_to_write)
        for line in lines_to_write:
            opened_file.write(line + '\n')


read_file('test1.txt')
write_file('test2.txt', 'this', 'is', 'a', 'test')
read_file('test2.txt')
