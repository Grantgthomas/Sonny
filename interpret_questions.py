from selenium.webdriver.common.keys import Keys


ageQ =["you","18"]
previousInterviewQ = ["interviewed","for","position"]
workedContractQ = ["worked","as","contractor"]
legalAuthQ = ["authorized","united","states"]
reqVisaQ = ["require","sponsorship","visa"]
performDutiesQ = ["perform","essential","duties"]


possible_questions = {
                        "ageQ": ageQ,
                        "previousInterviewQ": previousInterviewQ,
                        "workedContractQ":workedContractQ,
                        "legalAuthQ":legalAuthQ,
                        "reqVisaQ":reqVisaQ,
                        "performDutiesQ":performDutiesQ,
                      }

question_answers = {
                        "ageQ": "y",
                        "previousInterviewQ": "n",
                        "workedContractQ":"n",
                        "legalAuthQ":"n",
                        "reqVisaQ":"n",
                        "performDutiesQ":"y"
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
