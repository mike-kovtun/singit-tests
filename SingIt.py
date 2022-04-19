from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Selectors




class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://singit.io/auth/login")

    def test1_login_page(self):
        self.driver.find_element(By.ID, "logo").is_displayed()
        self.driver.find_element(By.XPATH, Selectors.emailX).is_displayed()
        self.driver.find_element(By.XPATH, Selectors.passwordX).is_displayed()
        self.driver.find_element(By.ID, Selectors.login_btn_ID).is_displayed()
        self.driver.find_element(By.ID, "forget").is_displayed()

    def test2_login_process(self):
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element(By.XPATH, Selectors.emailX).send_keys(Selectors.valid_mail)
        self.driver.find_element(By.XPATH, Selectors.passwordX).send_keys(Selectors.valid_pass)
        self.driver.find_element(By.ID, Selectors.login_btn_ID).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".next")))
        while self.driver.find_element(By.CSS_SELECTOR, ".next").is_displayed():
            self.driver.find_element(By.CSS_SELECTOR, ".next").click()

    def test3_forgot_pass(self):
        self.driver.find_element(By.ID, "forget").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "wrapper").is_displayed()
        self.driver.find_element(By.XPATH, "//*[@id='wrapper']/form/input").is_displayed()
        self.driver.find_element(By.XPATH, "//*[@id='wrapper']/form/input").is_displayed()

    def tearDown(self):
        self.driver.quit()


# @unittest.skip
class Explore(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()
        self.driver.get("https://singit.io/auth/login")
        self.driver.find_element(By.XPATH, Selectors.emailX).send_keys(Selectors.valid_mail)
        self.driver.find_element(By.XPATH, Selectors.passwordX).send_keys(Selectors.valid_pass)
        self.driver.find_element(By.ID, Selectors.login_btn_ID).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".next")))
        while self.driver.find_element(By.CSS_SELECTOR, ".next").is_displayed():
            self.driver.find_element(By.CSS_SELECTOR, ".next").click()

    def test1_explore_page(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, Selectors.logoX).is_displayed()
        self.driver.find_element(By.XPATH, Selectors.notif_iconX).is_displayed()
        self.driver.find_element(By.XPATH, Selectors.most_popularX).is_displayed()
        self.driver.find_element(By.XPATH, Selectors.my_wordsX).is_displayed()
        self.driver.find_element(By.XPATH, Selectors.popular_genres_logoX).is_displayed()
        self.driver.find_element(By.XPATH, Selectors.popular_genresX).is_displayed()
        self.driver.find_element(By.XPATH, Selectors.recently_played_logoX).is_displayed()
        self.driver.find_element(By.XPATH, Selectors.recently_playedX).is_displayed()

    def test2_navigation(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, Selectors.navigation_menuX)))
        self.driver.find_element(By.XPATH, Selectors.search_btnX).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Selectors.search_logoX)))
        self.driver.find_element(By.XPATH, Selectors.profile_btnX).click()
        wait.until(EC.visibility_of_element_located((By.ID, "header")))
        self.driver.find_element(By.XPATH, Selectors.explore_btnX).click()
        self.driver.find_element(By.XPATH, Selectors.logoX).is_displayed()

    def test3_notification(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, Selectors.notif_iconX)))
        self.driver.find_element(By.XPATH, Selectors.notif_iconX).click()
        self.driver.find_element(By.XPATH, Selectors.notif_menuX).is_displayed()

    @unittest.skip
    def test4_notification_song(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, Selectors.notif_iconX)))
        self.driver.find_element(By.XPATH, Selectors.notif_iconX).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[text()=' by Majestic ']").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "mat-dialog-2").is_displayed()
        self.driver.find_element(By.XPATH, "//*[text()='Listen now']").click()
        wait.until(EC.visibility_of_element_located((By.ID, "mat-dialog-4")))

    def test5_mostPopular(self):
        wait = WebDriverWait(self.driver, 10)
        time.sleep(2)
        self.driver.find_element(By.XPATH, Selectors.most_popularX).is_displayed()
        self.driver.find_element(By.XPATH, "//ion-icon[@name='chevron-forward-outline']").click()
        self.driver.find_element(By.XPATH, "//ion-icon[@name='chevron-back-outline']").click()
        self.driver.find_element(By.XPATH, "//div[@id='track-wrapper']/div").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='content']/app-track")))

    def test6_my_words(self):
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element(By.XPATH, "//*[@id='word-box']/div[1]").is_displayed()
        self.driver.find_element(By.ID, "words-wrapper").is_displayed()
        self.driver.find_element(By.XPATH, "//*[@id='words-wrapper']/app-word[1]").click()
        wait.until(EC.visibility_of_element_located((By.ID, "wrapper")))

    def test7_popular_genres(self):
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element(By.XPATH, Selectors.popular_genres_logoX).is_displayed()
        self.driver.find_element(By.XPATH, Selectors.popular_genresX).is_displayed()
        self.driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[3]/app-genre[1]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Selectors.search_barX)))
        genre_search = self.driver.find_element(By.XPATH, Selectors.search_barX)
        print(genre_search.get_attribute("value"))

    def test8_recently_played(self):
        self.driver.find_element(By.XPATH, Selectors.recently_played_logoX).is_displayed()
        self.driver.find_element(By.XPATH, Selectors.recently_playedX).is_displayed()
        self.driver.find_element(By.XPATH, "(//ion-icon[@name='chevron-forward-outline'])[3]").click()
        self.driver.find_element(By.XPATH, "(//ion-icon[@name='chevron-back-outline'])[3]").click()
        # Recently played song can be changed

    def tearDown(self):
        self.driver.quit()


