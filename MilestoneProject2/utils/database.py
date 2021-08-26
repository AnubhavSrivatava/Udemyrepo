books = []


def add_books(book_name, author_name):
    books.append({'name': book_name, 'author': author_name, 'read': False})


def list_book():
    for i in books:
        print(i)


def read_books(r_name):
    for i in books:
        if r_name in i['name']:
            i['read'] = True


def delete_books(d_name):
    global books
    books = [book for book in books if d_name != book['name']]


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
