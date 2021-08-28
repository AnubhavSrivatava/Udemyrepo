import sqlite3


class DatabaseConnection:
    def __init__(self, host):
        self.connection = None
        self.host = host

    def __enter__(self):
        self.connection = sqlite3.connect(
            'host')  # data.db can be replaced with host so that we can use data.db in actual module for readability
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:  # same as (if exc_type = not None or exc_val = not None  or exc_tb = not None ) :
            print("book already exists in DB")
            self.connection.close
        else:
            self.connection.commit()
            self.connection.close()
