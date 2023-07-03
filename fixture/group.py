from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.driver
        # Открытие страницы с группами.
        wd.find_element(By.LINK_TEXT, "groups").click()

    def create(self, abc):
        wd = self.app.driver
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
        self.app.driver.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.app.driver
        # Возврат к странице с группами.
        wd.find_element(By.LINK_TEXT, "group page").click()
