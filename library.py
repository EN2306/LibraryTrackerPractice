
# ET0735 Mock Lab Test - Library Book Tracker

books = [
    {"title": "Python Basics", "pages": 250, "category": "Programming"},
    {"title": "Data Science", "pages": 400, "category": "Technology"},
    {"title": "Web Development", "pages": 320, "category": "Programming"},
    {"title": "Cybersecurity", "pages": 280, "category": "Technology"},
    {"title": "Cloud Computing", "pages": 350, "category": "Technology"}
]


def get_longest_book(books):
    # REQ-01
    # Return the book dictionary with the most pages.
    # If the list is empty, return None.
    np = 0
    longest_book = None
    if len(books) > 0:
        for i in range(len(books)):
            if books[i]["pages"] > np:
                np = books[i]["pages"]
                longest_book = books[i]
        return longest_book
    else:
        return None


def calc_total_pages(books):
    # REQ-02a
    # Return the total number of pages.

    tp = 0
    for i in range(len(books)):
        tp += books[i]["pages"]
        return tp


def calc_average_pages(books):
    # REQ-02b
    # Return the average number of pages.
    # If the list is empty, return 0.
    total = 0
    if len(books) > 0:
        total = calc_total_pages(books)
        average = total/(len(books))
        return average
    else:
        return total

    


def main():
    print("----- Library Book Tracker -----")
    print("1 - Display all books")
    print("2 - Display statistics")
    print("3 - Display longest book")

    option = input("Enter selection => ")

    if option == "1":
        for book in books:
            print(book)

    elif option == "2":
        print("Total pages:", calc_total_pages(books))
        print("Average pages:", calc_average_pages(books))

    elif option == "3":
        print("Longest book:", get_longest_book(books))


if __name__ == "__main__":
    main()
