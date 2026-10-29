
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CareerPage:

    CAREER_URL = "https://hidr.com.np/careers"

    JOIN_TEAM_BUTTON = (
        By.XPATH,
        '//*[@id="main-content"]/div/div/section[1]/div[2]/a'
    )

    CAREER_OPENING_SECTION = (
        By.XPATH,
        "//*[contains(translate(normalize-space(.), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'career openings')]"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_career_page(self):
        self.driver.get(self.CAREER_URL)

    def click_join_team(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.JOIN_TEAM_BUTTON)
        )
        button.click()

    def verify_career_openings(self):
        section = self.wait.until(
            EC.visibility_of_element_located(
                self.CAREER_OPENING_SECTION
            )
        )

        assert section.is_displayed(), (
            "Career Openings section is not displayed"
        )
