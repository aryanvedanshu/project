from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class youtube():
    def __init__(self):
        options = webdriver.ChromeOptions()
#        options.add_argument("--headless")
        options.add_argument("start-maximized")
        options.add_argument("--disable-blink-features")
        options.add_argument("--disable-blink-features=AutomationControlled")
#        options.add_argument('--ignore-ssl-errors=yes')
#        options.add_argument('--ignore-certificate-errors')

        self.driver = webdriver.Chrome(options=options)

    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query="+query)

    # Find the search button element using its XPath and click it
        enter = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="thumbnail"]/yt-image/img'))
        )
        enter.click()

# TESTING CODE
""" 
play_vid = youtube()
play_vid.play("bats")
input("Press Enter to exit...")
 """