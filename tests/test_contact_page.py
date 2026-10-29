
import json
from pathlib import Path

import pytest

from pages.contact_page import ContactPage


DATA_FILE = (
    Path(__file__).resolve().parents[1]
    / "test_data"
    / "test_data.json"
)

with open(DATA_FILE, "r", encoding="utf-8") as file:
    TEST_DATA = json.load(file)


@pytest.fixture
def contact_page(driver):
    page = ContactPage(driver)
    page.open_contact_page()
    return page


# POSITIVE TESTING

def test_contact_form_accepts_valid_data(contact_page):
    data = TEST_DATA["valid_contact_data"]

    contact_page.fill_contact_form(
        data["name"],
        data["email"],
        data["phone"],
        data["message"]
    )

    assert contact_page.is_form_valid() is True


def test_name_accepts_spaces(contact_page):
    name = TEST_DATA["valid_contact_data"]["name"]

    contact_page.enter_name(name)

    assert contact_page.get_field_value(
        ContactPage.NAME_INPUT
    ) == name


def test_email_accepts_valid_email(contact_page):
    email = TEST_DATA["valid_contact_data"]["email"]

    contact_page.enter_email(email)

    assert contact_page.get_field_validity(
        ContactPage.EMAIL_INPUT
    ) is True


def test_phone_accepts_valid_input(contact_page):
    phone = TEST_DATA["valid_contact_data"]["phone"]

    contact_page.enter_phone(phone)

    assert contact_page.get_field_value(
        ContactPage.PHONE_INPUT
    ) == phone


def test_message_accepts_text(contact_page):
    message = TEST_DATA["valid_contact_data"]["message"]

    contact_page.enter_message(message)

    assert contact_page.get_field_value(
        ContactPage.MESSAGE_INPUT
    ) == message


# NEGATIVE TESTING

def test_email_rejects_invalid_format(contact_page):
    data = TEST_DATA["invalid_email_data"]

    contact_page.fill_contact_form(
        data["name"],
        data["email"],
        data["phone"],
        data["message"]
    )

    assert contact_page.get_field_validity(
        ContactPage.EMAIL_INPUT
    ) is False


# FUNCTIONAL TESTING

def test_contact_page_opens_successfully(contact_page):
    assert contact_page.driver.current_url == ContactPage.CONTACT_URL


def test_all_contact_form_fields_are_visible(contact_page):
    assert contact_page.get_field(ContactPage.NAME_INPUT).is_displayed()
    assert contact_page.get_field(ContactPage.EMAIL_INPUT).is_displayed()
    assert contact_page.get_field(ContactPage.PHONE_INPUT).is_displayed()
    assert contact_page.get_field(ContactPage.MESSAGE_INPUT).is_displayed()
    assert contact_page.get_field(ContactPage.SUBMIT_BUTTON).is_displayed()


def test_submit_button_is_enabled(contact_page):
    assert contact_page.get_field(
        ContactPage.SUBMIT_BUTTON
    ).is_enabled()
