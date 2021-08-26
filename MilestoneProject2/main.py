# from utils import database
books = []
print("welcome")
def prompt_add_books :
     book_name = input("Enter the book name")
     author_name = input ('Enter name of the author')
     books.append({'name': book_name , 'author': author_name , 'read': False})

def prompt_list_books :
    for i in books:
        print(i)
        print(i['author_name'])

prompt_add_books()