# @unittest.skip
class Notification_word(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        wait = WebDriverWait(cls.driver, 10)
        cls.driver.maximize_window()
        cls.driver.get("https://dashboard.singit.io/auth/login")
        cls.driver.find_element(By.XPATH, "//*[@id='main-content']/app-login/div/form/div[2]/input").send_keys(
            "mykhailo.kovtun.work@gmail.com")
        cls.driver.find_element(By.XPATH, "//*[@id='main-content']/app-login/div/form/div[3]/input").send_keys(
            "Aa12345678")
        cls.driver.find_element(By.ID, "main-button").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='mat-dialog-0']")))
        cls.driver.find_element(By.XPATH, "//*[@id='mat-dialog-0']/app-welcome/button").click()
        cls.driver.find_element(By.XPATH, "//*[@id='sidenav']/ul/li[3]").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='filter']/button")))
        cls.driver.find_element(By.XPATH, "//*[@id='filter']/button").click()
        cls.driver.find_element(By.XPATH, "//*[@id='menu']/li[2]").click()
        time.sleep(1)
        cls.driver.find_element(By.XPATH, "//*[@id='mat-chip-list-input-0']").send_keys("hi")
        cls.driver.find_element(By.XPATH,
                                "//*[@id='mat-dialog-1']/app-send-word/form/mat-form-field[2]/div/div[1]/div[3]").click()
        time.sleep(1)
        cls.driver.find_element(By.XPATH, "//*[@id='mat-option-2']/span").click()
        time.sleep(1)
        cls.driver.find_element(By.XPATH, "//*[@id='mat-dialog-1']/app-send-word/form/button").click()
        time.sleep(1)
        cls.driver.quit()

    def setUp(self):
        self.driver = webdriver.Chrome()
        wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()
        self.driver.get("https://singit.io/auth/login")
        self.driver.find_element(By.XPATH, Selectors.emailX).send_keys(Selectors.valid_mail)
        self.driver.find_element(By.XPATH, Selectors.passwordX).send_keys(Selectors.valid_pass)
        self.driver.find_element(By.ID, Selectors.login_btn_ID).click()
        wait.until(
            EC.element_to_be_clickable((By.XPATH, Selectors.new_notificationX)))
        self.driver.find_element(By.XPATH, Selectors.new_notificationX).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".next")))
        while self.driver.find_element(By.CSS_SELECTOR, ".next").is_displayed():
            self.driver.find_element(By.CSS_SELECTOR, ".next").click()

    def test1_word(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, Selectors.notif_iconX)))
        self.driver.find_element(By.XPATH, Selectors.notif_iconX).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[text()='hi ']").click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


