import tabulate
import csv
import copy

items = [
    {'name': 'coffee', 'quantity': 10.0, 'unit': 'pkg.', 'unit_price': 65.99},
    {'name': 'soy sauce', 'quantity': 7.0, 'unit': 'btl.', 'unit_price': 14.45},
    {'name': 'sugar', 'quantity': 50.0, 'unit': 'kg', 'unit_price': 9.5}
         ]
sold_items = []


def sort_key(element):
    return element['name']


def sorted_items_list(items_list):
    """Sorts alphabetically the names of the products in the list"""
    return sorted(items_list, key=sort_key)


def get_items(_items):
    _items = sorted_items_list(_items)
    header = 'name', 'quantity', 'unit', 'unit_price (PLN)'
    row = [item.values() for item in _items]
    print(tabulate.tabulate(row, header, tablefmt='github'))


def menu():
    print('MENU'.center(91, '_'))
    print('|{:<89}|'.format('->Q/q: exit<-|->W/w: show<-|->A/a: add<-|->S/s: sell<-|->E/e: show_revenue<-|->R/r save<-'))
    print(''.center(91, '-'))


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


def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


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
    revenue = income - cost
    cost = round(cost, 2)
    income = round(income, 2)
    revenue = round(revenue, 2)
    print('Income: {}zł'.format(income))
    print('Costs: {}zł'.format(cost))
    print('-'*20)
    print('Revenue: {}zł'.format(revenue))
    print('-' * 20)
    print()


def export_item_to_csv(items_list):
    with open('magazyn.csv', 'w') as magazyn_csv:
        fieldnames = ['name', 'quantity', 'unit', 'unit_price']
        csv_writer = csv.DictWriter(magazyn_csv, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()
        for item in items_list:
            csv_writer.writerow(item)


def export_sales_to_csv(sold_items_list):
    with open('sales.csv', 'w') as sales_csv:
        fieldnames = ['name', 'quantity', 'unit', 'unit_price']
        csv_writer = csv.DictWriter(sales_csv, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()
        for item in sold_items_list:
            csv_writer.writerow(item)


def change_quantity_and_unit_price_from_str_to_float(items_list):
    for item in items_list:
        for key, value in item.items():
            if key == 'quantity' or key == 'unit_price':
                item[key] = float(value)


def import_items_from_csv(items_list):
    with open('magazyn.csv', 'r') as magazyn_csv:
        csv_reader = csv.DictReader(magazyn_csv, delimiter='\t')
        items_list.clear()
        for line in csv_reader:
            items_list.append(line)
        change_quantity_and_unit_price_from_str_to_float(items_list)


if __name__ == '__main__':
    import_items_from_csv(items)
    print(items)
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
            while True:
                quantity = input('Item quantity: ')
                quantity = quantity.replace(',', '.')
                if is_number(quantity) is True:
                    quantity = float(quantity)
                    quantity = round(quantity, 2)
                    break
                else:
                    print('-' * 51)
                    print('the value entered is not a number, please try again')
                    print('-' * 51)
            unit = input('Item unit of measure (kg, l, pkg., btl.): ')
            while True:
                unit_price = input('Item price in PLN: ')
                unit_price = unit_price.replace(',', '.')
                if is_number(unit_price) is True:
                    unit_price = float(unit_price)
                    unit_price = round(unit_price, 2)
                    break
                else:
                    print('-' * 51)
                    print('the value entered is not a number, please try again')
                    print('-' * 51)
            add_item(items, name=name, quantity=quantity, unit=unit, unit_price=unit_price)
            get_items(items)
        elif operation_name.lower() == 'sell' or operation_name.lower() == 's':
            name = input('Item name: ')
            while True:
                quantity = input('Item quantity: ')
                quantity = quantity.replace(',', '.')
                if is_number(quantity) is True:
                    quantity = float(quantity)
                    quantity = round(quantity, 2)
                    break
                else:
                    print('-' * 51)
                    print('the value entered is not a number, please try again')
                    print('-' * 51)
            sell_item(items, sold_items, name=name, quantity=quantity)
            get_items(items)
            get_items(sold_items)
        elif operation_name.lower() == 'show_revenue' or operation_name.lower() == 'e':
            show_revenue(items, sold_items)
        elif operation_name.lower() == 'save' or operation_name.lower() == 'r':
            export_item_to_csv(items)
            export_sales_to_csv(sold_items)
        elif operation_name.lower() == 'load' or operation_name.lower() == 'l':
            import_items_from_csv(items)
