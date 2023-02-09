from selenium.webdriver.common.keys import Keys
import time
import string


#
possible_questions = {
                        #"ageQ": ["you","18"],
                        #"previousInterviewQ": ["interviewed","for","position"],
                        #"workedContractQ":["worked","as","contractor"],
                        #"legalAuthQ":["authorized","united","states"],
                        #"reqVisaQ":["require","sponsorship","visa"],
                        #"performDutiesQ":["perform","essential","duties"],
                        #"previousEmployeeQ":["worked","for"],
                        #"felonyQ":["convicted","of","felony"],
                        #"spanishFluentQ":["fluent","in","spanish"],
                        #"backgroundCheckQ":["submit","background","check"],
                        #"drugTestQ":["submit","drug","test"],
                        #"relationshipQ":["in","relationship","employed"],
                        #"sexOrientationQ":["sexual","orientation"]
                      }

#name and answer field
question_answers = {
                        #"ageQ": "y",
                        #"previousInterviewQ": "n",
                        #"workedContractQ":"n",
                        #"legalAuthQ":"n",
                        #"reqVisaQ":"n",
                        #"performDutiesQ":"y",
                        #"previousEmployeeQ":"n",
                        #"felonyQ":"n",
                        #"spanishFluentQ":"n",
                        #"backgroundCheckQ":"y",
                        #"drugTestQ":"y",
                        #"relationshipQ":"n",
                        #"sexOrientationQ":"i"
                    }

#contains name and question field
#this will need to become a dictionary of array and string (key)


imported_questions = {
    "_demo":["_demo"]
}

imported_answers = {
    "_demo":"_n"
}

def getImports(questions):
    for q in questions:
            imported_questions.update({q.name:q.question})
            imported_answers.update({q.name:q.answer})
    
    return imported_questions,imported_answers



def checkQuestions(aria_string):
    for question in possible_questions:
        if matchQuestion(aria_string,possible_questions[question]):
            return question

def answerCheckbox(boxOptions):
    # answer the last checkbox 
    try: 
        answerBox = boxOptions[len(boxOptions)-1]
        answerBox.click()
    except:
        print("unable to click checkbox")

#clean the word from the question

def matchQuestion(aria_string,possible_question):
    words_list = aria_string.split()
    word_index = 0
    for word in words_list:
        if cleanWord(word.lower()) == possible_question[word_index]:
            word_index += 1
            if word_index == len(possible_question):
                return True
    return False

def cleanWord(word):
    punctuation = string.punctuation
    
    # Removing the punctuation characters from the input string
    cleaned = "".join(char for char in word if char not in punctuation)
    
    return cleaned

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