# @unittest.skip
class Search(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()
        self.driver.get("https://singit.io/auth/login")
        self.driver.find_element(By.XPATH, Selectors.emailX).send_keys(Selectors.valid_mail)
        self.driver.find_element(By.XPATH, Selectors.passwordX).send_keys(Selectors.valid_pass)
        self.driver.find_element(By.ID, Selectors.login_btn_ID).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".next")))
        while self.driver.find_element(By.CSS_SELECTOR, ".next").is_displayed():
            self.driver.find_element(By.CSS_SELECTOR, ".next").click()
        self.driver.find_element(By.XPATH, Selectors.search_btnX).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Selectors.search_logoX)))

    def test1_search_page(self):
        self.driver.find_element(By.XPATH, Selectors.search_logoX).is_displayed()
        self.driver.find_element(By.NAME, "searchBar").is_displayed()
        self.driver.find_element(By.XPATH, Selectors.search_historyX).is_displayed()

    def test2_searching(self):
        self.driver.find_element(By.NAME, "searchBar").send_keys("hi")
        time.sleep(1)
        self.driver.find_element(By.XPATH, Selectors.searched_wordX).is_displayed()
        self.driver.find_element(By.ID, "words-row").is_displayed()
        self.driver.find_element(By.XPATH, Selectors.searched_tracksX).is_displayed()
        self.driver.find_element(By.ID, "content-wrapper").is_displayed()

    def test3_word_searching(self):
        self.driver.find_element(By.NAME, "searchBar").send_keys("hi")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='words-row']/app-word[1]/span")))
        self.driver.find_element(By.XPATH, "//*[@id='words-row']/app-word[1]/span").click()
        wait.until(EC.visibility_of_element_located((By.ID, "wrapper")))
        self.driver.find_element(By.ID, "wrapper").is_displayed()

    def test4_song_searching(self):
        self.driver.find_element(By.NAME, "searchBar").send_keys("hi")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='content-wrapper']/app-track-small[1]")))

    def tearDown(self):
        self.driver.quit()


