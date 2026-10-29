
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BlogPage:
    BLOG_URL = "https://hidr.com.np/blog"

    ARTICLES = (
        By.XPATH,
        '//*[@id="main-content"]/div/main/section[2]/div/div[2]/article'
    )

    LOAD_MORE_BUTTON = (
        By.XPATH,
        '//*[@id="main-content"]/div/main/section[2]/div/div[3]/button'
    )

    READ_MORE_LINKS = {
        1: (By.XPATH, '//*[@id="main-content"]/div/main/section[2]/div/div[2]/article[1]/div[2]/div/a'),
        2: (By.XPATH, '//*[@id="main-content"]/div/main/section[2]/div/div[2]/article[2]/div[2]/div/a'),
        3: (By.XPATH, '//*[@id="main-content"]/div/main/section[2]/div/div[2]/article[3]/div[2]/div/a'),
        4: (By.XPATH, '//*[@id="main-content"]/div/main/section[2]/div/div[2]/article[4]/div[2]/div/a'),
        5: (By.XPATH, '//*[@id="main-content"]/div/main/section[2]/div/div[2]/article[5]/div[2]/div/a'),
    }

    EXPECTED_URLS = {
        1: "https://hidr.com.np/blog/8",
        2: "https://hidr.com.np/blog/7",
        3: "https://hidr.com.np/blog/3",
        4: "https://hidr.com.np/blog/2",
        5: "https://hidr.com.np/blog/6",
    }

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_blog_page(self):
        self.driver.maximize_window()
        self.driver.get(self.BLOG_URL)

        self.wait.until(EC.url_to_be(self.BLOG_URL))
        self.wait.until(
            lambda driver: len(
                driver.find_elements(*self.ARTICLES)
            ) >= 5
        )

    def click_element(self, locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        self.driver.execute_script(
            """
            const element = arguments[0];
            const rect = element.getBoundingClientRect();

            window.scrollTo({
                top: window.scrollY + rect.top
                     - (window.innerHeight - rect.height) / 2,
                behavior: "instant"
            });
            """,
            element
        )

        def click_point_is_clear(driver):
            element = driver.find_element(*locator)

            if not element.is_displayed() or not element.is_enabled():
                return False

            return driver.execute_script(
                """
                const element = arguments[0];
                const rect = element.getBoundingClientRect();

                const x = rect.left + rect.width / 2;
                const y = rect.top + rect.height / 2;

                const topElement = document.elementFromPoint(x, y);

                return topElement &&
                    (topElement === element ||
                     element.contains(topElement));
                """,
                element
            )

        self.wait.until(click_point_is_clear)

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def click_read_more(self, article_number):
        self.click_element(
            self.READ_MORE_LINKS[article_number]
        )

        expected_url = self.EXPECTED_URLS[article_number]

        self.wait.until(EC.url_to_be(expected_url))

        assert self.driver.current_url == expected_url, (
            f"Expected: {expected_url}, "
            f"Actual: {self.driver.current_url}"
        )

    def click_load_more(self):
        initial_count = len(
            self.driver.find_elements(*self.ARTICLES)
        )

        assert initial_count == 5, (
            f"Expected 5 blogs initially, found {initial_count}"
        )

        self.click_element(self.LOAD_MORE_BUTTON)

        self.wait.until(
            lambda driver: len(
                driver.find_elements(*self.ARTICLES)
            ) >= 7
        )

        final_count = len(
            self.driver.find_elements(*self.ARTICLES)
        )

        assert final_count >= 7, (
            f"Expected at least 7 blogs, found {final_count}"
        )

    def go_back(self):
        self.driver.back()
        self.wait.until(EC.url_to_be(self.BLOG_URL))

        assert self.driver.current_url == self.BLOG_URL

    def go_forward(self, expected_url):
        self.driver.forward()
        self.wait.until(EC.url_to_be(expected_url))

        assert self.driver.current_url == expected_url

    def refresh_page(self, expected_url):
        self.driver.refresh()

        self.wait.until(EC.url_to_be(expected_url))
        self.wait.until(
            lambda driver: driver.execute_script(
                "return document.readyState"
            ) == "complete"
        )

        assert self.driver.current_url == expected_url
