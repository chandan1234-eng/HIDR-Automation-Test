
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ContactPage:

    CONTACT_URL = "https://hidr.com.np/contact"

    NAME_INPUT = (
        By.XPATH,
        '//*[@id="main-content"]/div/main/section[2]/div/div/div/div[1]/form/div[1]/input'
    )

    EMAIL_INPUT = (
        By.XPATH,
        '//*[@id="main-content"]/div/main/section[2]/div/div/div/div[1]/form/div[2]/input'
    )

    PHONE_INPUT = (
        By.XPATH,
        '//*[@id="main-content"]/div/main/section[2]/div/div/div/div[1]/form/div[3]/input'
    )

    MESSAGE_INPUT = (
        By.XPATH,
        '//*[@id="main-content"]/div/main/section[2]/div/div/div/div[1]/form/div[4]/textarea'
    )

    SUBMIT_BUTTON = (
        By.XPATH,
        '//*[@id="main-content"]/div/main/section[2]/div/div/div/div[1]/form/button'
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_contact_page(self):
        self.driver.get(self.CONTACT_URL)
        self.wait.until(
            EC.visibility_of_element_located(self.NAME_INPUT)
        )

    def get_field(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def enter_name(self, name):
        field = self.get_field(self.NAME_INPUT)
        field.clear()
        field.send_keys(name)

    def enter_email(self, email):
        field = self.get_field(self.EMAIL_INPUT)
        field.clear()
        field.send_keys(email)

    def enter_phone(self, phone):
        field = self.get_field(self.PHONE_INPUT)
        field.clear()
        field.send_keys(phone)

    def enter_message(self, message):
        field = self.get_field(self.MESSAGE_INPUT)
        field.clear()
        field.send_keys(message)

    def fill_contact_form(self, name, email, phone, message):
        self.enter_name(name)
        self.enter_email(email)
        self.enter_phone(phone)
        self.enter_message(message)

    def get_field_value(self, locator):
        return self.get_field(locator).get_attribute("value")

    def get_field_validity(self, locator):
        return self.driver.execute_script(
            "return arguments[0].validity.valid;",
            self.get_field(locator)
        )

    def is_form_valid(self):
        button = self.get_field(self.SUBMIT_BUTTON)

        return self.driver.execute_script(
            "return arguments[0].form.checkValidity();",
            button
        )