# @unittest.skip
class Profile(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()
        self.driver.get("https://singit.io/auth/login")
        self.driver.find_element(By.XPATH, Selectors.emailX).send_keys(Selectors.valid_mail)
        self.driver.find_element(By.XPATH, Selectors.passwordX).send_keys(Selectors.valid_pass)
        self.driver.find_element(By.ID, Selectors.login_btn_ID).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".next")))
        while self.driver.find_element(By.CSS_SELECTOR, ".next").is_displayed():
            self.driver.find_element(By.CSS_SELECTOR, ".next").click()
        self.driver.find_element(By.XPATH, "//*[@id='buttons-wrapper']/div[3]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='header']/h1")))

    def test1_profile_page(self):
        self.driver.find_element(By.XPATH, Selectors.profile_logoX).is_displayed()
        self.driver.find_element(By.XPATH, Selectors.profile_nameX).is_displayed()
        self.driver.find_element(By.ID, "stats").is_displayed()
        self.driver.find_element(By.XPATH, Selectors.edit_profileX).is_displayed()
        self.driver.find_element(By.XPATH, Selectors.contact_usX).is_displayed()
        self.driver.find_element(By.XPATH, Selectors.privacy_policyX).is_displayed()
        self.driver.find_element(By.XPATH, Selectors.accessibility_policyX).is_displayed()
        self.driver.find_element(By.XPATH, Selectors.cancel_subscriptionX).is_displayed()
        self.driver.find_element(By.XPATH, Selectors.log_outX).is_displayed()
        self.driver.find_element(By.ID, "support-wrapper").is_displayed()

    def test2_edit_profile_page(self):
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element(By.XPATH, Selectors.edit_profileX).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Selectors.firstnameX)))
        self.driver.find_element(By.XPATH, Selectors.firstnameX).is_displayed()
        self.driver.find_element(By.XPATH, Selectors.lastnameX).is_displayed()
        self.driver.find_element(By.XPATH, Selectors.edit_emailX).is_displayed()
        self.driver.find_element(By.XPATH, Selectors.languageX).is_displayed()
        self.driver.find_element(By.XPATH, Selectors.allow_explicit_lyricsX).is_displayed()
        self.driver.find_element(By.XPATH, Selectors.show_player_when_quiz_appearsX).is_displayed()
        self.driver.find_element(By.XPATH, Selectors.pause_the_song_when_translatingX).is_displayed()
        self.driver.find_element(By.XPATH, Selectors.update_profile_btnX).is_displayed()

    def test3_editing_profile(self):
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element(By.XPATH, Selectors.edit_profileX).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Selectors.firstnameX)))
        self.driver.find_element(By.XPATH, Selectors.firstname_barX).clear()
        self.driver.find_element(By.XPATH, Selectors.firstname_barX).send_keys("Autotest")
        self.driver.find_element(By.XPATH, Selectors.lastname_barX).clear()
        self.driver.find_element(By.XPATH, Selectors.lastname_barX).send_keys("Testingtest")
        self.driver.find_element(By.XPATH, Selectors.email_barX).clear()
        self.driver.find_element(By.XPATH, Selectors.email_barX).send_keys("auto-testingtest@singit.io")
        self.driver.find_element(By.ID, Selectors.language_dropdownX).click()
        self.driver.find_element(By.CSS_SELECTOR, "#mat-option-0 > .mat-option-text").click()
        self.driver.find_element(By.XPATH, "//ion-toggle").click()
        self.driver.find_element(By.XPATH, "//div[2]/ion-toggle").click()
        self.driver.find_element(By.XPATH, "//div[3]/ion-toggle").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,'Update')]").click()
        time.sleep(1)
        print(self.driver.find_element(By.XPATH, Selectors.firstname_barX).get_attribute("value"))
        print(self.driver.find_element(By.XPATH, Selectors.lastname_barX).get_attribute("value"))
        print(self.driver.find_element(By.XPATH, Selectors.email_barX).get_attribute("value"))
        print(self.driver.find_element(By.XPATH, "//ion-toggle").is_enabled())
        print(self.driver.find_element(By.XPATH, "//div[2]/ion-toggle").is_enabled())
        time.sleep(1)
        self.driver.find_element(By.XPATH, Selectors.firstname_barX).clear()
        self.driver.find_element(By.XPATH, Selectors.firstname_barX).send_keys("Auto")
        self.driver.find_element(By.XPATH, Selectors.lastname_barX).clear()
        self.driver.find_element(By.XPATH, Selectors.lastname_barX).send_keys("Testing")
        self.driver.find_element(By.XPATH, Selectors.email_barX).clear()
        self.driver.find_element(By.XPATH, Selectors.email_barX).send_keys("auto-testing@singit.io")
        self.driver.find_element(By.ID, Selectors.language_dropdownX).click()
        self.driver.find_element(By.CSS_SELECTOR, "#mat-option-4 > span").click()
        self.driver.find_element(By.XPATH, "//ion-toggle").click()
        self.driver.find_element(By.XPATH, "//div[2]/ion-toggle").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,'Update')]").click()
        time.sleep(1)

    # sending does not work
    @unittest.skip
    def test4_contact_us(self):
        self.driver.find_element(By.XPATH, "//*[@id='links']/li[2]").click()
        self.driver.find_element(By.ID, "wrapper").is_displayed()
        self.driver.find_element(By.XPATH, "//*[@id='wrapper']/form/select").click()
        self.driver.find_element(By.XPATH, "//*[@id='wrapper']/form/select/option[6]").click()
        self.driver.find_element(By.XPATH, "//*[@id='wrapper']/form/textarea").send.keys("Autotest")
        self.driver.find_element(By.XPATH, "//*[@id='buttons']/button").click()

    def test5_privacy_policy(self):
        self.driver.find_element(By.XPATH, Selectors.privacy_policyX).click()
        self.driver.find_element(By.XPATH, "//*[@id='wrapper']/p[1]").is_displayed()

    def test6_accessibility_policy(self):
        self.driver.find_element(By.XPATH, Selectors.accessibility_policyX).click()
        self.driver.find_element(By.XPATH, "//*[@id='wrapper']").is_displayed()

    def test7_cancel_subscription(self):
        self.driver.find_element(By.XPATH, Selectors.cancel_subscriptionX).click()
        self.driver.find_element(By.XPATH, "//*[@id='wrapper']").is_displayed()

    def test8_logout(self):
        self.driver.find_element(By.XPATH, Selectors.log_outX).click()
        self.driver.find_element(By.ID, "logo").is_displayed()

    def tearDown(self):
        self.driver.quit()


# @unittest.skip
class Words(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()
        self.driver.get("https://singit.io/auth/login")
        self.driver.find_element(By.XPATH, Selectors.emailX).send_keys(Selectors.valid_mail)
        self.driver.find_element(By.XPATH, Selectors.passwordX).send_keys(Selectors.valid_pass)
        self.driver.find_element(By.ID, Selectors.login_btn_ID).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".next")))
        while self.driver.find_element(By.CSS_SELECTOR, ".next").is_displayed():
            self.driver.find_element(By.CSS_SELECTOR, ".next").click()

    def test1_word_popup(self):
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element(By.XPATH, "//*[@id='words-wrapper']/app-word[1]/span").click()
        wait.until(EC.visibility_of_element_located((By.ID, "wrapper")))
        self.driver.find_element(By.XPATH, "//*[@id='main-wrapper']/h1").is_displayed()
        self.driver.find_element(By.XPATH, "//*[@id='main-wrapper']/h3").is_displayed()
        try:
            self.driver.find_element(By.XPATH, "//*[@id='wrapper']/div[2]/ion-slides/div/ion-slide/div").is_displayed()
        except NoSuchElementException:
            print("There is no 'Definition'")

        self.driver.find_element(By.ID, "example-header").is_displayed()
        self.driver.find_element(By.ID, "expand").click()
        self.driver.find_element(By.ID, "expand").click()

    def tearDown(self):
        self.driver.quit()


