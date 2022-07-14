
from selenium import webdriver
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from dotenv import dotenv_values

config = dotenv_values(".env")

#enter time to login 
logintime = config["LOGINTIME"]
username = config["USERNAME"]
password = config["PASSWORD"]

#enter time to wait for
starttime = config["STARWARTIME"]
cdate = datetime.strftime(datetime.now(), "%d-%m-%Y")


options = webdriver.ChromeOptions()
#options.add_argument("--start-maximized")
options.add_argument('--log-level=3')

# Provide the path of chromedriver present on your system.
driver = webdriver.Chrome(executable_path="chromedriver",
                            options=options)
driver.set_window_size(1920,1080)

# Send a get request to the url
driver.get('https://wish.wis.ntu.edu.sg/pls/webexe/ldap_login.login?w_url=https://wish.wis.ntu.edu.sg/pls/webexe/aus_stars_planner.main')

pressed = False
while(not pressed):
    print("waiting to login :" + str(datetime.now()))
    
    if (datetime.now() > datetime.strptime(cdate + " " + logintime, "%d-%m-%Y %H:%M:%S")):
        # click submit button
        try:
            
            #enter username box
            elem = WebDriverWait(driver, 0.1).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/section[2]/div/div/center[1]/form/table/tbody/tr/td/table/tbody/tr[2]/td[2]/input"))
            )
            elem.send_keys(username)
            #show password
            elem = WebDriverWait(driver, 0.1).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/section[2]/div/div/center[1]/form/table/tbody/tr/td/table/tbody/tr[4]/td[2]/input[1]")) 
            )
            elem.click()

            #enter password box
            elem = WebDriverWait(driver, 0.1).until(
            EC.presence_of_element_located((By.XPATH, "//html/body/div[3]/div/div/section[2]/div/div/form/center[1]/table/tbody/tr/td/table/tbody/tr[3]/td[2]/input"))
            )
            elem.send_keys(password)
            #enter starplanner
            elem = WebDriverWait(driver, 0.1).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/section[2]/div/div/form/center[1]/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]")) 
            )
            elem.click()
        finally:
            pressed = True



pressed = False
while(not pressed):
    print("Waiting for add timing:" + str(datetime.now()))
    
    if (datetime.now() > datetime.strptime(cdate + " " + starttime, "%d-%m-%Y %H:%M:%S")):
        # click submit button
        try:
            # submit_button = driver.find_elements_by_xpath("/html/body/form[2]/div/div[3]/div/div/section[2]/div/div/p/table/tbody/tr[1]/td[2]/table/tbody/tr[11]/td/form/input[1]")[0]
            # submit_button.click()


            #add courses (critical point) test with print
            # elem = WebDriverWait(driver, 0.2).until(
            # EC.presence_of_element_located((By.XPATH, "/html/body/form[2]/div/div[3]/div/div/section[2]/div/div/p/table/tbody/tr[1]/td[2]/table/tbody/tr[9]/td/input"))
            # )
            # elem.click()
            
            #add courses (critical point)
            elem = WebDriverWait(driver, 0.2).until(
            #EC.presence_of_element_located((By.XPATH, "/html/body/form[2]/div/div[3]/div/div/section[2]/div/div/p/table/tbody/tr[1]/td[2]/table/tbody/tr[10]/td/form/input[1]"))
            EC.presence_of_element_located((By.XPATH, "/html/body/form[2]/div/div[3]/div/div/section[2]/div/div/p/table/tbody/tr[1]/td[2]/table/tbody/tr[12]/td/form/input[1]"))
            )
            elem.click()
            #/html/body/form[2]/div/div[3]/div/div/section[2]/div/div/p/table/tbody/tr[1]/td[2]/table/tbody/tr[12]/td/form/input[1]

            #comfirm courses (comment out for less speed more reliablility)
            elem = WebDriverWait(driver, 0.1).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/form/div[3]/div/div/section[2]/div/div/input[1]")) #This is a dummy element
            )
            elem.click()
        finally:
            pressed = True
       


