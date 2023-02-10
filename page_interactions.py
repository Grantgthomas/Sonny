
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import argparse

import string
import os
import time
import random

from iden import * 
from interpret_questions import getAnswers,checkQuestions,answerDropdown,answerCheckbox
from create_dynamics import *



def submitButton(driver):
    wait = WebDriverWait(driver,10)
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@data-automation-id='bottom-navigation-next-button']"))).click()
        print("click")
        time.sleep(1.5)
    except:
        pass


def random_word(length):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))

def workdayAuth(driver,user):
    usrEmail = user.usrEmail
    usrPass = user.usrPass
    authInfo = "Username: {} Password: {}".format(usrEmail,usrPass)
    try:
            accButton = idenAutoID(driver,"createAccountLink")
            accButton.click()
            emailForm = WebDriverWait(driver, 10).until(

                EC.presence_of_element_located((By.XPATH,"//*[@data-automation-id='email']"))
                
            )
            emailForm.send_keys(usrEmail)
            passForm = driver.find_element(By.ID,'input-7')
            passForm.send_keys(usrPass)
            passForm = driver.find_element(By.ID,'input-8')
            passForm.send_keys(usrPass)
            try:
                createAccountCheckbox = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH,"//*[@data-automation-id='createAccountCheckbox']"))
                )
                createAccountCheckbox.click()
                time.sleep(2)
            except:
                print("No Create Checkbox")
            try:
                submitButton = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH,"//*[@data-automation-id='click_filter']"))
                )
                submitButton.click()
                submitButton.click()
                if autoIDDetected("errorMessage"):
                    try:
                        time.sleep(2)
                        existingAcc(driver,user)
                    except:
                        print("Account login failed you may have an account on this workday site already")
                        print("Please change the email in your user data file")
            except:
                pass
    except:
            print('Account Creation Fail')
    finally:
           print('Authentication Successful')
           return authInfo


def existingAcc(driver,user):
    signIn = idenAutoID(driver,"signInLink")
    signIn.click()
    emailForm = idenAutoID(driver,"email")
    passwordForm = idenAutoID(driver,"password")
    emailForm.send_keys(user.usrEmail)
    passwordForm.send_keys(user.usrPass)
    time.sleep(2)
    authenticateButton = idenAutoID(driver,"click_filter")
    WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH,"//*[@data-automation-id='click_filter']"))
    )
    authenticateButton.click()



def autoIDDetected(autoID):
   if EC.presence_of_element_located((By.XPATH,"//*[@data-automation-id='{}']".format(autoID))):
       return True
   else:
       return False

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


def checkStillExists(driver):
        try:
            if( WebDriverWait(driver,3).until(   EC.presence_of_element_located((By.XPATH,"//*[@data-automation-id='notFoundPage']")))):
                driver.quit()
                print("Page not found")
        except:
            pass




def clickRadio(driver,opt):
        RadioOpt =driver.find_element(By.XPATH,"//*[@id="+opt+"]")
        RadioOpt.send_keys(Keys.SPACE)

