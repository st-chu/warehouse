import tabulate


items = [
    {'name': 'coffee', 'quantity': 10.0, 'unit': 'pkg.', 'unit_price': 65.99},
    {'name': 'soy sauce', 'quantity': 7.0, 'unit': 'btl.', 'unit_price': 14.45},
    {'name': 'sugar', 'quantity': 50.0, 'unit': 'kg', 'unit_price': 9.5}
         ]
sold_items = []


def sort_key(element):
    return element['name']


def sorted_items_list(items_list):
    return sorted(items_list, key=sort_key)


def get_items(_items):
    _items = sorted_items_list(_items)
    header = 'name', 'quantity', 'unit', 'unit_price (PLN)'
    row = [item.values() for item in _items]
    print(tabulate.tabulate(row, header, tablefmt='github'))


def menu():
    print('MENU'.center(78, '_'))
    print('|{:<76}|'.format('->Q/q: exit<-|->W/w: show<-|->A/a: add<-|->S/s: sell<-|->E/e: show_revenue<-'))
    print(''.center(78, '-'))


def is_in_list(item_list, name, unit, unit_price):
    for item in item_list:
        if item['name'] == name and item['unit'] == unit and item['unit_price'] == unit_price:
            return True


def add_item(items_list, **item_info):
    if is_in_list(items_list, item_info['name'], item_info['unit'], item_info['unit_price']) is True:
        for item in items_list:
            if item['name'] == item_info['name']:
                item['quantity'] += item_info['quantity']
    else:
        items_list.append(item_info)
    return items_list


def add_to_sold_items(sold_items_list, **product_info):
    if is_in_list(sold_items_list, product_info['name'], product_info['unit'], product_info['unit_price']) is True:
        for item in sold_items_list:
            if item['name'] == product_info['name']:
                item['quantity'] += product_info['quantity']
    else:
        sold_items_list.append(product_info)


def sell_item(items_list, sold_items_list, **item_info):
    for item in items_list:
        if item['name'] == item_info['name']:
            item['quantity'] -= item_info['quantity']
            _name = item['name']
            _quantity = item_info['quantity']
            _unit = item['unit']
            _unit_price = item['unit_price']
            add_to_sold_items(sold_items_list, name=_name, quantity=_quantity, unit=_unit, unit_price=_unit_price)


def get_cost(items_list):
    total_cost_list = [item['quantity']*item['unit_price'] for item in items_list]
    return sum(total_cost_list)


def show_revenue(items_list, sold_items_list):
    print()
    print('-'*20)
    cost = get_cost(items_list)
    income = get_cost(sold_items_list)
    print('Income: {}zł'.format(income))
    print('Costs: {}zł'.format(cost))
    print('-'*20)
    print('Revenue: {}zł'.format(income-cost))
    print('-' * 20)
    print()


if __name__ == '__main__':
    while True:
        menu()
        operation_name = input("What would you like to do?: ")
        if operation_name.lower() == 'exit' or operation_name.lower() == 'q':
            print('see you later alligator...')
            break
        elif operation_name.lower() == 'show' or operation_name.lower() =='w':
            get_items(items)
            print(get_cost(items))
        elif operation_name.lower() == 'add' or operation_name.lower() == 'a':
            name = input('Item name: ')
            quantity = float(input('Item quantity: '))
            unit = input('Item unit of measure (kg, l, pkg., btl.): ')
            unit_price = float(input('Item price in PLN: '))
            add_item(items, name=name, quantity=quantity, unit=unit, unit_price=unit_price)
            get_items(items)
        elif operation_name.lower() == 'sell' or operation_name.lower() == 's':
            name = input('Item name: ')
            quantity = float(input('Item quantity: '))
            sell_item(items, sold_items, name=name, quantity=quantity)
            get_items(items)
            get_items(sold_items)
        elif operation_name.lower() == 'show_revenue' or operation_name.lower() == 'e':
            show_revenue(items, sold_items)



