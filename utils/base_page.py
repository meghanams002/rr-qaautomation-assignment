from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_texts(self, locator):
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return [el.text for el in self.driver.find_elements(*locator)]

