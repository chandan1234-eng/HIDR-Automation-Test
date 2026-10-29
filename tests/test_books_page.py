
from pages.books_page import BooksPage


def test_download_book(driver):
    page = BooksPage(driver)

    page.open_books_page()
    page.click_download_button()
