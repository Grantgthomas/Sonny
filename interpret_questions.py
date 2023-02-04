from selenium.webdriver.common.keys import Keys




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
                        "previousEmployeeQ":"y",
                        "felonyQ":"n",
                        "spanishFluentQ":"n",
                        "backgroundCheckQ":"y",
                        "drugTestQ":"y",
                        "relationshipQ":"n",
                    }

def checkQuestions(aria_string):
    for question in possible_questions:
        if idenQuestion(aria_string,possible_questions[question]):
            return question
        

def idenQuestion(aria_string,possible_question):
    words_list = aria_string.split()
    word_index = 0
    for word in words_list:
        if word.lower() == possible_question[word_index]:
            word_index += 1
            if word_index == len(possible_question):
                return True
    return False

def getQuestions():
    return possible_questions

def getAnswers():
    return question_answers

def answerDropdown(element,answer):
    element.send_keys(answer)
    element.send_keys(Keys.ENTER)
    element.send_keys(answer)
    element.send_keys(Keys.ENTER)
    #element.click()

#maybe use this class to store answers later instead of map

class question_answer:
    #initiate values for the question and answer to be supplied if the question matcher
    def __init__(self,question,answer,non_binary):
        self.non_binary = non_binary
        self.question = question
        self.answer = answer
    
    non_binary = False
    question = [""]
    answer = "y"

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