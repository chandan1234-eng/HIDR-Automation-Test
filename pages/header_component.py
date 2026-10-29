
from urllib.parse import urlparse

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


BASE_URL = "https://hidr.com.np"


class HeaderComponent:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Header locators

    LOGO = (
        By.XPATH,
        "//img[@alt='Himal Innovative Development & Research Logo']"
    )

    HOME_LINK = (
        By.XPATH,
        "//a[normalize-space()='Home' and "
        "(@href='/' or @href='https://hidr.com.np/')]"
    )

    WHO_WE_ARE_MENU = (
        By.XPATH,
        "//button[normalize-space()='Who We Are']"
    )

    ABOUT_US_LINK = (
        By.XPATH,
        "//a[normalize-space()='About Us' and "
        "contains(@href, '/about')]"
    )

    WHAT_WE_OFFER_LINK = (
        By.XPATH,
        "//a[normalize-space()='What We Offer' and "
        "contains(@href, '/what-we-offer')]"
    )

    OUR_TEAM_LINK = (
        By.XPATH,
        "//a[normalize-space()='Our Team' and "
        "contains(@href, '/our-team')]"
    )

    OPPORTUNITIES_MENU = (
        By.XPATH,
        "//button[normalize-space()='Opportunities']"
    )

    CAREER_LINK = (
        By.XPATH,
        "//a[normalize-space()='Career' and "
        "contains(@href, '/careers')]"
    )

    PARTNER_LINK = (
        By.XPATH,
        "//a[normalize-space()='Partner with us' and "
        "contains(@href, '/partner')]"
    )

    PUBLICATIONS_MENU = (
        By.XPATH,
        "//button[normalize-space()='Publications']"
    )

    REPORT_LINK = (
        By.XPATH,
        "//a[normalize-space()='Report' and "
        "contains(@href, '/publications/reports')]"
    )

    POLICY_BRIEF_LINK = (
        By.XPATH,
        "//a[normalize-space()='Policy Brief' and "
        "contains(@href, '/publications/briefs')]"
    )

    ANNUAL_REPORT_LINK = (
        By.XPATH,
        "//a[normalize-space()='Annual Report' and "
        "contains(@href, '/publications/annualreport')]"
    )

    ALL_PUBLICATIONS_LINK = (
        By.XPATH,
        "//a[normalize-space()='All Publication' and "
        "contains(@href, '/publications/all')]"
    )

    BOOK_LINK = (
        By.XPATH,
        "//a[normalize-space()='Book' and "
        "contains(@href, '/publications/books')]"
    )

    BLOG_LINK = (
        By.XPATH,
        "//a[normalize-space()='Blog' and "
        "contains(@href, '/blog')]"
    )

    # Find a visible, enabled element and click it

    def click_element(self, locator):
        element = self.wait.until(
            lambda driver: next(
                (
                    item
                    for item in driver.find_elements(*locator)
                    if item.is_displayed() and item.is_enabled()
                ),
                False
            )
        )

        element.click()

    # Verify the expected URL path

    @staticmethod
    def normalize_path(path):
        return path.rstrip("/") or "/"

    def verify_current_url(self, expected_path):
        expected_path = self.normalize_path(expected_path)

        try:
            self.wait.until(
                lambda driver: self.normalize_path(
                    urlparse(driver.current_url).path
                ) == expected_path
            )
        except TimeoutException:
            pass

        actual_url = self.driver.current_url
        actual_path = self.normalize_path(
            urlparse(actual_url).path
        )

        assert actual_path == expected_path, (
            f"Navigation failed. "
            f"Expected path: {expected_path}, "
            f"Actual path: {actual_path}, "
            f"Current URL: {actual_url}"
        )

    # Verify dropdown submenu visibility

    def verify_submenu_visible(self, locator):
        self.wait.until(
            lambda driver: any(
                element.is_displayed()
                for element in driver.find_elements(*locator)
            )
        )

    # Logo and Home

    def click_logo(self):
        self.click_element(self.LOGO)
        self.verify_current_url("/")

    def click_home(self):
        self.click_element(self.HOME_LINK)
        self.verify_current_url("/")

    # Who We Are

    def open_who_we_are_menu(self):
        self.click_element(self.WHO_WE_ARE_MENU)
        self.verify_submenu_visible(self.ABOUT_US_LINK)

    def click_about_us(self):
        self.click_element(self.ABOUT_US_LINK)
        self.verify_current_url("/about")

    def click_what_we_offer(self):
        self.click_element(self.WHAT_WE_OFFER_LINK)
        self.verify_current_url("/what-we-offer")

    def click_our_team(self):
        self.click_element(self.OUR_TEAM_LINK)
        self.verify_current_url("/our-team")

    # Opportunities

    def open_opportunities_menu(self):
        self.click_element(self.OPPORTUNITIES_MENU)
        self.verify_submenu_visible(self.CAREER_LINK)

    def click_career(self):
        self.click_element(self.CAREER_LINK)
        self.verify_current_url("/careers")

    def click_partner(self):
        self.click_element(self.PARTNER_LINK)
        self.verify_current_url("/partner")

    # Publications

    def open_publications_menu(self):
        self.click_element(self.PUBLICATIONS_MENU)
        self.verify_submenu_visible(self.REPORT_LINK)

    def click_report(self):
        self.click_element(self.REPORT_LINK)
        self.verify_current_url("/publications/reports")

    def click_policy_brief(self):
        self.click_element(self.POLICY_BRIEF_LINK)
        self.verify_current_url("/publications/briefs")

    def click_annual_report(self):
        self.click_element(self.ANNUAL_REPORT_LINK)
        self.verify_current_url("/publications/annualreport")

    def click_all_publications(self):
        self.click_element(self.ALL_PUBLICATIONS_LINK)
        self.verify_current_url("/publications/all")

    def click_book(self):
        self.click_element(self.BOOK_LINK)
        self.verify_current_url("/publications/books")

    # Blog

    def click_blog(self):
        self.click_element(self.BLOG_LINK)
        self.verify_current_url("/blog")
