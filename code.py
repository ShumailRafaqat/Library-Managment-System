# legacy_library_system_long.py

import os
import datetime

books_file = "books.txt"
users_file = "users.txt"
logs_file = "borrow_logs.txt"

def read_file(file):
    if not os.path.exists(file):
        open(file, 'w').close()
    with open(file, 'r') as f:
        return [line.strip().split("|") for line in f if line.strip()]

def write_file(file, data):
    with open(file, 'w') as f:
        for d in data:
            f.write("|".join(d) + "\n")

def register_user():
    users = read_file(users_file)
    uid = input("Enter User ID: ")
    name = input("Enter Name: ")
    role = input("Role (user/admin): ")
    users.append([uid, name, role])
    write_file(users_file, users)
    print("User registered.")

def add_book():
    books = read_file(books_file)
    bid = input("Enter Book ID: ")
    title = input("Title: ")
    author = input("Author: ")
    pub = input("Publisher: ")
    year = input("Year: ")
    books.append([bid, title, author, pub, year, "available"])
    write_file(books_file, books)
    print("Book added.")

def delete_book():
    books = read_file(books_file)
    bid = input("Enter Book ID to delete: ")
    books = [b for b in books if b[0] != bid]
    write_file(books_file, books)
    print("Book deleted.")

def update_book():
    books = read_file(books_file)
    bid = input("Book ID to update: ")
    for b in books:
        if b[0] == bid:
            b[1] = input("New Title: ")
            b[2] = input("New Author: ")
            b[3] = input("New Publisher: ")
            b[4] = input("New Year: ")
            break
    write_file(books_file, books)
    print("Book updated.")

def list_books():
    books = read_file(books_file)
    for b in books:
        print(f"ID: {b[0]}, Title: {b[1]}, Author: {b[2]}, Status: {b[5]}")

def borrow_book():
    books = read_file(books_file)
    uid = input("Enter User ID: ")
    bid = input("Enter Book ID: ")
    for b in books:
        if b[0] == bid and b[5] == "available":
            b[5] = f"borrowed by {uid}"
            logs = read_file(logs_file)
            logs.append([uid, bid, str(datetime.date.today()), ""])
            write_file(logs_file, logs)
            write_file(books_file, books)
            print("Book borrowed.")
            return
    print("Book not available.")

def return_book():
    books = read_file(books_file)
    bid = input("Enter Book ID: ")
    uid = input("Enter Your User ID: ")
    logs = read_file(logs_file)
    for b in books:
        if b[0] == bid and b[5] == f"borrowed by {uid}":
            b[5] = "available"
            for log in logs:
                if log[0] == uid and log[1] == bid and log[3] == "":
                    log[3] = str(datetime.date.today())
                    break
            write_file(logs_file, logs)
            write_file(books_file, books)
            print("Book returned.")
            return
    print("Error: Book not found or not issued to this user.")

def show_logs():
    logs = read_file(logs_file)
    for l in logs:
        print(f"User ID: {l[0]}, Book ID: {l[1]}, Borrowed: {l[2]}, Returned: {l[3]}")

def user_menu():
    while True:
        print("\nUser Menu:")
        print("1. List Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View Logs")
        print("5. Exit")
        ch = input("Choice: ")
        if ch == '1':
            list_books()
        elif ch == '2':
            borrow_book()
        elif ch == '3':
            return_book()
        elif ch == '4':
            show_logs()
        elif ch == '5':
            break

def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. Update Book")
        print("4. Register User")
        print("5. List Books")
        print("6. View Logs")
        print("7. Exit")
        ch = input("Choice: ")
        if ch == '1':
            add_book()
        elif ch == '2':
            delete_book()
        elif ch == '3':
            update_book()
        elif ch == '4':
            register_user()
        elif ch == '5':
            list_books()
        elif ch == '6':
            show_logs()
        elif ch == '7':
            break

def main():
    print("Welcome to Legacy Library System")
    role = input("Login as (user/admin): ")
    if role == 'user':
        user_menu()
    elif role == 'admin':
        admin_menu()
    else:
        print("Invalid role")

if __name__ == "__main__":
    main()
