
from pages.header_component import HeaderComponent, BASE_URL


# Logo and Home navigation

def test_logo_redirects_to_home_page(driver):
    driver.get(f"{BASE_URL}/about")

    header = HeaderComponent(driver)
    header.click_logo()


def test_home_navigation(driver):
    driver.get(f"{BASE_URL}/about")

    header = HeaderComponent(driver)
    header.click_home()


# Who We Are dropdown

def test_who_we_are_dropdown_opens(driver):
    driver.get(BASE_URL)

    header = HeaderComponent(driver)
    header.open_who_we_are_menu()


def test_about_us_navigation(driver):
    driver.get(BASE_URL)

    header = HeaderComponent(driver)
    header.open_who_we_are_menu()
    header.click_about_us()


def test_what_we_offer_navigation(driver):
    driver.get(BASE_URL)

    header = HeaderComponent(driver)
    header.open_who_we_are_menu()
    header.click_what_we_offer()


def test_our_team_navigation(driver):
    driver.get(BASE_URL)

    header = HeaderComponent(driver)
    header.open_who_we_are_menu()
    header.click_our_team()


# Opportunities dropdown

def test_opportunities_dropdown_opens(driver):
    driver.get(BASE_URL)

    header = HeaderComponent(driver)
    header.open_opportunities_menu()


def test_career_navigation(driver):
    driver.get(BASE_URL)

    header = HeaderComponent(driver)
    header.open_opportunities_menu()
    header.click_career()


def test_partner_navigation(driver):
    driver.get(BASE_URL)

    header = HeaderComponent(driver)
    header.open_opportunities_menu()
    header.click_partner()


# Publications dropdown

def test_publications_dropdown_opens(driver):
    driver.get(BASE_URL)

    header = HeaderComponent(driver)
    header.open_publications_menu()


def test_report_navigation(driver):
    driver.get(BASE_URL)

    header = HeaderComponent(driver)
    header.open_publications_menu()
    header.click_report()


def test_policy_brief_navigation(driver):
    driver.get(BASE_URL)

    header = HeaderComponent(driver)
    header.open_publications_menu()
    header.click_policy_brief()


def test_annual_report_navigation(driver):
    driver.get(BASE_URL)

    header = HeaderComponent(driver)
    header.open_publications_menu()
    header.click_annual_report()


def test_all_publications_navigation(driver):
    driver.get(BASE_URL)

    header = HeaderComponent(driver)
    header.open_publications_menu()
    header.click_all_publications()


def test_book_navigation(driver):
    driver.get(BASE_URL)

    header = HeaderComponent(driver)
    header.open_publications_menu()
    header.click_book()


# Blog navigation

def test_blog_navigation(driver):
    driver.get(BASE_URL)

    header = HeaderComponent(driver)
    header.click_blog()
