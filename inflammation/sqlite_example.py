# Original code: Function that performs a database query
import sqlite3

def connect_to_datebase(db_name):
    """Connect to the SQLite database with the given name."""
    return sqlite3.connect(db_name)

def query_database(sql, connection=None):
    if connection is None:
        raise TypeError("A valid database connection is required")
    # cursor - used to traverse and manipulate results returned by a query
    cursor = connection.cursor()
    # we pass a string named 'sql' that contains our SQL query
    cursor.execute(sql)
    # fetchall - returns a list of tuples containing all rows of our result
    result = cursor.fetchall()
    connection.close()
    return result

