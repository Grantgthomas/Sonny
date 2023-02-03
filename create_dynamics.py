from iden import * 
from create_dynamics import *
from lib2to3.pgen2.driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time



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
    time.sleep(2.1)
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

def createEdu(driver):
    #put this one on hold
    schoolData = "Purdue University"
    gpaData = "3.00"
    fromDate = "022000"
    toDate = "022004"
    

    try:
        addEduButton = driver.find_element(By.XPATH, "//*[@aria-label='Add Education']")
    except:
        addEduButton = driver.find_element(By.XPATH, "//*[@aria-label='Add Another Education']")
    addEduButton.click()
    degreeInput = driver.find_elements(By.XPATH, "//*[@data-automation-id='degree']")
    schoolInput = driver.find_elements(By.XPATH, "//*[@data-automation-id='school']")
    gpalInput = driver.find_elements(By.XPATH, "//*[@data-automation-id='gpa']")
    schoolInput.send_keys(schoolData)
    gpalInput.send_keys(gpaData)
    degreeInput.send_keys("B")
    degreeInput.send_keys(Keys.ENTER)
    dateBoxes = driver.find_elements(By.XPATH,"//*[@data-automation-id='dateSectionMonth-input']")
    dateBoxes[len(dateBoxes)-2].send_keys(fromDate)
    dateBoxes[len(dateBoxes)-1].send_keys(toDate)