def fillMyInfo(driver,user):
    usrAddress = user.usrAddress
    usrCity = user.usrCity 
    usrPostal = user.usrPostal 
    usrPhone = user.usrPhone 
    usrFname = user.usrFname 
    usrLname = user.usrLname 
    usrState = user.usrState 
    usrCounty = user.usrCounty 
    try:
        searchBox = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"//*[@data-automation-id='sourceDropdown']"))
        )
        searchBox.click()
        try:
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
        except:
            searchBox.send_keys("T")
            searchBox.send_keys(Keys.ENTER)
        previousWorker = idenAutoID(driver,"previousWorker")

        if previousWorker != None:
            print("attempting click")
            clickRadio(driver,"2")

        
        addressLine = driver.find_element(By.XPATH, "//*[@data-automation-id='addressSection_addressLine1']")
        cityLine = driver.find_element(By.XPATH, "//*[@data-automation-id='addressSection_city']")
        postalLine = driver.find_element(By.XPATH, "//*[@data-automation-id='addressSection_postalCode']")
        fnameLine = driver.find_element(By.XPATH, "//*[@data-automation-id='legalNameSection_firstName']")
        lnameLine = driver.find_element(By.XPATH, "//*[@data-automation-id='legalNameSection_lastName']")
        phoneType = driver.find_element(By.XPATH, "//*[@data-automation-id='phone-device-type']")
        phoneNumber = driver.find_element(By.XPATH, "//*[@data-automation-id='phone-number']")
        county = driver.find_element(By.XPATH, "//*[@data-automation-id='addressSection_regionSubdivision1']")
        if nullValue(addressLine):
            addressLine.send_keys(usrAddress)
        if nullValue(cityLine):
            cityLine.send_keys(usrCity)
        if nullValue(postalLine):
            postalLine.send_keys(usrPostal)
        if nullValue(phoneNumber):
            phoneNumber.send_keys(usrPhone)
        if nullValue(fnameLine):
            fnameLine.send_keys(usrFname)
        if nullValue(lnameLine):
            lnameLine.send_keys(usrLname)
        if nullValue(county):
            county.send_keys(usrCounty)
        setUsrState(driver,"addressSection_countryRegion",usrState)      
        phoneType.send_keys('m')
        phoneType.send_keys(Keys.ENTER)

    except:
        searchBox =idenID(driver,"input-1")
        searchBox.click()
        try:
            searchBox =idenAutoID(driver,"sourceDropdown")
            searchBox.click()
        except:
            pass
    finally:
        submitButton(driver)
        print('myinfo filled')

def nullValue(element):
    value =element.get_attribute("value")
    if value == '':
        return True
    else:
        return False
    pass

def fillMyExperience(driver,jobs,user):
    try:
        WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@aria-label='Add Work Experience']"))
        )
        addExperience(driver,jobs,user.usrResume)
    finally:
        submitButton(driver)

def setUsrState(driver,ElementID,newAria):
    element = idenAutoID(driver,ElementID)
    element.get_attribute("aria-label")
    element.send_keys(newAria)
    element.send_keys(Keys.ENTER)
    element.send_keys(Keys.ENTER)


def useImports(import_questions,imported_answers):
    possible_questions = import_questions
    question_answers = imported_answers

class workExpData:
    def __init__(self,fromDate,toDate,jobTitle,company,location,jobDescription,currentJob):
        self.fromDate = fromDate
        self.toDate = toDate
        self.jobTitle = jobTitle
        self.company = company
        self.location = location
        self.jobDescription = jobDescription
        self.currentJob = currentJob

def appQuestions(driver,questAns):
    
    questionElements = idenAppQuestions(driver)
    answers = getAnswers()
    
    for element in questionElements:
        time.sleep(.5)
        element_aria = element.get_attribute("aria-label")
        element_question = checkQuestions(element_aria)
        try:
            answerDropdown(element,answers[element_question])
        except:
            answerDropdown(element,"b")

        driver.execute_script("arguments[0].scrollIntoView();", element)

    

    
        
  

def addExperience(driver,jobs,resumePath):
    actions = ActionChains(driver)
    workExperiences = jobs
    #workExperiences = [w1,w2,w2]
    for w in workExperiences:
        createWorkExp(driver,w)
    #Create a function to fill out education

    #create a function to fill out languages

    #create a function to fill out skills

    #Create a function to upload resume
    file_input = idenAutoID(driver,"file-upload-input-ref")
    file = os.getcwd()+"\\{}".format(resumePath)
    file_input.send_keys(file)



def fillDateRange(driver):
    fromDateBox = driver.find_element(By.XPATH, "//*[@data-automation-id='dateSectionMonth-input']")
    fromDateBox.send_keys("42006")
    fromDateBox.send_keys(Keys.TAB)
    fromDateBox.send_keys(Keys.TAB)
    fromDateBox.send_keys("42007")

def fillEEO(driver,questAns):
    checkBoxes = idenCheckBoxes(driver)
    answerCheckbox(checkBoxes)

def acceptAgreement(driver):
    agrementBox = idenAutoID(driver,"agreementCheckbox")
    agrementBox.click()





def checkManualButton(driver):
    applyManually = idenAutoID(driver,"applyManually")
    if applyManually != None:
        applyManually.click()
    else:
        print("Button not there")

def fillVoluntary(driver):
    acceptAgreement(driver)


