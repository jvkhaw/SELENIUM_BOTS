import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,TimeoutException

driver_path = "C:/Users/ruben/Desktop/SELENIUM_BOTS/chromedriver.exe" # location of your chromedriver
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe" # location of your Brave browser

s = Service(driver_path)

option = webdriver.ChromeOptions()
option.add_argument('log-level=3')
option.add_experimental_option('excludeSwitches', ['enable-logging'])
option.binary_location = brave_path

d = DesiredCapabilities.CHROME
d['goog:loggingPrefs'] = { 'browser':'ALL' }

driver = webdriver.Chrome(service=s, options=option, desired_capabilities=d)


wait = WebDriverWait(driver,60)
def go_to_wax():
    try:
        driver.get("https://wallet.wax.io/")
        return True
    except AssertionError as e:
        print(f"Couldnt go to WAX. Error:\n{e}")
        return False

def click_discord_button():    
    try:
        discord_button = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="discord-social-btn"]')))
        discord_button.click()
        return True
    except AssertionError as e:
        print(f"Couldnt click discord button. Error:\n{e}")
        return False
    
def login_to_wax_dashboard():    
    url_to_be = wait.until(EC.url_to_be("https://wallet.wax.io/dashboard"))
    return url_to_be

def go_to_aw():
    try:
        driver.get("https://play.alienworlds.io/")
        return True
    except AssertionError as e:
        print(f"Couldnt go to AW. Error:\n{e}")
        return False
    
def click_start_now():
    try:
        start_now_button = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[3]/div/div[1]/div/div')))
        start_now_button.click()
        return True
    except AssertionError as e:
        print(f"Couldnt click Start Now button. Error:\n{e}")
        return False
    
def approve_window():
    window_is_opened = wait.until(EC.new_window_is_opened(driver.window_handles))
    return window_is_opened

def click_approve():
    main_window_handle = driver.current_window_handle
    for wh in driver.window_handles:
        if wh != main_window_handle:
            driver.switch_to.window(wh)
            break
    try:
        start_now_button = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/section/div[2]/div/div[6]/button')))
        start_now_button.click()
        driver.switch_to.window(main_window_handle)
        return True
    except AssertionError as e:
        print(f"Couldnt click Approve button. Error:\n{e}")
        return False
    
def click_mine():
    try:
        mine_button = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[3]/div[1]/div/div[3]/div[5]/div[2]/div/div/div')))
        mine_button.click()
        return True
    except AssertionError as e:
        print(f"Couldnt click discord button. Error:\n{e}")
        return False

def waiting_stale():
    staleness = wait.until(EC.staleness_of(
        driver.find_element(By.XPATH,'//*[@id="root"]/div[3]/div[1]/div/div[3]/div[5]/div[2]/div/div/div'))
                          )
    return staleness

def sign_window():
    window_is_opened = wait.until(EC.new_window_is_opened(driver.window_handles))
    return window_is_opened

def click_sign():
    main_window_handle = driver.current_window_handle
    for wh in driver.window_handles:
        if wh != main_window_handle:
            driver.switch_to.window(wh)
            break
    try:
        sign_button = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/section/div[2]/div/div[5]/button')))
        sign_button.click()
        driver.switch_to.window(main_window_handle)
        return True
    except AssertionError as e:
        print(f"Couldnt click discord button. Error:\n{e}")
        return False
    
def wait_for_time():    
    while True:
        try:        
            hours = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[3]/div[1]/div/div[3]/div[5]/div[2]/p[1]/span[1]')))
            minutes = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[3]/div[1]/div/div[3]/div[5]/div[2]/p[1]/span[2]')))
            seconds = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[3]/div[1]/div/div[3]/div[5]/div[2]/p[1]/span[3]')))
        # do stuff
        except TimeoutException:
            print('Couldnt get time... refreshing')
            driver.refresh()
        else:
            break

    time_available = int(hours.text) * 60 * 60 + int(minutes.text) * 60 + int(seconds.text)
    return time_available

def get_cpu_trilium():
    trilium = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[3]/div[1]/div/div[3]/div[1]/div/div[2]/p[1]')))
    cpu = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[3]/div[2]/div[1]/div/div/div[2]/div/div/div[10]/div[1]/div[1]/p[2]')))
    print(f'Trilium: {trilium}   CPU: {cpu}')

print('Going to wax website...',end=' ')
print(go_to_wax())
print('Clicking Discord button...',end=' ')
print(click_discord_button())
print('Authorizing Discord & 2FA...',end=' ')
print(login_to_wax_dashboard())
print('Going to Alien Worlds...',end=' ')
print(go_to_aw())
print('Clicking Start Now...',end=' ')
print(click_start_now())
print('Waiting for approve window...',end=' ')
print(approve_window())
print('Clicking wallet...',end=' ')
print(click_approve())
while True:
    print('Clicking mine...',end=' ')
    print(click_mine())
    print('Waiting Mine staleness',end=' ')
    print(waiting_stale())
    print('Claiming mine...',end=' ')
    print(click_mine())
    print('Signing window...',end=' ')
    print(sign_window())
    print('Clicking sign...',end=' ')
    print(click_sign())
    get_cpu_trilium()
    print('Waiting for time to appear...',end=' ')
    waiting_time = wait_for_time()
    print(waiting_time)
    time.sleep(waiting_time)
    