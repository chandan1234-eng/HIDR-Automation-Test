
from urllib.parse import urlparse

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


BASE_URL = "https://hidr.com.np"


class FooterComponent:

    FOOTER = (By.XPATH, "//footer")

    COMPANY_NAME = (
        By.XPATH,
        "//footer//*[contains(normalize-space(), "
        "'Himal Innovative Development')]"
    )
    QUICK_LINKS_HEADING = (
        By.XPATH, "//footer//*[normalize-space()='Quick Links']"
    )
    COPYRIGHT_TEXT = (
        By.XPATH,
        "//footer//*[contains(normalize-space(), 'All rights reserved')]"
    )

    # Social media links: supplied XPath locators
    FACEBOOK_LINK = (
        By.XPATH, "/html/body/footer/div[1]/div/div[1]/div/div/a[1]"
    )
    INSTAGRAM_LINK = (
        By.XPATH, "/html/body/footer/div[1]/div/div[1]/div/div/a[2]"
    )
    YOUTUBE_LINK = (
        By.XPATH, "/html/body/footer/div[1]/div/div[1]/div/div/a[3]"
    )
    X_LINK = (
        By.XPATH, "/html/body/footer/div[1]/div/div[1]/div/div/a[4]"
    )

    # Quick links
    HOME_LINK = (
        By.XPATH, "/html/body/footer/div[1]/div/div[2]/ul/li[1]/a"
    )
    ABOUT_US_LINK = (
        By.XPATH, "/html/body/footer/div[1]/div/div[2]/ul/li[2]/a"
    )
    GALLERY_LINK = (
        By.XPATH, "/html/body/footer/div[1]/div/div[2]/ul/li[3]/a"
    )
    CONTACT_US_LINK = (
        By.XPATH, "/html/body/footer/div[1]/div/div[2]/ul/li[4]/a"
    )

    MAP_LINK = (
        By.XPATH, "/html/body/footer/div[1]/div/div[3]/a"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @staticmethod
    def normalize_path(path):
        return path.rstrip("/") or "/"

    def verify_footer_visible(self):
        self.wait.until(
            EC.visibility_of_element_located(self.FOOTER)
        )

    def verify_footer_content(self):
        self.wait.until(
            EC.visibility_of_element_located(self.COMPANY_NAME)
        )
        self.wait.until(
            EC.visibility_of_element_located(self.QUICK_LINKS_HEADING)
        )
        self.wait.until(
            EC.visibility_of_element_located(self.COPYRIGHT_TEXT)
        )

    def scroll_to_footer(self):
        footer = self.wait.until(
            EC.presence_of_element_located(self.FOOTER)
        )

        # Scroll to the bottom of the page first
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

        # Then bring the footer into view
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'end'});",
            footer
        )

        self.wait.until(
            EC.visibility_of_element_located(self.FOOTER)
        )

    def click_element(self, locator):
        self.scroll_to_footer()

        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )

        # Position the link in the middle of the viewport
        self.driver.execute_script(
            "arguments[0].scrollIntoView({"
            "block: 'center', inline: 'center'});",
            element
        )

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        try:
            # Prefer a normal Selenium user-style click
            element.click()

        except ElementClickInterceptedException:
            # Fallback only if a normal click is intercepted.
            # This bypasses the normal hit-testing, so it should
            # not be treated as proof that a user can click the link.
            element = self.driver.find_element(*locator)

            self.driver.execute_script(
                "arguments[0].click();", element
            )

    def verify_current_path(self, expected_path):
        expected_path = self.normalize_path(expected_path)

        self.wait.until(
            lambda driver: self.normalize_path(
                urlparse(driver.current_url).path
            ) == expected_path
        )

        actual_path = self.normalize_path(
            urlparse(self.driver.current_url).path
        )

        assert actual_path == expected_path, (
            f"Expected path: {expected_path}; "
            f"Actual URL: {self.driver.current_url}"
        )

    @staticmethod
    def urls_match(actual_url, expected_url):
        actual = urlparse(actual_url)
        expected = urlparse(expected_url)

        return (
            actual.scheme.lower() == expected.scheme.lower()
            and actual.netloc.lower() == expected.netloc.lower()
            and FooterComponent.normalize_path(actual.path)
            == FooterComponent.normalize_path(expected.path)
            and actual.query == expected.query
        )

    def click_internal_link(self, locator, expected_path):
        self.click_element(locator)
        self.verify_current_path(expected_path)

    def click_external_link(self, locator, expected_url):
        original_handle = self.driver.current_window_handle
        original_url = self.driver.current_url
        handles_before = set(self.driver.window_handles)

        self.click_element(locator)

        self.wait.until(
            lambda driver: (
                bool(set(driver.window_handles) - handles_before)
                or driver.current_url != original_url
            )
        )

        new_handles = set(self.driver.window_handles) - handles_before
        opened_new_tab = bool(new_handles)

        if opened_new_tab:
            self.driver.switch_to.window(new_handles.pop())

        try:
            self.wait.until(
                lambda driver: self.urls_match(
                    driver.current_url, expected_url
                )
            )

            assert self.urls_match(
                self.driver.current_url, expected_url
            ), (
                f"Expected URL: {expected_url}; "
                f"Actual URL: {self.driver.current_url}"
            )

        finally:
            if opened_new_tab:
                self.driver.close()
                self.driver.switch_to.window(original_handle)

    # Social media
    def click_facebook(self):
        self.click_external_link(
            self.FACEBOOK_LINK,
            "https://www.facebook.com/hidrnepal/"
        )

    def click_instagram(self):
        self.click_external_link(
            self.INSTAGRAM_LINK,
            "https://www.instagram.com/"
        )

    def click_youtube(self):
        self.click_external_link(
            self.YOUTUBE_LINK,
            "https://www.youtube.com/"
        )

    def click_x(self):
        self.click_external_link(
            self.X_LINK,
            "https://x.com/"
        )

    # Internal navigation
    def click_home(self):
        self.click_internal_link(self.HOME_LINK, "/")

    def click_about_us(self):
        self.click_internal_link(self.ABOUT_US_LINK, "/about")

    def click_gallery(self):
        self.click_internal_link(self.GALLERY_LINK, "/gallery")

    def click_contact_us(self):
        self.click_internal_link(self.CONTACT_US_LINK, "/contact")

    # Map
    def click_map(self):
        self.click_external_link(
            self.MAP_LINK,
            "https://www.google.com/maps?q=Himal+Innovative+Development+and+Research,+Buddha+Marg,+Kathmandu+44600"
        )

    # Browser navigation
    def go_back(self, expected_path):
        self.driver.back()
        self.verify_current_path(expected_path)

    def go_forward(self, expected_path):
        self.driver.forward()
        self.verify_current_path(expected_path)

    def refresh_page(self, expected_path):
        self.driver.refresh()
        self.verify_current_path(expected_path)
