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
        time.sleep(1.5)
    except:
        pass


def random_word(length):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))

def workdayAuth(driver,user):
    #random_words = RandomWords()
    usrEmail = 'a@gmail.com'
    #for testing only
    usrEmail = user.usrEmail
    emailSeed = random_word(16)
    #usrEmail = emailSeed + usrEmail
    usrPass = 'Passsssssss123!'
    user = user.usrPass
    authInfo = "Username: {} Password: {}".format(usrEmail,usrPass)
        #frame = driver.find_element(By.ID,value='__gwt_historyFrame')
        #driver.switch_to.frame(frame)
    try:
            #accButton = WebDriverWait(driver,15).until(
            #    EC.presence_of_element_located((By.CLASS_NAME,'css-14pfav7'))
            #)
            accButton = idenAutoID(driver,"createAccountLink")
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
            try:
                submitButton = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH,"//*[@data-automation-id='click_filter']"))
                )
                #submitButton = driver.find_element(By.XPATH,"//*[@data-automation-id='click_filter']")
                submitButton.click()
                submitButton.click()
            except:
                pass
    except:
            print('Account Creation Fail')
    finally:
           print('AccountCreated')
           return authInfo



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

        #press button for if you were a previous employee
        if previousWorker != None:
            print("attempting click")
            clickRadio(driver,"2")
            #WebDriverWait(driver,3).until(EC.invisibility_of_element_located((By.XPATH,"//div[@class='blockUI blockOverlay']")))
            #invis = idenAutoID(driver,"//*[@class='css-1utp272']")
            #invis.click()
            #notPrevious = driver.find_element(By.XPATH, "//*[@class='css-1utp272']")
            #notPrevious.click()
        
        addressLine = driver.find_element(By.XPATH, "//*[@data-automation-id='addressSection_addressLine1']")
        cityLine = driver.find_element(By.XPATH, "//*[@data-automation-id='addressSection_city']")
        postalLine = driver.find_element(By.XPATH, "//*[@data-automation-id='addressSection_postalCode']")
        fnameLine = driver.find_element(By.XPATH, "//*[@data-automation-id='legalNameSection_firstName']")
        lnameLine = driver.find_element(By.XPATH, "//*[@data-automation-id='legalNameSection_lastName']")
        phoneType = driver.find_element(By.XPATH, "//*[@data-automation-id='phone-device-type']")
        phoneNumber = driver.find_element(By.XPATH, "//*[@data-automation-id='phone-number']")
        county = driver.find_element(By.XPATH, "//*[@data-automation-id='addressSection_regionSubdivision1']")
        addressLine.send_keys(usrAddress)
        cityLine.send_keys(usrCity)
        postalLine.send_keys(usrPostal)
        phoneNumber.send_keys(usrPhone)
        fnameLine.send_keys(usrFname)
        lnameLine.send_keys(usrLname)
        county.send_keys(usrCounty)
        setUsrState(driver,"addressSection_countryRegion",usrState)      
        phoneType.send_keys('m')
        phoneType.send_keys(Keys.ENTER)

        #selectListItem("//*[@data-automation-id='phone-device-type']","//*[text()='Mobile']","//*[@data-automation-id='contactInformationPage']",driver)
        #selectListItem("//*[@data-automation-id='addressSection_countryRegion']","//*[text()='Washington']","//*[@data-automation-id='contactInformationPage']",driver)
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
    #element.click()
    #driver.execute_script("arguments[0].setAttribute('aria-label', 'State {} Required'); arguments[0].innerHTML = '{}';".format(newAria,newAria), element)
    #direcctInput = driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div/div/div[3]/div[2]/div[7]/div[3]/div/div/div/input")
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
    #button_ids = [button.get_attribute("id") for button in questionElements]
    #button_arias = [button.get_attribute("aria-label") for button in questionElements]
    #element_arias = [ for button in questionElements]
    answers = getAnswers()
    
    for element in questionElements:
        time.sleep(.5)
        element_aria = element.get_attribute("aria-label")
        element_question = checkQuestions(element_aria)
        try:
            answerDropdown(element,question_answers[element_question])
        except:
            #answer is not within question dict so guess
            answerDropdown(element,"b")
            #answerDropdown(element,"y")

        #answerDropdown(element,True)
        driver.execute_script("arguments[0].scrollIntoView();", element)
    
    
    #submitButton(driver)
    

    
        
  

def addExperience(driver,jobs,resumePath):
    actions = ActionChains(driver)
    usrDescription = "A fun fast paced environment where I performed software development and devOps duties"
    w1 = workExpData("042005","042005","Consultant","Workday","United States",usrDescription,True)
    w2 = workExpData("042005","042005","Consultant2","Workday2","United States",usrDescription,False)

    #workExpData = ["042005","042005","Consultant","Workday","United States",usrDescription,True]
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
    #create a function to add websites

    #actions.move_to_element(addWorkButton).perform()



    #Generate dynamic work experince boxes 
    #Get the xpath for each elment in the dynamically gnerated boxes
    #fillDateRange(driver)

    #if currentJob:
    #    print("current")
    #    currentJob = driver.find_element(By.XPATH, "//*[@data-automation-id='currentlyWorkHere']")
    #    currentJob.click()
   # titleBox = driver.find_element(By.XPATH, "//*[@data-automation-id='jobTitle']")
    #titleBox.send_keys(usrJobTitle)
    #companyBox = driver.find_element(By.XPATH, "//*[@data-automation-id='company']")
    #companyBox.send_keys(usrCompany)
    #locationBox = driver.find_element(By.XPATH, "//*[@data-automation-id='location']")
    #locationBox.send_keys(usrLocation)
    #descriptionBox = driver.find_element(By.XPATH, "//*[@data-automation-id='location']")
    #descriptionBox.send_keys(usrDescription)



def fillDateRange(driver):
    fromDateBox = driver.find_element(By.XPATH, "//*[@data-automation-id='dateSectionMonth-input']")
    #fromDateBox.click()
    #fromDateBox.click()
    fromDateBox.send_keys("42006")
    fromDateBox.send_keys(Keys.TAB)
    fromDateBox.send_keys(Keys.TAB)
    fromDateBox.send_keys("42007")

def fillEEO(driver,questAns):
    checkBoxes = idenCheckBoxes(driver)
    answerCheckbox(checkBoxes)
    #submitButton(driver)

def acceptAgreement(driver):
    agrementBox = idenAutoID(driver,"agreementCheckbox")
    agrementBox.click()

def engineInit(site):
    service = FirefoxService(executable_path=GeckoDriverManager().install())
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Firefox(service=service,options=options)
    driver.get(site[0])
    return driver


def importSites(args):
        #get directory of file for site names
    siteFile = args.a
    sites = []
    sites = readFile(siteFile)
    return sites

def checkManualButton(driver):
    applyManually = idenAutoID(driver,"applyManually")
    if applyManually != None:
        applyManually.click()
    else:
        print("Button not there")

def fillVoluntary(driver):
    acceptAgreement(driver)

def parseInput():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a',type=str,required=True,help='provides input for addresses')
    parser.add_argument('-r',type=str,required=False,help='provide a json file for user data input')
    args = parser.parse_args()
    
    return importSites(args)
