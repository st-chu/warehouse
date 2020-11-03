def menu():
    print('MENU'.center(80, '-'))
    print('|{:<78}|'.format(' exit'))
    print(''.center(80, '-'))


if __name__ == '__main__':
    while True:
        menu()
        operation_name = input("What would you like to do?: ")
        if operation_name.lower() == 'exit':
            break
