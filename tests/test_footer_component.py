
from pages.footer_component import FooterComponent, BASE_URL


def open_home_page(driver):
    driver.get(BASE_URL)
    return FooterComponent(driver)


def test_footer_is_visible(driver):
    footer = open_home_page(driver)
    footer.verify_footer_visible()


def test_footer_content_is_visible(driver):
    footer = open_home_page(driver)
    footer.verify_footer_content()


def test_facebook_link(driver):
    footer = open_home_page(driver)
    footer.click_facebook()


def test_instagram_link(driver):
    footer = open_home_page(driver)
    footer.click_instagram()


def test_youtube_link(driver):
    footer = open_home_page(driver)
    footer.click_youtube()


def test_x_link(driver):
    footer = open_home_page(driver)
    footer.click_x()


def test_home_link(driver):
    driver.get(f"{BASE_URL}/about")
    footer = FooterComponent(driver)
    footer.click_home()


def test_about_us_link(driver):
    footer = open_home_page(driver)
    footer.click_about_us()


def test_gallery_link(driver):
    footer = open_home_page(driver)
    footer.click_gallery()


def test_contact_us_link(driver):
    footer = open_home_page(driver)
    footer.click_contact_us()


def test_map_link(driver):
    footer = open_home_page(driver)
    footer.click_map()


def test_browser_back_forward_and_refresh(driver):
    footer = open_home_page(driver)

    footer.click_about_us()
    footer.go_back("/")
    footer.go_forward("/about")
    footer.refresh_page("/about")
