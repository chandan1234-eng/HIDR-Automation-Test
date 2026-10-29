
from pages.reports_page import ReportsPage


def test_report_link_opens_pdf(driver):
    page = ReportsPage(driver)

    page.open_reports_page()
    page.click_report_link()
