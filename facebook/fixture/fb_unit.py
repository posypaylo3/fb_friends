from selenium.webdriver.common.by import By
from facebook.tools.general_helper import ClickHelper
from facebook.tools.constants import EMAIL, PASSWORD


class Friends(ClickHelper):
    def __init__(self, app):
        self.app = app
        self.wd = app.wd
        self.email = lambda: self.app.wait_presence_of_element('email', By.ID)
        self.password = lambda: self.app.wait_presence_of_element('pass', By.ID)
        self.loginbtn = lambda: self.app.wait_presence_of_element('loginbutton', By.ID)
        self.profile = lambda: self.app.wait_presence_of_element('//a[@title="Profile" or @title="Профиль"]')
        self.friends_btn = lambda: self.app.wait_presence_of_element('//a[text()="Friends" or text()="Друзья"]')
        self.number_of_friends = lambda: self.app.wait_presence_of_element('//a[@name="All friends" or @name="Все друзья"]/span[2]')
        self.movies_block = lambda: self.wd.find_elements_by_id('pagelet_timeline_medley_movies')
        self.friends = lambda: self.app.wait_presence_of_elements('//div[@data-testid="friend_list_item"]')


    def login(self):
        self._fill(self.email, EMAIL)
        self._fill(self.password, PASSWORD)
        self.loginbtn().click()


    def open_friends_page(self):
        self.profile().click()
        self.friends_btn().click()


    def check_friends(self):
        self.friends_counter = self.number_of_friends().text
        print('Friends counted by facebook: {}'.format(self.friends_counter))


    def scroll_page_count_friends(self):
        count = 50
        while not len(self.movies_block()):
            if count == 0:
                break
            else:
                self.wd.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                count -= 1
        counted_friends = len(self.friends())
        print('Friends counted with selenium: {}'.format(counted_friends))


