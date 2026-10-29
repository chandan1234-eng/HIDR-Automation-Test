
import pytest
from pathlib import Path
from selenium import webdriver


SCREENSHOTS_DIR = Path(__file__).parent / "screenshots"


@pytest.fixture
def driver(request):
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(0)

    yield driver

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        screenshot_name = (
            f"{request.node.name}.png"
            .replace("/", "_")
            .replace("\\", "_")
        )

        screenshot_path = SCREENSHOTS_DIR / screenshot_name
        driver.save_screenshot(str(screenshot_path))

        print(f"\nFailure screenshot saved: {screenshot_path}")

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    setattr(item, f"rep_{report.when}", report)
