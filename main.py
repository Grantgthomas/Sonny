import argparse
import csv
import string
import random
from lib2to3.pgen2.driver import Driver
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random_word import RandomWords
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



#def readFile(dir):
    
def readFile(file):
    rows =[]
    with open(file,newline='') as addrs:
        addReader = csv.reader(addrs, delimiter=' ')
        for row in addReader:
            rows.append(row)
    return rows

def submitButton(driver):
    wait = WebDriverWait(driver,10)
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@data-automation-id='bottom-navigation-next-button']"))).click()
        print("click")
    except:
        pass

    #submitButton = driver.find_element(By.XPATH, "//*[@data-automation-id='bottom-navigation-next-button']")
    #submitButton.click
    #submitButton.click

def random_word(length):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))

def workdayAuth(driver,sites):
    #random_words = RandomWords()
    usrEmail = '@gmail.com'
    #for testing only
    
    emailSeed = random_word(10)
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
            

            #passForm = driver.find_element(by=By.XPATH,value='//*[@id="input-4"]'))
            #emailForm = driver.find_element(By.ID,value='input-4')
                #EC.presence_of_element_located((By.ID,'input-6'))
                
            passForm = driver.find_element(By.ID,'input-7')
            #emai = driver.find_element(By.XPATH,"//*[@_data-automation-id='email']")
            passForm.send_keys(usrPass)
            passForm = driver.find_element(By.ID,'input-8')
            passForm.send_keys(usrPass)
            #Check for create account checkbox
            try:
                createAccountCheckbox = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH,"//*[@data-automation-id='createAccountCheckbox']"))
                )
                createAccountCheckbox.click()
            except:
                print("No Create Checkbox")

            submitButton = driver.find_element(By.XPATH,"//*[@data-automation-id='click_filter']")
            submitButton.click()
            submitButton.click()
        finally:
           print('AccountCreated')




def selectListItem(list,item,page,driver):
    listItemSet = False
    while(listItemSet != True):
        phoneLine = driver.find_element(By.XPATH, list)
        phoneLine.click()
        if(EC.presence_of_element_located((By.XPATH,item ))):
            phoneLine = driver.find_element(By.XPATH, item)
            phoneLine.click()
            listItemSet = True
        phoneLine = driver.find_element(By.XPATH, page)
        phoneLine.click()
        

def fillMyInfo(driver):
    usrAddress = "132 North Mulberry St."
    usrCity = "Portland"
    usrPostal = "98059"
    usrPhone = "7378084776"
    usrFname = "G"
    usrLname = "T"
    try:
        searchBox = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"//*[@id='input-1']"))
        )
        searchBox.click()
        WebDriverWait(driver,3).until(
            EC.presence_of_element_located((By.XPATH,"//*[@data-automation-label='Social Media']"))
        )
        searchBox = driver.find_element(By.XPATH, "//*[@data-automation-label='Social Media']")
        searchBox.click()
        WebDriverWait(driver,3).until(
            EC.presence_of_element_located((By.XPATH,"//*[@data-automation-label='Twitter']"))
        )
        searchBox = driver.find_element(By.XPATH, "//*[@data-automation-label='Twitter']")
        searchBox.click()
        addressLine = driver.find_element(By.XPATH, "//*[@data-automation-id='addressSection_addressLine1']")
        cityLine = driver.find_element(By.XPATH, "//*[@data-automation-id='addressSection_city']")
        postalLine = driver.find_element(By.XPATH, "//*[@data-automation-id='addressSection_postalCode']")
        fnameLine = driver.find_element(By.XPATH, "//*[@data-automation-id='legalNameSection_firstName']")
        lnameLine = driver.find_element(By.XPATH, "//*[@data-automation-id='legalNameSection_lastName']")
        phoneType = driver.find_element(By.XPATH, "//*[@data-automation-id='phone-device-type']")
        phoneNumber = driver.find_element(By.XPATH, "//*[@data-automation-id='phone-number']")
        addressLine.send_keys(usrAddress)
        cityLine.send_keys(usrCity)
        postalLine.send_keys(usrPostal)
        phoneNumber.send_keys(usrPhone)
        fnameLine.send_keys(usrFname)
        lnameLine.send_keys(usrLname)      
        phoneType.send_keys('Mobile')
        phoneType.click()

        #selectListItem("//*[@data-automation-id='phone-device-type']","//*[text()='Mobile']","//*[@data-automation-id='contactInformationPage']",driver)
        #selectListItem("//*[@data-automation-id='addressSection_countryRegion']","//*[text()='Washington']","//*[@data-automation-id='contactInformationPage']",driver)
    finally:
        submitButton(driver)
        print('myinfo filled')

