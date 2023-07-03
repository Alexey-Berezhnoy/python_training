from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)

    def open_home_page(self):
        wd = self.driver
        # Открытие домашней страницы адресной книги.
        wd.get("http://localhost/addressbook/")

    def open_groups_page(self):
        wd = self.driver
        # Открытие страницы с группами.
        wd.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, abc):
        wd = self.driver
        self.open_groups_page()
        # Начало создания группы.
        wd.find_element(By.NAME, "new").click()
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").send_keys(abc.aa)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").send_keys(abc.bb)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").send_keys(abc.cc)
        # Окончание создания группы.
        self.driver.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.driver
        # Возврат к странице с группами.
        wd.find_element(By.LINK_TEXT, "group page").click()

    def destroy(self):
        self.driver.quit()
