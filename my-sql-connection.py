import mysql.connector
from mysql.connector import Error
from config import db_config


def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database = db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


connection = create_connection("localhost", "root", db_config.db_password, "sql_store")

def execute_query(connection, query):

    cursor = connection.cursor()

    try:

        cursor.execute(query)

        connection.commit()

        print("Query executed successfully")

    except Error as e:

        print(f"The error '{e}' occurred")

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT, 
  name TEXT NOT NULL, 
  age INT, 
  gender TEXT, 
  nationality TEXT, 
  PRIMARY KEY (id)
) ENGINE = InnoDB
"""

execute_query(connection, create_users_table)
