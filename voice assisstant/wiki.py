from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyttsx3 as p

engine = p.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

class infow():
    def __init__(self):
        
        options = webdriver.ChromeOptions()
#        options.add_argument("--headless")
        options.add_argument("start-maximized")
#        options.add_arguments("user-data-dir=C:\Users\Aryan Goel\AppData\Local\Google\Chrome\User Data\Default")
        options.add_argument("--disable-blink-features")
        options.add_argument("--disable-blink-features=AutomationControlled")
#        options.add_argument('--ignore-ssl-errors=yes')
#        options.add_argument('--ignore-certificate-errors')

        self.driver = webdriver.Chrome(options=options)

    def get_info(self, query):
        self.query = query
        self.driver.get("https://en.wikipedia.org/wiki/Main_Page")

        # Wait for the search input element to be clickable
        search = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'cdx-text-input__input'))
        )

        search.click()

        # Wait for the search input element to be present and enter the query
        search = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'cdx-text-input__input'))
        )
        search.send_keys(query)
        
        
         # Find the search button element using its XPath
        enter = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="searchform"]/div/button'))
        )
        # Click the enter element
        enter.click()


       # Wait for the element with the specified XPath to be present
       #To read first element
        result_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="siteSub"]'))
        ) 

        # Get the text content of the element and pass it to the speak function
        text_to_read = result_element.text
        speak(text_to_read)
# Call the get_info method with the query "info"

""" assist = infow()
assist.get_info(query="nit")

input("Press Enter to exit...") """
 
