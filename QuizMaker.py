def stringIsNumber(aString):
    partionByMinusSign = aString.partition("-")
    partionByDecimalPoint = aString.partition(".")
    isNumber = False
    canBeNegative = False
    canBeDecimal = False

    if len(partionByMinusSign) == 3 and len(partionByDecimalPoint) == 3:
        if partionByMinusSign[0] == "":
            canBeNegative = True
        if partionByDecimalPoint[1] == ".":
            canBeDecimal = True

        if canBeNegative:
            partionByMinusSignAndDecimalPoint = partionByMinusSign[2].partition(".")
            if partionByMinusSignAndDecimalPoint[0] == "":
                if partionByMinusSignAndDecimalPoint[2].isdigit():
                    isNumber = True
            elif partionByMinusSignAndDecimalPoint[2] == "":
                if partionByMinusSignAndDecimalPoint[0].isdigit():
                    isNumber = True
            else:
                if partionByMinusSignAndDecimalPoint[0].isdigit() and partionByMinusSignAndDecimalPoint[2].isdigit():
                    isNumber = True
        else:
            if partionByDecimalPoint[0] == "":
                if partionByDecimalPoint[2].isdigit():
                    isNumber = True
            elif partionByDecimalPoint[2] == "":
                if partionByDecimalPoint[0].isdigit():
                    isNumber = True
            else:
                if partionByDecimalPoint[0].isdigit() and partionByDecimalPoint[2].isdigit():
                    isNumber = True

    return isNumber



def getPositiveInteger(promptStatement):
    inputNumber = raw_input(promptStatement + "\n")
        
    while (stringIsNumber(inputNumber) == False) or (float(inputNumber) <= 0 or float(inputNumber)%1 != 0):
        inputNumber = raw_input("Please enter a positive integer.\n")

    return int(float(inputNumber))



def getInputMatchingElementFromList(promptStatement, listOfAcceptableValues):
    inputValue = raw_input(promptStatement + "\n")
    numberOfPossibleValues = len(listOfAcceptableValues)
    
    valid = False
    for index in range(numberOfPossibleValues):
        if stringIsNumber(inputValue) and stringIsNumber(str(listOfAcceptableValues[index])):
            if float(inputValue) == float(listOfAcceptableValues[index]):
                valid = True
        else:
            if inputValue == str(listOfAcceptableValues[index]):
                valid = True
                    
    while valid != True:
        inputValue = raw_input("Please enter an acceptable value.\n")
        
        for index in range(numberOfPossibleValues):
            if stringIsNumber(inputValue) and stringIsNumber(str(listOfAcceptableValues[index])):
                if float(inputValue) == float(listOfAcceptableValues[index]):
                    valid = True
            else:
                if inputValue == str(listOfAcceptableValues[index]):
                    valid = True

    return inputValue




def getInputMatchingElementFromListIgnoreCase(promptStatement, listOfAcceptableValues):
    inputValue = raw_input(promptStatement + "\n")
    numberOfPossibleValues = len(listOfAcceptableValues)
    
    valid = False
    for index in range(numberOfPossibleValues):
        if stringIsNumber(inputValue) and stringIsNumber(str(listOfAcceptableValues[index])):
            if float(inputValue) == float(listOfAcceptableValues[index]):
                valid = True
        else:
            if inputValue.lower() == str(listOfAcceptableValues[index]).lower():
                valid = True
                    
    while valid != True:
        inputValue = raw_input("Please enter an acceptable value.\n")
        
        for index in range(numberOfPossibleValues):
            if stringIsNumber(inputValue) and stringIsNumber(str(listOfAcceptableValues[index])):
                if float(inputValue) == float(listOfAcceptableValues[index]):
                    valid = True
            else:
                if inputValue.lower() == str(listOfAcceptableValues[index]).lower():
                    valid = True

    return inputValue



def createMultipleChoiceQuestion(questionsFile):
    questionStatement = raw_input("Enter the question statement.\n")
    numberOfChoices = getPositiveInteger("How many choices do you want this question to have?")
    possibleChoices = []

    for count in range(numberOfChoices):
        possibleChoices.append(raw_input("Enter a possible choice.\n"))

    answer = getInputMatchingElementFromList("Enter the correct answer. It must match one of the possible choices. Case and spelling matter.", possibleChoices)
    questionData = "Multiple Choice" + "-------" + questionStatement + "-------" + answer

    for index in range(numberOfChoices):
        questionData = questionData + "-------" + possibleChoices[index]
        
    questionsFile.write(questionData + "\n")



def createTrueOrFalseQuestion(questionsFile):
    questionStatement = raw_input("Enter the statement.\n")
    answer = getInputMatchingElementFromListIgnoreCase("Enter whether the answer is \"True\" or \"False.\"", ["True", "False"])
    
    questionData = "True or False" + "-------" + questionStatement + "-------" + answer
    
    questionsFile.write(questionData + "\n")


    
def createFillInTheBlankQuestion(questionsFile):
    questionStatement = raw_input("Enter the question statement.\n")
    answer = raw_input("Enter the answer to the question. Case and spelling matter.\n")
    questionData = "Fill-in-the-Blank" + "-------" + questionStatement + "-------" + answer

    alternateAnswersPossible = getInputMatchingElementFromListIgnoreCase("Are there alternate answers? Enter \"Yes\" or \"No.\"", ["Yes", "No"])

    if alternateAnswersPossible == "Yes":
        numberOfAlternateAnswers = getPositiveInteger("How many alternate answers are there?")
        for count in range(numberOfAlternateAnswers):
            questionData = questionData + "-------" + raw_input("Enter an acceptable alternate answer.\n")
    
    questionsFile.write(questionData + "\n")


    
print "Welcome to QuizMaker!\n"

fileName = raw_input("Enter the name of your quiz. Do not include the file extension. If you give the name of a text file that already exists in this directory" + \
                      ", it will be deleted and replaced with this quiz.\n")
questionsFile = open(fileName + ".txt", "w")
numberOfQuestions = getPositiveInteger("How many questions do you want your quiz to have?")

for questionNumber in range(numberOfQuestions):
    question = "Question " + \
               str(questionNumber+1) + \
               ": Please enter the capital letter corresponding to the type of question you want." + \
               "\nA. Multiple Choice" + \
               "\nB. True or False" + \
               "\nC. Fill-in-the-Blanks"
    
    questionType = (getInputMatchingElementFromListIgnoreCase(question, ["A", "B", "C"])).upper()

    if questionType == "A":
        createMultipleChoiceQuestion(questionsFile)
    elif questionType == "B":
        createTrueOrFalseQuestion(questionsFile)
    else:
        createFillInTheBlankQuestion(questionsFile)

questionsFile.close()


print "\nYour quiz has been created!\n"

quizLengthInfo = ""
if numberOfQuestions == 1:
    print = "It has " + str(numberOfQuestions) + " question.\n"
else:
    print = "It has " + str(numberOfQuestions) + " questions.\n"

print "Thank you for using QuizMaker!\n"


