from selenium.webdriver.common.keys import Keys
import time
from iden import *



ageQ =["you","18"]
previousInterviewQ = ["interviewed","for","position"]
workedContractQ = ["worked","as","contractor"]
previousEmployeeQ = ["worked","for"]
legalAuthQ = ["authorized","united","states"]
reqVisaQ = ["require","sponsorship","visa"]
performDutiesQ = ["perform","essential","duties"]
felonyQ = ["convicted","of","felony"]
spanishFluentQ = ["fluent","in","spanish"]
backgroundCheckQ = ["submit","background","check"]
drugTestQ = ["submit","drug","test"]
relationshipQ = ["in","relationship","employed"]
sexOrientationQ = ["sexual","orientation"]

possible_questions = {
                        "ageQ": ageQ,
                        "previousInterviewQ": previousInterviewQ,
                        "workedContractQ":workedContractQ,
                        "legalAuthQ":legalAuthQ,
                        "reqVisaQ":reqVisaQ,
                        "performDutiesQ":performDutiesQ,
                        "previousEmployeeQ":previousEmployeeQ,
                        "felonyQ":felonyQ,
                        "spanishFluentQ":spanishFluentQ,
                        "backgroundCheckQ":backgroundCheckQ,
                        "drugTestQ":drugTestQ,
                        "relationshipQ":relationshipQ,
                      }

question_answers = {
                        "ageQ": "y",
                        "previousInterviewQ": "n",
                        "workedContractQ":"n",
                        "legalAuthQ":"n",
                        "reqVisaQ":"n",
                        "performDutiesQ":"y",
                        "previousEmployeeQ":"n",
                        "felonyQ":"n",
                        "spanishFluentQ":"n",
                        "backgroundCheckQ":"y",
                        "drugTestQ":"y",
                        "relationshipQ":"n",
                        "sexOrientationQ":"i"
                    }

def checkQuestions(aria_string):
    for question in possible_questions:
        if idenQuestion(aria_string,possible_questions[question]):
            return question
        
def answerCheckbox(boxOptions):
    # answer the last checkbox 
    try: 
        answerBox = boxOptions[len(boxOptions)-1]
        answerBox.click()
    except:
        print("unable to click checkbox")
    



def getQuestions():
    return possible_questions

def getAnswers():
    return question_answers

def answerDropdown(element,answer):
    element.send_keys(answer)
    time.sleep(.5)
    element.send_keys(answer)
    #element.send_keys(Keys.ENTER)
    #element.send_keys(answer)
    #element.send_keys(Keys.ENTER)
    
    #element.click()

#maybe use this class to store answers later instead of map

class workExp:
    jobDescription = "A fun fast paced environment where I performed software development and devOps duties"
    currentJob = True
    dateStarted ="042005"
    dateEnded = "042005"
    jobTitle = "Consultant"
    jobCompany ="Workday"
    jobCountry = "United States"


    def __init__(self,currentJob):
        self.currentJob = currentJob

class usrData:
    #data for application
    usrEmail = "email@gmail.com"
    usrPass = 'Passsssssss123!'
    usrAddress = "132 North Mulberry St."
    usrCity = "Portland"
    usrPostal = "98059"
    usrPhone = "7378084776"
    usrFname = "G"
    usrLname = "T"
    usrState = "Washington"
    usrCounty = "Seattle"
    usrJobs = []

    def __init__(self,usrEmail):
        self.usrEmail = usrEmail
    


class question_answer:
    id = 0
    non_binary = False
    question = [""]
    answer = "y"
    #initiate values for the question and answer to be supplied if the question matcher
    def __init__(self,question,answer,non_binary,id):
        self.non_binary = non_binary
        self.question = question
        self.answer = answer
        self.id = id
    


    #return true if a question posed in an aria string matches question of the class
    def idenQuestion(self,aria_string):
        words_list = aria_string.split()
        word_index = 0
        for word in words_list:
            if word.lower() == self.question[word_index]:
                word_index += 1
                if word_index == len(self.question):
                    return True
        return False   

    def getAnswer(self):
        return self.answer
    
    def getQuestion(self):
        return self.answer
    
    def changeAnswer(self,newAnswer):
        newAnswer = newAnswer.lower()
        if self.non_binary!=True: 
            self.answer = newAnswer
        else:
            if newAnswer == "y":
                self.answer = newAnswer
            elif newAnswer == "n":
                self.answer = newAnswer
            else:
                print("please send a binary answer (y or n)")