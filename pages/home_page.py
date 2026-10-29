
from urllib.parse import urlparse

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
)
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


BASE_URL = "https://hidr.com.np"


class HomePage:
    HERO_SECTION = (
        By.XPATH,
        '//*[@id="main-content"]/div/section[1]'
    )

    HERO_HEADING = (
        By.XPATH,
        '//*[@id="main-content"]/div/section[1]//*[self::h1 or self::h2]'
    )

    EXPLORE_OUR_WORK = (
        By.XPATH,
        '//*[@id="main-content"]/div/section[1]/div[2]/div[2]/div/div[2]/a[1]'
    )

    HERO_PUBLICATIONS = (
        By.XPATH,
        '//*[@id="main-content"]/div/section[1]/div[2]/div[2]/div/div[2]/a[2]'
    )

    SLIDER_BUTTONS = {
        1: (
            By.XPATH,
            '//*[@id="main-content"]/div/section[1]/div[3]/button[1]'
        ),
        2: (
            By.XPATH,
            '//*[@id="main-content"]/div/section[1]/div[3]/button[2]'
        ),
        3: (
            By.XPATH,
            '//*[@id="main-content"]/div/section[1]/div[3]/button[3]'
        ),
        4: (
            By.XPATH,
            '//*[@id="main-content"]/div/section[1]/div[3]/button[4]'
        ),
        5: (
            By.XPATH,
            '//*[@id="main-content"]/div/section[1]/div[3]/button[5]'
        ),
    }

    RECENT_PUBLICATION_READ_MORE = (
        By.XPATH,
        '//*[@id="main-content"]/div/section[2]/div/div[2]/div[2]/div/a'
    )

    WHAT_WE_OFFER_BUTTONS = {
        1: (
            By.XPATH,
            '//*[@id="main-content"]/div/section[3]/div/div[2]/div/div[1]/div/div[2]/a'
        ),
        2: (
            By.XPATH,
            '//*[@id="main-content"]/div/section[3]/div/div[2]/div/div[2]/div/div[2]/a'
        ),
        3: (
            By.XPATH,
            '//*[@id="main-content"]/div/section[3]/div/div[2]/div/div[3]/div/div[2]/a'
        ),
    }

    RECENT_EVENT_BUTTONS = {
        1: (
            By.XPATH,
            '//*[@id="main-content"]/div/section[4]/div/div[2]/a[1]'
        ),
        2: (
            By.XPATH,
            '//*[@id="main-content"]/div/section[4]/div/div[2]/a[2]'
        ),
        3: (
            By.XPATH,
            '//*[@id="main-content"]/div/section[4]/div/div[3]/a'
        ),
    }

    PUBLICATIONS_READ_MORE = (
        By.XPATH,
        '//*[@id="main-content"]/div/section[5]/div/div[3]/a'
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_home_page(self):
        self.driver.maximize_window()
        self.driver.get(BASE_URL)

        self.wait.until(
            EC.visibility_of_element_located(self.HERO_SECTION)
        )

    def scroll_to_element(self, locator):
        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center',
                inline: 'center',
                behavior: 'instant'
            });
            """,
            element,
        )

        return element

    def wait_for_stable_position(self, locator):
        # Wait until the element stops moving after scrolling.
        position = {"last": None, "count": 0}

        def is_position_stable(driver):
            try:
                element = driver.find_element(*locator)
                current = element.rect

                if current == position["last"]:
                    position["count"] += 1
                else:
                    position["last"] = current
                    position["count"] = 0

                return position["count"] >= 2

            except StaleElementReferenceException:
                position["last"] = None
                position["count"] = 0
                return False

        self.wait.until(is_position_stable)

    def click_element(self, locator):
        last_error = None

        for attempt in range(2):
            try:
                element = self.scroll_to_element(locator)
                self.wait_for_stable_position(locator)

                self.wait.until(
                    EC.element_to_be_clickable(locator)
                )

                # Re-center the element after waiting.
                element = self.driver.find_element(*locator)

                self.driver.execute_script(
                    """
                    arguments[0].scrollIntoView({
                        block: 'center',
                        inline: 'center',
                        behavior: 'instant'
                    });
                    """,
                    element,
                )

                self.wait.until(
                    EC.element_to_be_clickable(locator)
                )

                # Use a real Selenium click, not JavaScript click.
                self.driver.find_element(*locator).click()
                return

            except ElementClickInterceptedException as error:
                last_error = error

                if attempt == 0:
                    # Move the target slightly lower in the viewport
                    # in case a sticky header or floating element overlaps it.
                    self.driver.execute_script(
                        "window.scrollBy(0, -120);"
                    )
                    self.wait_for_stable_position(locator)

        raise last_error

    def assert_current_url(self, expected_url):
        self.wait.until(
            lambda driver: self.urls_match(
                driver.current_url,
                expected_url
            )
        )

        actual_url = self.driver.current_url

        assert self.urls_match(actual_url, expected_url), (
            f"URL mismatch!\n"
            f"Expected: {expected_url}\n"
            f"Actual:   {actual_url}"
        )

    @staticmethod
    def urls_match(actual_url, expected_url):
        actual = urlparse(actual_url)
        expected = urlparse(expected_url)

        actual_path = actual.path.rstrip("/") or "/"
        expected_path = expected.path.rstrip("/") or "/"

        return (
            actual.scheme == expected.scheme
            and actual.netloc == expected.netloc
            and actual_path == expected_path
            and actual.query == expected.query
        )

    def click_and_assert_url(self, locator, expected_url):
        self.click_element(locator)
        self.assert_current_url(expected_url)

    def get_hero_image_state(self):
        hero = self.wait.until(
            EC.presence_of_element_located(self.HERO_SECTION)
        )

        return self.driver.execute_script(
            """
            const hero = arguments[0];
            const images = [];

            for (const element of [hero, ...hero.querySelectorAll('*')]) {
                const style = window.getComputedStyle(element);

                const visible =
                    element.getClientRects().length > 0 &&
                    style.visibility !== 'hidden' &&
                    style.display !== 'none' &&
                    Number(style.opacity) > 0;

                if (!visible) {
                    continue;
                }

                if (element.tagName === 'IMG') {
                    images.push(
                        'img:' + (element.currentSrc || element.src || '')
                    );
                }

                const background = style.backgroundImage;

                if (background && background !== 'none') {
                    images.push('bg:' + background);
                }
            }

            return [...new Set(images)].sort();
            """,
            hero,
        )

    def click_slider_and_verify_image_change(self, slide_number):
        locator = self.SLIDER_BUTTONS[slide_number]
        previous_state = self.get_hero_image_state()

        self.click_element(locator)

        self.wait.until(
            lambda driver: (
                self.get_hero_image_state() != previous_state
            )
        )

        current_state = self.get_hero_image_state()

        assert current_state != previous_state, (
            f"Slider {slide_number}: hero image did not change."
        )

        assert current_state, (
            f"Slider {slide_number}: no visible hero image found."
        )

    def go_back(self):
        self.driver.back()

    def go_forward(self):
        self.driver.forward()

    def refresh_page(self):
        current_url = self.driver.current_url
        self.driver.refresh()

        self.wait.until(
            lambda driver: driver.execute_script(
                "return document.readyState"
            ) == "complete"
        )

        self.assert_current_url(current_url)
