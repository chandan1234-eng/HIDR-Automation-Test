
from pages.career_page import CareerPage


def test_join_team_opens_career_openings(driver):
    career_page = CareerPage(driver)

    career_page.open_career_page()
    career_page.click_join_team()
    career_page.verify_career_openings()
