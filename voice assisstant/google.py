from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class goog():
    def __init__(self):
        
        options = webdriver.ChromeOptions()
#        options.add_argument("--headless")
        options.add_argument("start-maximized")
#        options.add_arguments("user-data-dir=C:\Users\Aryan Goel\AppData\Local\Google\Chrome\User Data\Default")
        options.add_argument("--disable-blink-features")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')

        self.driver = webdriver.Chrome(options=options)

    def google_search(self, query):
        self.query = query
        self.driver.get("https://www.google.com")

        # Wait for the search input element to be clickable
        search = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="APjFqb"]'))
        )

        search.click()

        # Wait for the search input element to be present and enter the query
        search = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="APjFqb"]'))
        )
        search.send_keys(query)
        
        
         # Find the search button element using its XPath
        enter = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'gNO89b'))
        )
        # Click the enter element
        enter.click()

        first_tag = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a/h3[1]'))
        ) 
        """ Second_tag = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/table/tbody/tr[2]/td/div/div/div/div/h3/a'))
        ) 
        third_tag = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a/h3[3]'))
        )  """
        first_tag.click()
        """ Second_tag.click()
        third_tag.click() """
        
        first_para = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/section[1]/div/div/div[2]/div/h2[1]'))
        )
        for element in self.driver.find_elements(By.XPATH, '//body'):
            print(element.text)
# Call the get_info method with the query "info"
assist = goog()
assist.google_search(query="nit")

input("Press Enter to exit...")