
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PartnerPage:

    PARTNER_URL = "https://hidr.com.np/partner"
    CONTACT_URL = "https://hidr.com.np/contact"
    LEARN_MORE_URL = "https://hidr.com.np/partner#why-partner"

    CONTACT_US_BUTTON = (
        By.XPATH,
        '//*[@id="main-content"]/div/main/section[1]/div/div/div[1]/div/a[1]'
    )

    LEARN_MORE_BUTTON = (
        By.XPATH,
        '//*[@id="main-content"]/div/main/section[1]/div/div/div[1]/div/a[2]'
    )

    GET_IN_TOUCH_BUTTON = (
        By.XPATH,
        '//*[@id="main-content"]/div/main/section[5]/div/div/a'
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_partner_page(self):
        self.driver.get(self.PARTNER_URL)

    def click_contact_us(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.CONTACT_US_BUTTON)
        )

        button.click()

        self.wait.until(EC.url_to_be(self.CONTACT_URL))

        assert self.driver.current_url == self.CONTACT_URL

    def click_learn_more(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.LEARN_MORE_BUTTON)
        )

        button.click()

        self.wait.until(EC.url_to_be(self.LEARN_MORE_URL))

        assert self.driver.current_url == self.LEARN_MORE_URL

    def click_get_in_touch(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.GET_IN_TOUCH_BUTTON)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            button
        )

        # Wait until the button's center is not covered by another element
        self.wait.until(
            lambda driver: driver.execute_script(
                """
                const element = arguments[0];
                const rect = element.getBoundingClientRect();

                const x = rect.left + rect.width / 2;
                const y = rect.top + rect.height / 2;

                const topElement = document.elementFromPoint(x, y);

                return topElement && (
                    topElement === element ||
                    element.contains(topElement)
                );
                """,
                button
            )
        )

        button.click()

        self.wait.until(EC.url_to_be(self.CONTACT_URL))

        assert self.driver.current_url == self.CONTACT_URL, (
            f"Expected URL: {self.CONTACT_URL}, "
            f"Actual URL: {self.driver.current_url}"
        )
