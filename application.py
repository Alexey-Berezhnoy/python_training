from selenium import webdriver
from selenium.webdriver.common.by import By
class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def open_home_page(self):
        # Открытие домашней страницы адресной книги.
        self.driver.get("http://localhost/addressbook/")

    def login(self, username, password):
        self.open_home_page()
        # Авторизация.
        self.driver.find_element(By.NAME, "user").click()
        self.driver.find_element(By.NAME, "user").click()
        self.driver.find_element(By.NAME, "user").send_keys(username)
        self.driver.find_element(By.NAME, "pass").click()
        self.driver.find_element(By.NAME, "pass").send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@value=\'Login\']").click()

    def open_groups_page(self):
        # Открытие страницы с группами.
        self.driver.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, abc):
        self.open_groups_page()
        # Начало создания группы.
        self.driver.find_element(By.NAME, "new").click()
        self.driver.find_element(By.NAME, "group_name").click()
        self.driver.find_element(By.NAME, "group_name").send_keys(abc.aa)
        self.driver.find_element(By.NAME, "group_header").click()
        self.driver.find_element(By.NAME, "group_header").send_keys(abc.bb)
        self.driver.find_element(By.NAME, "group_footer").click()
        self.driver.find_element(By.NAME, "group_footer").send_keys(abc.cc)
        # Окончание создания группы.
        self.driver.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        # Возврат к странице с группами.
        self.driver.find_element(By.LINK_TEXT, "group page").click()

    def logout(self):
        # Логаут.
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

    def destroy(self):
        self.driver.quit()