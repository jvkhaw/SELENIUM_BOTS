
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException

class SELENIUM_BOT:
	def __init__(self,
		driver_path,
		binary_path
		):

		s = Service(driver_path)

		option = webdriver.ChromeOptions()
		option.add_argument('log-level=3')
		option.add_experimental_option('excludeSwitches', ['enable-logging'])
		option.binary_location = brave_path
				
		d = DesiredCapabilities.CHROME
		d['goog:loggingPrefs'] = { 'browser':'ALL' }
		
		self.driver = webdriver.Chrome(service=s, options=option, desired_capabilities=d)
	
	def goto(self,website):
		self.driver.get(website)

	def wait_to_click_xpath(self,xpath,wait):
		element = WebDriverWait(
			self.driver,
			wait,
			ignored_exceptions=(NoSuchElementException,StaleElementReferenceException)).until(
				EC.element_to_be_clickable((By.XPATH,xpath)))
		time.sleep(1)
		element.click()

class Alien_Worlds_Bot(SELENIUM_BOT):
	def __init__(self,
		driver_path,
		binary_path):
		super().__init__(driver_path,
		binary_path)

	def WAX_login(self):
		self.goto("https://wallet.wax.io/")
		self.wait_to_click_xpath('//*[@id="discord-social-btn"]',10)

		# print('Waiting for QR code: ...')
		

		# https://discord.com/oauth2/authorize
		print('Waiting for 2FA: ...')

		while True:
			if self.driver.current_url.startswith("https://wallet.wax.io/dashboard"):
				print('Logged In Wax!')
				break;
			time.sleep(1)

	def AW_login(self):
		self.goto("https://play.alienworlds.io/")		
		self.wait_to_click_xpath('//*[@id="root"]/div[3]/div/div[1]/div/div',10)
		self.switch_window()
		self.wait_to_click_xpath('//*[@id="root"]/div/section/div[2]/div/div[6]/button',10)
		self.switch_window()


		while True:
			if self.driver.current_url.startswith("https://play.alienworlds.io/inventory"):
				print('Logged In Alien Worlds!')
				break;
			time.sleep(1)

	def mine(self):
		# Mine
		print('Mining...')
		self.wait_to_click_xpath('//*[@id="root"]/div[3]/div[1]/div/div[3]/div[5]/div[2]/div/div/div/div',10)
		# Claim
		time.sleep(5)
		print('Claiming mine...')
		self.wait_to_click_xpath('//*[@id="root"]/div[3]/div[1]/div/div[3]/div[5]/div[2]/div/div/div/div',20)
		# Authorize wax wallet
		self.switch_window()
		self.wait_to_click_xpath('//*[@id="root"]/div/section/div[2]/div/div[5]/button',10)
		self.switch_window()

		# hours = self.driver.find_elements(
		# 	By.XPATH,
		# 	'/html/body/div/div[3]/div[1]/div/div[3]/div[5]/div[2]/p[1]/span[1]')[0].text
		
		time.sleep(20)
		
		hours = self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div[1]/div/div[3]/div[5]/div[2]/p[1]/span[1]')
		hours = hours.text

		# minutes = self.driver.find_element() WebDriverWait(self.driver, 20).until(
		# 	EC.visibility_of_element_located(
		minutes = self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div[1]/div/div[3]/div[5]/div[2]/p[1]/span[2]')
		minutes = minutes.text
		# 	)
		# ).get_attribute("text")

		# seconds = WebDriverWait(self.driver, 20).until(
		# 	EC.visibility_of_element_located(
		seconds = self.driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div[1]/div/div[3]/div[5]/div[2]/p[1]/span[3]')
		seconds = seconds.text
		# 	)
		# ).get_attribute("text")

		# print(hours,minutes,seconds)
		total_time_in_seconds =  int(hours) * 60 * 60 + int(minutes) * 60 + int(seconds)
		print(total_time_in_seconds)
		return total_time_in_seconds

	def switch_window(self):
		while len(self.driver.window_handles) == 1:
			time.sleep(1)	
		main_window_handle = self.driver.current_window_handle
		for wh in self.driver.window_handles:
			if wh != main_window_handle:
				self.driver.switch_to.window(wh)
				break;		


if __name__ == "__main__":
	driver_path = "C:/Driver/chromedriver.exe" # location of your chromedriver
	brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe" # location of your Brave browser

	awbot=Alien_Worlds_Bot(driver_path=driver_path,
		binary_path=brave_path)
	awbot.WAX_login()
	awbot.AW_login()
	while True:
		mining_time = awbot.mine()
		time.sleep(mining_time)