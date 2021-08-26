

from utils.database_file import *


def prompt_add_books():
    book_name = input("Enter the book name \n")
    author_name = input('Enter name of the author \n')
    add_books(book_name, author_name)


def prompt_list_books():
    list_book()


def prompt_read_books():
    r_name = input("Enter the book name you read recently \n")
    read_books(r_name)


def prompt_delete_books():
    d_name = input("Enter the book name you want to delete \n")
    delete_books(d_name)


def prompt_add_to_file():
    print("appending books to file........")
    add_to_file()


def prompt_read_from_file():
    read_from_file()


user_req = {
    'a': prompt_add_books,
    'l': prompt_list_books,
    'r': prompt_read_books,
    'd': prompt_delete_books,
    'af': prompt_add_to_file,
    'rf': prompt_read_from_file,
    'q': quit
}

user_choice = input("Enter a to add book , l to list books , r to read books , d to delete book ,rf to read from file "
                    ", af add to file , q to quit \n")

while user_choice != 'q':
    create_file_table()
    invalid = 0
    if user_choice == 'a':
        selection = user_req['a']
    #        selection()
    elif user_choice == 'l':
        selection = user_req['l']
    #        selection()
    elif user_choice == 'r':
        selection = user_req['r']
    #        selection()
    elif user_choice == 'd':
        selection = user_req['d']
    elif user_choice == 'af':
        selection = user_req['af']
    #        selection()
    elif user_choice == 'rf':
        selection = user_req['rf']
    else:
        print('Invalid Input')
        invalid = 1

    if invalid == 0:
        selection()

    user_choice = input(
        "Enter a to add book , l to list books , r to read books , d to delete book ,rf to read from file "
        ", af add to file , q to quit \n")
