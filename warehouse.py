import tabulate


items = [
    {'name': 'coffee', 'quantity': 10, 'unit': 'pkg.', 'unit_price': 65.99},
    {'name': 'soy sauce', 'quantity': 7, 'unit': 'btl.', 'unit_price': 14.45},
    {'name': 'sugar', 'quantity': 50, 'unit': 'kg', 'unit_price': 9.5}
         ]


def get_items(items):
    header = items[0].keys()
    row = [item.values() for item in items]
    print(tabulate.tabulate(row, header, tablefmt='github'))


def menu():
    print('MENU'.center(80, '_'))
    print('|{:<78}|'.format(' exit | show'))
    print(''.center(80, '-'))


if __name__ == '__main__':
    while True:
        menu()
        operation_name = input("What would you like to do?: ")
        if operation_name.lower() == 'exit':
            print('see you later alligator...')
            break
        elif operation_name.lower() == 'show':
            get_items(items)