# @unittest.skip
class Lessons(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        wait = WebDriverWait(cls.driver, 10)
        cls.driver.maximize_window()
        cls.driver.get("https://dashboard.singit.io/auth/login")
        cls.driver.find_element(By.XPATH, "//*[@id='main-content']/app-login/div/form/div[2]/input").send_keys(
            "mykhailo.kovtun.work@gmail.com")
        cls.driver.find_element(By.XPATH, "//*[@id='main-content']/app-login/div/form/div[3]/input").send_keys(
            "Aa12345678")
        cls.driver.find_element(By.ID, "main-button").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='mat-dialog-0']")))
        cls.driver.find_element(By.XPATH, "//*[@id='mat-dialog-0']/app-welcome/button").click()
        cls.driver.get('https://dashboard.singit.io/marketplace/619280583acdf03bcc59cede')
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-details']/div[1]/button[1]")))
        cls.driver.find_element(By.XPATH, "//*[@id='main-details']/div[1]/button[1]").click()
        time.sleep(1)
        cls.driver.find_element(By.XPATH, "//*[@id='wrapper']/div[2]/mat-form-field/div/div[1]/div[3]").click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mat-option-2']/span")))
        cls.driver.find_element(By.XPATH, "//*[@id='mat-option-2']/span").click()
        time.sleep(1)
        cls.driver.find_element(By.XPATH, "//*[@id='wrapper']/div[3]/button[1]").click()
        time.sleep(1)
        cls.driver.quit()

    def setUp(self):
        self.driver = webdriver.Chrome()
        wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()
        self.driver.get("https://singit.io/auth/login")
        self.driver.find_element(By.XPATH, Selectors.emailX).send_keys(Selectors.valid_mail)
        self.driver.find_element(By.XPATH, Selectors.passwordX).send_keys(Selectors.valid_pass)
        self.driver.find_element(By.ID, Selectors.login_btn_ID).click()

    def test1_lesson_play(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.element_to_be_clickable((By.XPATH, Selectors.new_notificationX)))
        self.driver.find_element(By.XPATH, Selectors.new_notificationX).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".next")))
        while self.driver.find_element(By.CSS_SELECTOR, ".next").is_displayed():
            self.driver.find_element(By.CSS_SELECTOR, ".next").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, Selectors.notif_iconX)))
        self.driver.find_element(By.XPATH, Selectors.notif_iconX).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='mat-menu-panel-0']/div/ul/li[1]/div")))
        self.driver.find_element(By.XPATH, "//*[@id='mat-menu-panel-0']/div/ul/li[1]").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, Selectors.play_songX)))
        self.driver.find_element(By.XPATH, Selectors.play_songX).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, Selectors.cont_lessX)))
        self.driver.find_element(By.XPATH, "//*[@id='white-wrapper']/div").is_displayed()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mat-dialog-5']/app-track-tour/div/div[2]/span")))
        self.driver.find_element(By.XPATH, "//*[@id='mat-dialog-5']/app-track-tour/div/div[2]/span").click()

    def test2_lesson_menu(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".next")))
        while self.driver.find_element(By.CSS_SELECTOR, ".next").is_displayed():
            self.driver.find_element(By.CSS_SELECTOR, ".next").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, Selectors.notif_iconX)))
        self.driver.find_element(By.XPATH, Selectors.notif_iconX).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='mat-menu-panel-0']/div/ul/li[1]/div")))
        self.driver.find_element(By.XPATH, "//*[@id='mat-menu-panel-0']/div/ul/li[1]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Selectors.play_songX)))
        time.sleep(2)
        self.driver.find_element(By.XPATH, Selectors.vocabulary_quizX).is_displayed()
        self.driver.find_element(By.XPATH, Selectors.speaking_quizX).is_displayed()
        self.driver.find_element(By.XPATH, Selectors.grammar_testX).is_displayed()
        self.driver.find_element(By.XPATH, Selectors.unseenX).is_displayed()
        self.driver.find_element(By.XPATH, Selectors.word_pauseX).is_displayed()
        self.driver.find_element(By.XPATH, Selectors.fill_blanksX).is_displayed()
        self.driver.find_element(By.ID, "words-section").is_displayed()
        self.driver.find_element(By.XPATH, Selectors.go_back_btnX).is_displayed()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
