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
    print('|{:<78}|'.format(' exit | show | add | sell |'))
    print(''.center(80, '-'))


def add_item(items_list):
    name = input('Item name: ')
    quantity = float(input('Item quantity: '))
    unit = input('Item unit of measure (kg, l, pkg., btl.): ')
    unit_price = float(input('Item price in PLN: '))
    return items_list.append({'name': name, 'quantity': quantity, 'unit': unit, 'unit_price': unit_price})


def sel_item(item_list):
    name = input('Item name: ')
    quantity = float(input('Quantity to sell: '))
    for item in item_list:
        if item['name'] == name:
            item['quantity'] -= quantity
    return item_list


if __name__ == '__main__':
    while True:
        menu()
        operation_name = input("What would you like to do?: ")
        if operation_name.lower() == 'exit':
            print('see you later alligator...')
            break
        elif operation_name.lower() == 'show':
            get_items(items)
        elif operation_name.lower() == 'add':
            add_item(items)
            get_items(items)
        elif operation_name.lower() == 'sell':
            items = sel_item(items)
            get_items(items)
