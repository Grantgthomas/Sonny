import json
from types import SimpleNamespace
from collections import namedtuple
import csv

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


def importSites(args):
    siteFile = args.a
    sites = []
    sites = readFile(siteFile)
    return sites



def readFile(file):
    rows =[]
    with open(file,newline='') as addrs:
        addReader = csv.reader(addrs, delimiter=' ')
        for row in addReader:
            rows.append(row)
    return rows



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
    


    def __init__(self,usrEmail,usrPass,usrAddress,usrCity,usrPostal,usrPhone,usrFname,usrLname,usrState,usrCounty):
        self.usrEmail = usrEmail
        self.usrPass = usrPass
        self.usrAddress = usrAddress
        self.usrCity = usrCity
        self.usrPostal = usrPostal
        self.usrPhone = usrPhone
        self.usrFname = usrFname
        self.usrLname = usrLname
        self.usrState = usrState
        self.usrCounty = usrCounty

    @classmethod
    def json_init(classInstance,objData):
           
            return classInstance(objData["usrEmail"],objData["usrPass"],objData["usrAddress"],objData["usrCity"],objData["usrPostal"],objData["usrPhone"],objData["usrFname"],objData["usrLname"],objData["usrState"],objData["usrCounty"])



class Question_Answer:
    ID = 0
    non_binary = False
    question = [""]
    answer = "y"
    name = "Q"
    #initiate values for the question and answer to be supplied if the question matcher
    def __init__(self,ID,non_binary,question,answer,name):
        self.ID = ID
        self.non_binary = non_binary
        self.question = question
        self.answer = answer
        self.name = name

    @classmethod
    def json_init(classInstance,objData):
            return classInstance(objData["ID"],objData["non_binary"],objData["question"],objData["answer"],objData["name"])



def importUsrInfo(filePath):
    with open(filePath,"r") as file:
        usrData = json.load(file)
    newUser = User.json_init(usrData["user"])
    jobsJson=[usrData["jobs"]]
    questionAnswersJson=[usrData["questionAnswers"]]
    questionAnswerArr=[Question_Answer.json_init(x) for x in questionAnswersJson[0]]
    jobArr=[WorkExp.json_init(x) for x in jobsJson[0]]
    

    return newUser,jobArr,questionAnswerArr


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



