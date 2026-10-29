
import pytest

from pages.home_page import HomePage, BASE_URL


@pytest.fixture
def home_page(driver):
    page = HomePage(driver)
    page.open_home_page()
    return page


def test_home_page_loads(home_page):
    home_page.assert_current_url(BASE_URL)

    heading = home_page.wait.until(
        lambda driver: driver.find_element(
            *home_page.HERO_HEADING
        )
    )

    assert heading.is_displayed(), "Hero heading is not visible."
    assert heading.text.strip(), "Hero heading is empty."


def test_explore_our_work_button(home_page):
    home_page.click_and_assert_url(
        home_page.EXPLORE_OUR_WORK,
        f"{BASE_URL}/our-work"
    )


def test_hero_our_publications_button(home_page):
    home_page.click_and_assert_url(
        home_page.HERO_PUBLICATIONS,
        f"{BASE_URL}/publications/all"
    )


def test_all_hero_slider_images_change(home_page):
    # Check every slide, including returning to slide 1.
    for slide_number in [2, 3, 4, 5, 1]:
        home_page.click_slider_and_verify_image_change(
            slide_number
        )


def test_recent_publication_read_more(home_page):
    home_page.click_and_assert_url(
        home_page.RECENT_PUBLICATION_READ_MORE,
        f"{BASE_URL}/blog/8"
    )


@pytest.mark.parametrize(
    ("button_number", "expected_url"),
    [
        (1, f"{BASE_URL}/what-we-offer/1"),
        (2, f"{BASE_URL}/what-we-offer/2"),
        (3, f"{BASE_URL}/what-we-offer/3"),
    ],
)
def test_what_we_offer_learn_more_buttons(
    home_page,
    button_number,
    expected_url,
):
    home_page.click_and_assert_url(
        home_page.WHAT_WE_OFFER_BUTTONS[button_number],
        expected_url,
    )


@pytest.mark.parametrize(
    ("button_number", "expected_url"),
    [
        (1, f"{BASE_URL}/event/1"),
        (2, f"{BASE_URL}/event/2"),
        (3, f"{BASE_URL}/event/3"),
    ],
)
def test_recent_event_buttons(
    home_page,
    button_number,
    expected_url,
):
    home_page.click_and_assert_url(
        home_page.RECENT_EVENT_BUTTONS[button_number],
        expected_url,
    )


def test_publications_section_read_more(home_page):
    home_page.click_and_assert_url(
        home_page.PUBLICATIONS_READ_MORE,
        f"{BASE_URL}/publications/all"
    )


def test_browser_back_forward_and_refresh(home_page):
    home_page.click_and_assert_url(
        home_page.EXPLORE_OUR_WORK,
        f"{BASE_URL}/our-work"
    )

    # Back: Our Work -> Home
    home_page.go_back()
    home_page.assert_current_url(BASE_URL)

    # Forward: Home -> Our Work
    home_page.go_forward()
    home_page.assert_current_url(
        f"{BASE_URL}/our-work"
    )

    # Refresh: URL should remain on Our Work
    home_page.refresh_page()
    home_page.assert_current_url(
        f"{BASE_URL}/our-work"
    )
