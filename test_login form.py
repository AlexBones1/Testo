from selenium import webdriver
from selenium.webdriver.common.by import By
from group import Group
link = "https://testpages.herokuapp.com/styled/validation/input-validation.html"


class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite..")
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(30)

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite..")
        self.browser.quit()

    def test_fill_fields(self, group):
        self.browser.get(link)
        self.browser.find_element(By.ID, "firstname").send_keys(group.firstname)
        self.browser.find_element(By.ID, "surname").send_keys(group.surname)
        self.browser.find_element(By.ID, "age").send_keys(group.age)
        self.browser.find_element(By.ID, "notes").send_keys(group.notes)

    def test_submit(self):
        self.browser.find_element(By.CSS_SELECTOR, '[type="submit"]')


