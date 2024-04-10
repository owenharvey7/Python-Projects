# 9
# Dictionaries Challenge:
# Modify the books dictionary to include the publication year of each book.

# Explain Program
print("This program will modify the books dictionary to include the publication year of each book.\n")

books = {"The Great Gatsby": "F. Scott Fitzgerald", "To Kill a Mockingbird": "Harper Lee",
         "1984": "George Orwell", "The Catcher in the Rye": "J.D. Salinger"}

# Add publication year to each book.
def add_year():
    for book in books:
        books[book] = [books[book], input(f"What year was '{book}' published? ")]

add_year()

# Print the books dictionary.
print(books)
print()
