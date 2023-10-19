from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time
import pytest

link = "https://casenik.com.ua/"

@pytest.fixture(scope="class")
def browser():
    print("\n start Browser")
    options = ChromeOptions()
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    yield browser
    print("\n quit Browser")
    browser.quit()

@pytest.fixture(autouse=True)
def all_print():
    print("Autouse print")

class TestPage1():
    def test_number1(self, browser):
        browser.get(link)
        # знайти елемент за класом "view-all"
        view_all = browser.find_element(By.CLASS_NAME, "view-all")
        view_all.click()
        print("Show page all new products")
        wait = WebDriverWait(browser, 100)
        time.sleep(5)
        prod = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@href='product/gidrogelevaya-broneplenka-plenka-smartex-xiaomi-redmi-go']")))
        prod.click()

    def test_number2_asert(self):
        result = 5 + 7
        expected_result = 12
        assert result == expected_result, f"Result ({result}) does not correspond ({expected_result})"

    def test_number3(self, browser):
        browser.get(link)
        wait = WebDriverWait(browser, 100)
        prod = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='category/Zashitnye-stekla']")))
        prod.click()












