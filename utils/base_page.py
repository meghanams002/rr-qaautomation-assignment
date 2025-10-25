from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def get_elements(self, locator):
        return self.driver.find_elements(*locator)

    def get_texts(self, locator):
        elements = self.get_elements(locator)
        return [e.text for e in elements]

    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
