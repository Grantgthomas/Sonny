from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def idenAppQuestions(driver):
    button_elements = driver.find_elements(By.XPATH,"//*[@aria-haspopup='{}']".format("listbox"))
    #button_ids = [button.get_attribute("id") for button in button_elements]
    #button_arias = [button.get_attribute("aria-label") for button in button_elements]
    return button_elements

def idenCheckBoxes(driver):
    box_elements = driver.find_elements(By.XPATH,"//*[@type='{}']".format("checkbox"))
    return box_elements 

def idenAutoID(driver,ID):
    try:
        if (WebDriverWait(driver,6).until(EC.presence_of_element_located((By.XPATH, "//*[@data-automation-id='"+ID+"']")))):
            element = driver.find_element(By.XPATH, "//*[@data-automation-id='"+ID+"']")
            return element
    except:
        print("Element not found ID"+ID)
        pass
            
def idenID(driver,ID):
    try:
        if (WebDriverWait(driver,6).until(EC.presence_of_element_located((By.XPATH, "//*[@ID'{}']".format(ID))))):
            element = driver.find_element(By.XPATH, "//*[@ID'{}']".format(ID))
            return element
    except:
        print("Element not found ID"+ID)
        pass