def fillMyExperience(driver):
    resumeName = "Grant_Resume.pdf"
    try:
        WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@aria-label='Add Work Experience']"))
        )
        addExperience(driver,True)
    finally:
        submitButton(driver)

def createWorkExp(driver,workExpData):
    fromDate = workExpData.fromDate
    toDate = workExpData.toDate
    usrJobTitle = workExpData.jobTitle
    usrCompany = workExpData.company
    usrLocation = workExpData.location
    currentJob = workExpData.currentJob
    usrDescription = workExpData.jobDescription
    #find the button for work exp

    try:
        addWorkButton = driver.find_element(By.XPATH, "//*[@aria-label='Add Work Experience']")
    except:
        addWorkButton = driver.find_element(By.XPATH, "//*[@aria-label='Add Another Work Experience']")

    addWorkButton.click()
    jobTitleInput = driver.find_elements(By.XPATH, "//*[@data-automation-id='jobTitle']")
    companyInput = driver.find_elements(By.XPATH, "//*[@data-automation-id='company']")
    locationTitleInput = driver.find_elements(By.XPATH, "//*[@data-automation-id='location']")
    descriptionInput = driver.find_elements(By.XPATH, "//*[@data-automation-id='description']")
    
    #find the last two date range boxes
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,"//*[@data-automation-id='dateSectionMonth-input']")))
    dateBoxes = driver.find_elements(By.XPATH,"//*[@data-automation-id='dateSectionMonth-input']")
    dateBoxes[len(dateBoxes)-2].send_keys(fromDate)
    dateBoxes[len(dateBoxes)-1].send_keys(toDate)
    if(currentJob):
        currentJobBox = driver.find_element(By.XPATH,"//*[@data-automation-id='currentlyWorkHere']")
        currentJobBox.click()
    jobTitleInput[len(jobTitleInput)-1].send_keys(usrJobTitle)
    companyInput[len(companyInput)-1].send_keys(usrCompany)
    locationTitleInput[len(locationTitleInput)-1].send_keys(usrLocation)
    descriptionInput[len(descriptionInput)-1].send_keys(usrDescription)
    driver.execute_script("arguments[0].scrollIntoView();", descriptionInput[len(descriptionInput)-1])



class workExpData:
    def __init__(self,fromDate,toDate,jobTitle,company,location,jobDescription,currentJob):
        self.fromDate = fromDate
        self.toDate = toDate
        self.jobTitle = jobTitle
        self.company = company
        self.location = location
        self.jobDescription = jobDescription
        self.currentJob = currentJob


def addExperience(driver,currentJob):
    actions = ActionChains(driver)
    usrDescription = "A fun fast paced environment where I performed software development and devOps duties"
    w1 = workExpData("042005","042005","Consultant","Workday","United States",usrDescription,True)
    w2 = workExpData("042005","042005","Consultant2","Workday2","United States",usrDescription,False)

    #workExpData = ["042005","042005","Consultant","Workday","United States",usrDescription,True]
    workExperiences = [w1,w2,w2]
    for w in workExperiences:
        createWorkExp(driver,w)
    #Create a function to fill out education

    #create a function to fill out languages

    #create a function to fill out skills

    #Create a function to upload resume

    #create a function to add websites

    #actions.move_to_element(addWorkButton).perform()



    #Generate dynamic work experince boxes 
    #Get the xpath for each elment in the dynamically gnerated boxes
    #fillDateRange(driver)

    if currentJob:
        print("current")
        currentJob = driver.find_element(By.XPATH, "//*[@data-automation-id='currentlyWorkHere']")
        currentJob.click()
    titleBox = driver.find_element(By.XPATH, "//*[@data-automation-id='jobTitle']")
    titleBox.send_keys(usrJobTitle)
    companyBox = driver.find_element(By.XPATH, "//*[@data-automation-id='company']")
    companyBox.send_keys(usrCompany)
    locationBox = driver.find_element(By.XPATH, "//*[@data-automation-id='location']")
    locationBox.send_keys(usrLocation)
    descriptionBox = driver.find_element(By.XPATH, "//*[@data-automation-id='location']")
    descriptionBox.send_keys(usrDescription)



def fillDateRange(driver):
    fromDateBox = driver.find_element(By.XPATH, "//*[@data-automation-id='dateSectionMonth-input']")
    #fromDateBox.click()
    #fromDateBox.click()
    fromDateBox.send_keys("42006")
    fromDateBox.send_keys(Keys.TAB)
    fromDateBox.send_keys(Keys.TAB)
    fromDateBox.send_keys("42007")

    

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
    fillMyExperience(driver)


if __name__ == "__main__":
    main()
    