import mysql.connector


class DatabaseHelpers:

    def __init__(self):
        self.connection = mysql.connector.connect(user='root', password='root12#', host='127.0.0.1',
                                     database='pkp_db', auth_plugin='mysql_native_password')
        self.cursor = self.connection.cursor()

    def insert_test_order_data(self):
        insert_query = ("INSERT INTO pkp_db.orders(order_num, from_name, to_name, user_id) VALUES(%(order_num)s, "
                        "%(from_name)s, %(to_name)s, %(user_id)s)")
        insert_data = {
            'order_num': '172666',
            'from_name': 'Szczecin Główny',
            'to_name': 'Gryfino',
            'user_id': 'test user'
        }

        self.cursor.execute(insert_query, insert_data)
        self.connection.commit()

    def select_test_order_data(self):
        select_query = "SELECT user_id, order_num, from_name, to_name FROM pkp_db.orders WHERE user_id = 'test user'"

        self.cursor.execute(select_query)

        for (user_id, order_num, from_name, to_name) in self.cursor:
            print(f'{user_id} - {order_num} - {from_name} - {to_name}')

    def clear_order_and_close_connection(self):
        delete_query = "DELETE FROM pkp_db.orders WHERE user_id = 'test user'"

        self.cursor.execute(delete_query)
        self.connection.close()
