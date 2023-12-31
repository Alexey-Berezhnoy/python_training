# Generated by Selenium IDE
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTestaddgroup():
    def test_testaddgroup(self):
        self.open_home_page()
        self.login()
        self.open_groups_page()
        self.create_group()
        self.return_to_groups_page()
        self.logout()

    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def logout(self):
        # Логаут.
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_groups_page(self):
        # Возврат к странице с группами.
        self.driver.find_element(By.LINK_TEXT, "group page").click()

    def create_group(self):
        # Начало создания группы.
        self.driver.find_element(By.NAME, "new").click()
        self.driver.find_element(By.NAME, "group_name").click()
        self.driver.find_element(By.NAME, "group_name").send_keys("Name_group01")
        self.driver.find_element(By.NAME, "group_header").click()
        self.driver.find_element(By.NAME, "group_header").send_keys("group_header01")
        self.driver.find_element(By.NAME, "group_footer").click()
        self.driver.find_element(By.NAME, "group_footer").send_keys("group_footer01")
        # Окончание создания группы.
        self.driver.find_element(By.NAME, "submit").click()

    def open_groups_page(self):
        # Открытие страницы с группами.
        self.driver.find_element(By.LINK_TEXT, "groups").click()

    def login(self):
        # Авторизация.
        self.driver.find_element(By.NAME, "user").click()
        self.driver.find_element(By.NAME, "user").click()
        self.driver.find_element(By.NAME, "user").send_keys("admin")
        self.driver.find_element(By.NAME, "pass").click()
        self.driver.find_element(By.NAME, "pass").send_keys("secret")
        self.driver.find_element(By.XPATH, "//input[@value=\'Login\']").click()

    def open_home_page(self):
        # Открытие домашней страницы адресной книги.
        self.driver.get("http://localhost/addressbook/")
