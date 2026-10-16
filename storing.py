import sqlite3

class Storing():
    def __init__(self):
        self.connection = sqlite3.connect("companies.db")
        self.cur = self.connection.cursor()

    # Creating a table
    def create_table(self, table_name, table_columns):
        try:
            self.cur.execute(
                f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                {table_columns}
                )
                """
            )
            print('Table creation: Successful')
        except:
            print('Table creation: Unsuccessful')

    def delete_table(self, table_name):
        try:
            self.cur.execute(
                f"""DROP TABLE {table_name}"""
            )
            print(f'Success: {table_name} deleted')
        except:
            print(f'Error: {table_name} not found')
