from selenium import webdriver
from facebook.fixture.fb_unit import Friends
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from facebook.tools.constants import WD_WAITING_TIME


class Application:
    '''
    Class for initializing browser
    '''
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.prefs = {"profile.default_content_setting_values.notifications": 2}
        self.chrome_options.add_experimental_option("prefs", self.prefs)
        self.wd = webdriver.Chrome(chrome_options=self.chrome_options,
                              executable_path='/home/posypaylo_cr/chromedriver')
        self.wd.maximize_window()
        self.friends = Friends(self)
        self.wd.get("https://www.facebook.com")


    def destroy(self):
        self.wd.quit()


    def wait_presence_of_element(self, locator, by=By.XPATH, seconds_to_wait=WD_WAITING_TIME):
        return WebDriverWait(self.wd, seconds_to_wait).until(
            EC.presence_of_element_located((by, locator)),
            'elements: "%s" was not found or was not visible during %i seconds' % (locator, seconds_to_wait))

    def wait_presence_of_elements(self, locator, by=By.XPATH, seconds_to_wait=WD_WAITING_TIME):
        return WebDriverWait(self.wd, seconds_to_wait).until(
            EC.presence_of_all_elements_located((by, locator)),
            'elements: "%s" was not found or was not visible during %i seconds' % (locator, seconds_to_wait))