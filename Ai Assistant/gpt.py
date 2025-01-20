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

    def google_search(self, gmail, password):
        self.gmail = gmail
        self.password = password
        self.driver.get("https://chat.openai.com/")
        wait = WebDriverWait(self.driver, 10)
        #Click on lgin button
        login=wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[1]/div/div/button[1]'))
        )
        login.click
        
        # Wait for the gmail input element to be clickable
        search = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))
        )

        search.click()

        # Wait for the gmail input element to be present and enter the email
        search = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))
        )
        search.send_keys(gmail)
        
                # Wait for the gmail input element to be clickable
        cont_but = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))
        )

        cont_but.click()

        # Wait for the gmail input element to be present and enter the email
        search = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
        )
        search.send_keys(password)
        
        
         # Find the search button element using its XPath
        login = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'gNO89b'))
        )
        # Click the login element
        login.click()

#        first_tag = wait.until(
#            EC.presence_of_element_located((By.XPATH, '//a/h3[1]'))
#        ) 
        """ Second_tag = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/table/tbody/tr[2]/td/div/div/div/div/h3/a'))
        ) 
        third_tag = wait.until(
            EC.presence_of_element_located((By.XPATH, '//a/h3[3]'))
        )  """
#        first_tag.click()
        """ Second_tag.click()
        third_tag.click() """
        
        """ first_para = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/section[1]/div/div/div[2]/div/h2[1]'))
        )
        for element in self.driver.find_elements(By.XPATH, '//body'):
            print(element.text) """
# Call the get_info method with the gmail "info"
assist = goog()
assist.google_search(gmail="aryangoel299@gmail.com", password="Multiman22971H")

input("Press Enter to exit...")