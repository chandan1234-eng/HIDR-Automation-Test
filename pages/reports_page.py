
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ReportsPage:

    REPORTS_URL = "https://hidr.com.np/publications/reports"

    PDF_URL = (
        "https://admin.hidr.com.np/media/publications/"
        "Final_Report_GRB_Report_Press_Ready_25_May_2026.pdf"
    )

    REPORT_LINK = (
        By.XPATH,
        '//*[@id="main-content"]/div/section[1]/div/div/div[3]/div/a'
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_reports_page(self):
        self.driver.get(self.REPORTS_URL)

    def click_report_link(self):
        original_tab = self.driver.current_window_handle

        report = self.wait.until(
            EC.element_to_be_clickable(self.REPORT_LINK)
        )

        report.click()

        self.wait.until(
            EC.number_of_windows_to_be(2)
        )

        for tab in self.driver.window_handles:
            if tab != original_tab:
                self.driver.switch_to.window(tab)
                break

        self.wait.until(
            EC.url_to_be(self.PDF_URL)
        )

        return self.driver.current_url
