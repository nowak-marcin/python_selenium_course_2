import mysql.connector


class DatabaseHelpers:

    def __init__(self):
        self.connection = mysql.connector.connect(user='root', password='root12#', host='127.0.0.1',
                                     database='sql_kurs_1', auth_plugin='mysql_native_password')
        self.cursor = self.connection.cursor()

    def insert_test_order_data(self):
        insert_query = "INSERT INTO users(username, order, date, from, to) VALUES(%(username)s, %(display_name)s, %(year_of_birth)s)"
        insert_data = {
            'username': 'dorota333',
            'display_name': 'dorota janiak',
            'year_of_birth': '1983'
        }

        self.cursor.execute(insert_query, insert_data)
        self.connection.commit()

    def select_test_order_data(self):
        select_query = "SELECT username, display_name, year_of_birth FROM pkp_orders WHERE..."

        self.cursor.execute(select_query)
        self.connection.commit()

        for (username, display_name, year_of_birth) in self.cursor:
            print(f'{username} - {display_name} - {year_of_birth}')

    def clear_order_and_close_connection(self):
        delete_query = ""

        self.cursor.execute(delete_query)
        self.connection.close()
