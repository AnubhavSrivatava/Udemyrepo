# same functionality as database.py but using files


import json

books = []


def create_file_table():
    with open("book_file", "w") as file:
        json.dump([], file)


def add_books(book_name, author_name):
    books.append({'name': book_name, 'author': author_name, 'read': False})
    addToFile()


def list_book():
    with open("book_file.txt", 'r') as file:
        print(json.load(file))


def read_books(r_name):
    global books
    with open("book_file.txt", 'r') as file:
        books = json.load(file)
        for outer in range(len(books)):
            if r_name in books[outer]["name"]:
                books[outer]["read"] = True
    addToFile()


def delete_books(d_name):
    global books

    books = [book for book in books if d_name != book['name']]
    addToFile()


def addToFile():
    with open("book_file.txt", "w") as file:
        json.dump(books, file, indent=4)


def add_to_file():
    with open("book_file.txt", "w") as file:
        for j in books:
            file.write(f"Book :{j['name']}\n")
            file.write(f"Author :{j['author']}\n")
            file.write(f"Reading Status : {j['read']}\n")
            file.write("\n")


def read_from_file():
    with open("book_file.txt", 'r') as file1:
        print(file1.read())
