from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options

# Set Chrome options to run in headless mode
chrome_options = Options()
chrome_options.add_argument('--headless')

# Instantiate the Chrome driver with the headless options
driver = webdriver.Chrome()
share_name = 'دي'

driver.get("http://www.tsetmc.com/Loader.aspx?ParTree=15")

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, "search"))).click()
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, "SearchKey"))).send_keys(share_name)
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='SearchResult']/div/div[2]/table/tbody/tr[1]/td[1]/a"))).click()
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, "dbp")))
print(f'your share price is {element.text}')
