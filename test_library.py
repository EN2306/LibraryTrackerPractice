import library

def test_get_longest_book():
    longest_book = library.get_longest_book(library.books)
    assert longest_book == {"title": "Data Science", "pages": 400, "category": "Technology"}

def test_calc_total_pages():
    total = library.calc_total_pages(library.books)
    assert total == 1600

def test_calc_average_pages():
    assert library.calc_average_pages(library.books) == 320