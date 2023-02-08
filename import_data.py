import json
from types import SimpleNamespace
from collections import namedtuple

class WorkExp:
    jobDescription = "A fun fast paced environment where I performed software development and devOps duties"
    currentJob = True
    fromDate ="042005"
    toDate = "042005"
    jobTitle = "Consultant"
    jobCompany ="Workday"
    jobCountry = "United States"
    ID = "0"

    def __init__(self,ID,jobDescription,currentJob,dateStarted,dateEnded,jobTitle,jobCompany,jobCountry):
        self.ID = ID
        self.jobDescription = jobDescription
        self.currentJob = currentJob
        self.dateStarted = dateStarted
        self.dateEnded = dateEnded
        self.jobTitle = jobTitle
        self.jobCompany = jobCompany
        self.jobCountry = jobCountry

    @classmethod
    def json_init(classInstance,objData):
            return classInstance(objData["ID"],objData["jobDescription"],objData["currentJob"],objData["dateEnded"],objData["dateStarted"],objData["jobTitle"],objData["jobCompany"],objData["jobCountry"])









class User:
    #data for application
    usrEmail = "email@gmail.com"
    usrPass = 'Passsssssss123!'
    usrAddress = "132 North Mulberry St."
    usrPostal = "98059"
    usrCity = "Portland"
    usrPhone = "7378084776"
    usrFname = "G"
    usrLname = "T"
    usrState = "Washington"
    usrCounty = "Seattle"
    usrResume = "functionalsample.pdf"
    ID = "0"
    usrJobs = []

    def __init__(self,ID):
        self.ID = ID

    @classmethod
    def json_init(classInstance,filePath):
            with open(filePath,"r") as file:
                classJson = json.load(file)
            
            return classInstance(classJson["user"])



class Question_Answer:
    ID = 0
    non_binary = False
    question = [""]
    answer = "y"
    #initiate values for the question and answer to be supplied if the question matcher
    def __init__(self,ID,non_binary,question,answer):
        self.ID = ID
        self.non_binary = non_binary
        self.question = question
        self.answer = answer

    @classmethod
    def json_init(classInstance,objData):
            return classInstance(objData["ID"],objData["non_binary"],objData["question"],objData["answer"])



def importUsrInfo(filePath):
    
    #usrDataFile = open(filePath)
    #UsrData = json.loads(usrDataFile.read())
    #user = decodeUsr(UsrData)
    with open(filePath,"r") as file:
        usrData = json.load(file)
    #print(user)
    #UsrData = json.loads("./usrDataModel.json",object_hook=lambda d: SimpleNamespace(**d))
    #user = json.loads(UsrData.user)
    #jobs = json.loads(UsrData.jobs)
    #questionAnswers = json.loads(UsrData.questionAnswers)
    #user = usrData["user"]
    #jobs = usrData["jobs"]
    #questionAnswers = usrData["questionAnswers"]
    newUser = User.json_init(filePath)
    #jobs = Question_Answer.json_init(filePath)
    #questionAnswers = Question_Answer.json_init(filePath)
    jobsJson=[usrData["jobs"]]
    questionAnswersJson=[usrData["questionAnswers"]]
    questionAnswerArr=[Question_Answer.json_init(x) for x in questionAnswersJson[0]]
    jobArr=[WorkExp.json_init(x) for x in jobsJson[0]]
    

    return newUser,jobArr,questionAnswerArr


    
    
    return newUser,jobs,questionAnswers

def decodeUsr(UsrData):
    return namedtuple('user',UsrData.keys())(*UsrData.values())

def decodeUsrJobs(UsrData):
    jobsArr = json.loads("./usrDataModel.json",object_hook=lambda d: SimpleNamespace(**d))
    jobs = json.loads(jobsArr,object_hook=lambda d: SimpleNamespace(**d))
    return jobs

def decodeQuestAns(UsrData):
    questionArr = json.loads("./usrDataModel.json",object_hook=lambda d: SimpleNamespace(**d))
    questionAnswers = json.loads(questionArr,object_hook=lambda d: SimpleNamespace(**d))
    return jobs

