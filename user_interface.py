from storing import Storing

def main():
    store = Storing()

    print(" Investment Dashboard ")

    uinput = input()
    match(uinput):
        case 'create_table':
            table_name = input('Enter table name: ')
            table_columns = input('Enter table column(s): ')
            store.create_table(table_name, table_columns)

        case 'delete_table':
            table_name = input('Enter table name: ')
            store.delete_table(table_name)

        case _:
            print('Invalid input: Exiting')


if __name__ == "__main__":
    main()