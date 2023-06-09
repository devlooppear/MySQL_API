import mysql.connector

HOST = 'localhost'
USER = 'root'
PASSWORD = '<sua senha>'
DATABASE = ''

class MySQLDB:
    def __init__(self):
        self.host = HOST
        self.user = USER
        self.password = PASSWORD
        self.database = DATABASE
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()
        return self.cursor.fetchall()

    def create_table(self, table_name):
        query = f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
        id INT NOT NULL AUTO_INCREMENT,
        PRIMARY KEY (id)
        ) DEFAULT CHARSET = utf8mb4;
        '''
        return self.execute_query(query)

    def drop_table(self, table_name):
        query = f'''
        DROP TABLE IF EXISTS {table_name};
        '''
        return self.execute_query(query)

    def insert_data(self, table_name, values):
        query = f'''
        INSERT INTO {table_name} 
        VALUES ({values});
        '''
        return self.execute_query(query)

    def select_data(self, table_name, column='*', condition=None):
        query = f'''
        SELECT {column} FROM {table_name}
        '''
        if condition:
            query += f' WHERE {condition}'
        return self.execute_query(query)

    def update_data(self, table_name, column, value, condition):
        query = f'''
        UPDATE {table_name}
        SET {column} = '{value}'
        WHERE {condition};
        '''
        return self.execute_query(query)

    def add_column(self, table_name, column_name, data_type):
        query = f'''
        ALTER TABLE {table_name}
        ADD COLUMN {column_name} {data_type} FIRST;
        '''
        return self.execute_query(query)

    def delete_data(self, table_name, condition, limit=None):
        query = f'''
        DELETE FROM {table_name}
        WHERE {condition}
        '''
        if limit:
            query += f'LIMIT {limit}'
        return self.execute_query(query)

    def drop_database(self, database_name):
        query = f'''
        DROP DATABASE IF EXISTS {database_name};
        '''
        return self.execute_query(query)

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
