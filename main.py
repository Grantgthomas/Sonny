import argparse
import csv
import string
import os
import time
import random
from iden import * 
from create_dynamics import *
#from interpret_questions import possible_questions,question_answers
from interpret_questions import *
from import_data import *
from page_interactions import *
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



#def readFile(dir):
    


def main():
    #define arguments to run
    #run parser
    sites = parseInput()
    
    global possible_questions
    global question_answers
    #import user data
    user,jobs,questAns= importUsrInfo("usrDataModel.json")
    import_questions,imported_answers = getImports(questAns)
    possible_questions = import_questions
    question_answers = imported_answers
    for site in sites:
        #try 3 times 
        successful = True
        for x in range(3):
            driver = engineInit(site)
            try:
                
                #get directory of file for site names
                authInfo =workdayAuth(driver,user)
                #driver.get('https://pscu.wd5.myworkdayjobs.com/en-US/PSCUCareers/login?redirect=%2Fen-US%2FPSCUCareers%2Fjob%2FRemote-USA%2FSr-IT-Security-Compliance-Analyst---Remote_5194%2Fapply%2FapplyManually%3Fjbsrc%3D1018%26source%3DLinkedin')
                #time.sleep(3.2)
                checkStillExists(driver)
                fillMyInfo(driver,user)
                fillMyExperience(driver,jobs,user)
                #time.sleep(1.5)
                appQuestions(driver,questAns)
                submitButton(driver)
                #time.sleep(1.5)
                appQuestions(driver,questAns)
                fillEEO(driver,questAns)
                submitButton(driver)
                
                appQuestions(driver,questAns)
                fillVoluntary(driver)
                submitButton(driver)
                submitButton(driver)
                break
            except:
                successful =False
                driver.quit()
                pass
    
        if successful:
            print("Application Submitted for job: {}".format(site))
            print("Access your application with the following info: {}".format(authInfo))
        else:
            print("Failed to submit application for: {}".format(site))
        
    


if __name__ == "__main__":
    main()
    