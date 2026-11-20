
def add_book():
    with open("library.txt", "a") as f:
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        f.write(title + "," + author + "\n")
    print("Book added successfully!")

def search_book():
    name = input("Enter title or author: ")
    with open("library.txt", "r") as f:
        for line in f:
            if name.lower() in line.lower():
                print(line.strip())

def report():
    with open("library.txt", "r") as f:
        books = f.readlines()
    print("Total number of books:", len(books))

while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Total Books")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        report()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
