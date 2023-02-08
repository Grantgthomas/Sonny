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

#clean the word from the question



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


    #return true if a question posed in an aria string matches question of the class
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