import sqlite3


def create_book_table():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS books(tittle text primary key , author text , read integer )')
    connection.commit()
    connection.close()


def get_all_books():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM books')
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    connection.close()
    return books


def add_book(name, author):
    # ",0);DROP TABLE books;     #sql injection attack
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    #   cursor.execute(f'INSERT INTO books VALUES("{name}","{author}",0)')  #prone to sql injection attack hence it should not be used
    #   cursor.execute(f'INSERT INTO books VALUES("{name}","",0);DROP TABLE books;",0)') # direct string formating is not safe for queries
    cursor.execute('INSERT INTO books VALUES(?,?,0)', (name, author))
    connection.commit()
    connection.close()


def mark_book_as_read(name):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute('UPDATE books SET read=1 WHERE tittle=?', (name,))
    connection.commit()
    connection.close()


def delete_book(name):
    with sqlite3.connect('data.db') as connection:  # note this
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE tittle =?', (name,))
        connection.commit()
