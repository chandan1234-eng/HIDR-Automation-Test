
import pytest

from pages.blog_page import BlogPage


@pytest.fixture
def blog_page(driver):
    page = BlogPage(driver)
    page.open_blog_page()
    return page


@pytest.mark.parametrize(
    "article_number",
    [1, 2, 3, 4, 5]
)
def test_read_more_navigation(blog_page, article_number):
    blog_page.click_read_more(article_number)


def test_load_more_displays_remaining_blogs(blog_page):
    blog_page.click_load_more()


def test_blog_back_forward_refresh(blog_page):
    blog_page.click_read_more(1)

    article_url = BlogPage.EXPECTED_URLS[1]

    blog_page.go_back()
    blog_page.go_forward(article_url)
    blog_page.refresh_page(article_url)
