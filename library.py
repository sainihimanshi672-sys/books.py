class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.issued = False

    def __str__(self):
        status = "Issued" if self.issued else "Available"
        return f"{self.title} | {self.author} | {self.isbn} | {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn):
        self.books.append(Book(title, author, isbn))
        print("Book added!\n")

    def issue_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                if b.issued:
                    print("Already issued!")
                else:
                    b.issued = True
                    print("Book issued!\n")
                return
        print("ISBN not found!\n")

    def return_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                if not b.issued:
                    print("Book was not issued!")
                else:
                    b.issued = False
                    print("Book returned!\n")
                return
        print("ISBN not found!\n")

    def view_all(self):
        if not self.books:
            print("No books in library.\n")
        else:
            print("\n--- All Books ---")
            for b in self.books:
                print(b)
            print()

    def search_title(self, title):
        found = [b for b in self.books if title.lower() in b.title.lower()]
        if found:
            print("\n--- Search Results ---")
            for b in found:
                print(b)
            print()
        else:
            print("No match found.\n")


def main():
    lib = Library()

    while True:
        print("Library Menu:")
        print("1) Add Book")
        print("2) Issue Book")
        print("3) Return Book")
        print("4) View All")
        print("5) Search by Title")
        print("6) Exit")

        ch = input("Choose (1-6): ")

        if ch == "1":
            lib.add_book(input("Title: "), input("Author: "), input("ISBN: "))

        elif ch == "2":
            lib.issue_book(input("ISBN to issue: "))

        elif ch == "3":
            lib.return_book(input("ISBN to return: "))

        elif ch == "4":
            lib.view_all()

        elif ch == "5":
            lib.search_title(input("Title search: "))

        elif ch == "6":
            print("Exit. Bye!")
            break

        else:
            print("Invalid option!\n")


if __name__ == "__main__":
    main()