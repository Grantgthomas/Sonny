import argparse
import csv
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random_word import RandomWords


#def readFile(dir):
    
def readFile(file):
    rows =[]
    with open(file,newline='') as addrs:
        addReader = csv.reader(addrs, delimiter=' ')
        for row in addReader:
            rows.append(row)
    return rows


def workdayAuth(driver,sites):
    random_words = RandomWords()
    usrEmail = '@gmail.com'
    #for testing only
    
    emailSeed = random_words.get_random_word()
    usrEmail = emailSeed + usrEmail
    usrPass = 'Passsssssss123!'
    for address in sites:
        driver.get(address[0])
        #frame = driver.find_element(By.ID,value='__gwt_historyFrame')
        #driver.switch_to.frame(frame)
        try:
            accButton = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.CLASS_NAME,'css-14pfav7'))
            )
            accButton.click()
            emailForm = WebDriverWait(driver, 10).until(
            #emailForm = driver.find_element(By.ID,value='input-4')
                #EC.presence_of_element_located((By.ID,'input-6'))
                EC.presence_of_element_located((By.XPATH,"//*[@data-automation-id='email']"))
                
            )
            emailForm.send_keys(usrEmail)
            #passForm = driver.find_element(by=By.XPATH,value='//*[@id="input-4"]')
            passForm = driver.find_element(By.ID,'input-7')
            #emai = driver.find_element(By.XPATH,"//*[@_data-automation-id='email']")
            passForm.send_keys(usrPass)
            passForm = driver.find_element(By.ID,'input-8')
            passForm.send_keys(usrPass)
            submitButton = driver.find_element(By.XPATH,"//*[@data-automation-id='click_filter']")
            submitButton.click()
            submitButton.click()
        finally:
           print('AccountCreated')

def fillMyInfo(driver):
    usrAddress = "132 North Mulberry St."
    usrCity = "Portland"
    usrPostal = "11204"
    usrPhone = "7378084776"
    usrFname = "G"
    usrLname = "T"
    try:
        searchBox = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"//*[@id='input-1']"))
        )
        searchBox.click()
        searchBox = driver.find_element(By.XPATH, "//*[@data-automation-label='Social Media']")
        searchBox.click()
        searchBox = driver.find_element(By.XPATH, "//*[@data-automation-label='Twitter']")
        searchBox.click()

        addressLine = driver.find_element(By.XPATH, "//*[@data-automation-id='addressSection_addressLine1']")
        cityLine = driver.find_element(By.XPATH, "//*[@data-automation-id='addressSection_city']")
        stateLine = driver.find_element(By.XPATH, "//*[@data-automation-id='addressSection_countryRegion']")
        postalLine = driver.find_element(By.XPATH, "//*[@data-automation-id='addressSection_postalCode']")
        fnameLine = driver.find_element(By.XPATH, "//*[@data-automation-id='legalNameSection_firstName']")
        lnameLine = driver.find_element(By.XPATH, "//*[@data-automation-id='legalNameSection_lastName']")
        phoneLine = driver.find_element(By.XPATH, "//*[@data-automation-id='phone-device-type']")
        phoneNumber = driver.find_element(By.XPATH, "//*[@data-automation-id='phone-number']")

        addressLine.send_keys(usrAddress)
        cityLine.send_keys(usrCity)
        postalLine.send_keys(usrPostal)
        phoneNumber.send_keys(usrPhone)
        fnameLine.send_keys(usrFname)
        lnameLine.send_keys(usrLname)

        stateLine.click()
        stateLine = driver.find_element(By.XPATH, "//*[text()='Washington']")
        stateLine.click()
        
        phoneLine.click()
        phoneLine = driver.find_element(By.XPATH, "//*[text()='Mobile']")
        phoneLine.click()

    finally:
        submitButton = driver.find_element(By.XPATH, "//*[@data-automation-id='bottom-navigation-next-button']")
        submitButton.click
        
        print('myinfo filled')


def main():
    #define arguments to run
    parser = argparse.ArgumentParser()
    parser.add_argument('-a',type=str,required=True,help='provides input for addresses')
    args = parser.parse_args()

    #get directory of file for site names
    siteFile = args.a
    sites = []
    sites = readFile(siteFile)

    service = FirefoxService(executable_path=GeckoDriverManager().install())
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Firefox(service=service,options=options)

    workdayAuth(driver,sites)
    #driver.get('https://pscu.wd5.myworkdayjobs.com/en-US/PSCUCareers/login?redirect=%2Fen-US%2FPSCUCareers%2Fjob%2FRemote-USA%2FSr-IT-Security-Compliance-Analyst---Remote_5194%2Fapply%2FapplyManually%3Fjbsrc%3D1018%26source%3DLinkedin')
    fillMyInfo(driver)
    
    
       




    


if __name__ == "__main__":
    main()
    