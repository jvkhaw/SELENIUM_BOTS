import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,TimeoutException,WebDriverException
import os


from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import platform


class TLM_prospector:
    def __init__(self,browser='Chrome'):
        # self.driver = self.create_web_driver()
        self.driver =self.create_brave_chromium_driver()       
        self.webdriverwait = WebDriverWait(self.driver,60)

    def create_brave_chromium_driver(self):
        # driver_path = os.path.join(os.path.dirname(__file__),'chromedriver.exe') # location of your chromedriver

        brave_path = {
        'Linux':"/usr/bin/brave-browser-stable",
        'Windows':"C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"} # location of your Brave browser

        s = Service(ChromeDriverManager().install())
        option = webdriver.ChromeOptions()
        option.add_argument('log-level=3')
        option.add_experimental_option('excludeSwitches', ['enable-logging'])
        option.binary_location = brave_path[platform.system()]

        d = DesiredCapabilities.CHROME
        d['goog:loggingPrefs'] = { 'browser':'ALL' }

        driver = webdriver.Chrome(service=s, options=option, desired_capabilities=d)
        return driver

    def create_web_driver(self):                
        try:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            return driver
        except WebDriverException:            
            print("Can't find Chrome browser... Fallback to Firefox")
            pass # Fallback to Firefox
        try:
            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
            return driver
        except WebDriverException:
            print("Can't find Firefox browser... Fallback to Edge")
            pass # Fallback to Edge
        try:
            driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        except WebDriverException:
            print('Holy smokes please install either Chrome, Firefox or Edge on your computer!!')

    def go_to_website(self,URL,identifier):
        try:
            self.driver.get(URL)
            return True
        except AssertionError as e:
            print(f'Couldnt go to {identifier}. Error:\n{e}')
            return False

    def click_button(self,xpath,identifier,new_window=False):
        if new_window:
            main_window_handle = self.driver.current_window_handle
            for wh in self.driver.window_handles:
                if wh != main_window_handle:
                    self.driver.switch_to.window(wh)
                    break
        try:
            button = self.webdriverwait.until(EC.element_to_be_clickable((By.XPATH,xpath)))
            button.click()
            if new_window:
                self.driver.switch_to.window(main_window_handle)
            return True
        except AssertionError as e:
            print(f"Couldnt click {identifier} button. Error:\n{e}")
            return False
        
    def login_to_wax_dashboard(self):    
        url_to_be = self.webdriverwait.until(EC.url_to_be("https://wallet.wax.io/dashboard"))
        return url_to_be

    def pop_up_window(self):
        window_is_opened = self.webdriverwait.until(EC.new_window_is_opened(self.driver.window_handles))
        return window_is_opened

    def wait_for_time(self):            
        hours = self.webdriverwait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[3]/div[1]/div/div[3]/div[5]/div[2]/p[1]/span[1]')))
        minutes = self.webdriverwait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[3]/div[1]/div/div[3]/div[5]/div[2]/p[1]/span[2]')))
        seconds = self.webdriverwait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[3]/div[1]/div/div[3]/div[5]/div[2]/p[1]/span[3]')))
        # do stuff    
        time_available = int(hours.text) * 60 * 60 + int(minutes.text) * 60 + int(seconds.text)
        return time_available

    def get_cpu_trilium(self):
        trilium = self.webdriverwait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[3]/div[1]/div/div[3]/div[1]/div/div[2]/p[1]')))
        cpu = self.webdriverwait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[3]/div[2]/div[1]/div/div/div[2]/div/div/div[10]/div[1]/div[1]/p[2]')))
        print(f'Trilium: {trilium.text}   CPU: {cpu.text}')

        
    def waiting_stale(self):
        staleness = self.webdriverwait.until(EC.staleness_of(
            self.driver.find_element(By.XPATH,'//*[@id="root"]/div[3]/div[1]/div/div[3]/div[5]/div[2]/div/div/div'))
                              )
        return staleness

    # def click_discord_button(self):    
    #     try:
    #         discord_button = self.webdriverwait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="discord-social-btn"]')))
    #         discord_button.click()
    #         return True
    #     except AssertionError as e:
    #         print(f"Couldnt click discord button. Error:\n{e}")
    #         return False

    def click_approve():
        try:
            start_now_button = self.webdriverwait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/section/div[2]/div/div[6]/button')))
            start_now_button.click()
            driver.switch_to.window(main_window_handle)
            return True
        except AssertionError as e:
            print(f"Couldnt click Approve button. Error:\n{e}")
            return False
    def click_sign():
        main_window_handle = driver.current_window_handle
        for wh in driver.window_handles:
            if wh != main_window_handle:
                driver.switch_to.window(wh)
                break
        try:
            sign_button = self.webdriverwait.until(EC.element_to_be_clickable((By.XPATH,)))
            sign_button.click()
            driver.switch_to.window(main_window_handle)
            return True
        except AssertionError as e:
            print(f"Couldnt click discord button. Error:\n{e}")
            return False

        
    def click_start_now():
        try:
            start_now_button = self.webdriverwait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[3]/div/div[1]/div/div')))
            start_now_button.click()
            return True
        except AssertionError as e:
            print(f"Couldnt click Start Now button. Error:\n{e}")
            return False

    def click_mine():
        try:
            mine_button = self.webdriverwait.until(EC.element_to_be_clickable((By.XPATH,)))
            mine_button.click()
            return True
        except AssertionError as e:
            print(f"Couldnt click discord button. Error:\n{e}")
            return False
        
    def MINE_SETUP(self):    
        print('Going to wax website...',end=' ')
        print(self.go_to_website('https://wallet.wax.io/','WAX'))
        print('Authorizing WAX Login and/or 2FA...',end=' ')
        print(self.login_to_wax_dashboard())
        print('Going to Alien Worlds...',end=' ')    
        print(self.go_to_website('https://play.alienworlds.io/','Alien Worlds'))
        print('Clicking Start Now...',end=' ')
        print(self.click_button('//*[@id="root"]/div[3]/div/div[1]/div/div','Start Now'))
        print('Waiting for Approve pop-up window...',end=' ')
        print(self.pop_up_window())
        print('Clicking Approve wallet...',end=' ')
        print(self.click_button('//*[@id="root"]/div/section/div[2]/div/div[6]/button','Approve WAX wallet',new_window=True))

    def MINE_LOOP(self):           
        
        # print('Waiting for time to appear...',end=' ')
        # waiting_time = self.wait_for_time()
        # print(waiting_time)
        # time.sleep(waiting_time)
        try:
            while True:
                try: 
                    self.get_cpu_trilium()
                    print('Waiting for time to appear...',end=' ')
                    waiting_time = self.wait_for_time()
                    print(waiting_time)
                    time.sleep(waiting_time)
                except:
                    pass
                try:
                    print('Clicking mine...',end=' ')
                    print(self.click_button('//*[@id="root"]/div[3]/div[1]/div/div[3]/div[5]/div[2]/div/div/div','Mine'))
                    print('Waiting Mine staleness',end=' ')
                    print(self.waiting_stale())
                    print('Clicking claim mine...',end=' ')
                    print( self.click_button('//*[@id="root"]/div[3]/div[1]/div/div[3]/div[5]/div[2]/div/div/div','Claim'))
                    print('Waiting for claim mine approve window...',end=' ')
                    print(self.pop_up_window())
                    print('Clicking approve transaction...',end=' ')
                    print(self.click_button('//*[@id="root"]/div/section/div[2]/div/div[5]/button','Approve Transaction',new_window=True))
                except Exception as e:
                    print(e)
                    self.driver.refresh()
        except:
            RESUME_KEY = 'TLMFTW'
            while RESUME_KEY != '':
                RESUME_KEY = input("\n\n\nSomething went wrong. Press ENTER to continue.\n\n\n")
            self.driver.refresh()
            self.MINE_LOOP()

if __name__ == '__main__':
    TLMillionaire = TLM_prospector()
    TLMillionaire.MINE_SETUP()
    TLMillionaire.MINE_LOOP()