
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BooksPage:

    BOOKS_URL = "https://hidr.com.np/publications/books"

    DOWNLOAD_BUTTON = (
        By.XPATH,
        '//*[@id="main-content"]/div/section[1]/div/div[2]/div/div[2]/div[2]/a'
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_books_page(self):
        self.driver.get(self.BOOKS_URL)

    def click_download_button(self):
        download_button = self.wait.until(
            EC.element_to_be_clickable(self.DOWNLOAD_BUTTON)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            download_button
        )

        # Wait until no other element blocks the button
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
                download_button
            )
        )

        download_button.click()
