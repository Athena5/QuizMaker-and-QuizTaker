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



def answerMultipleChoiceQuestion(questionData, questionNumber):
    questionStatement = "Question " + str(questionNumber) + ": Multiple Choice\nEnter the capital letter that corresponds to your answer.\n" + questionData[1]
    correctAnswer = questionData[2]
    numberOfPossibleChoices = len(questionData)-3
    possibleChoices = questionData[3:]
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lettersForPossibleChoices = alphabet[:numberOfPossibleChoices]
    answeredCorrectly = False

    for index in range(numberOfPossibleChoices):
        questionStatement = questionStatement + "\n" + lettersForPossibleChoices[index] + ". " + questionData[index+3]
        
    usersAnswer = (getInputMatchingElementFromListIgnoreCase(questionStatement, lettersForPossibleChoices)).upper()
    usersAnswerIndex = lettersForPossibleChoices.index(usersAnswer)
    correctAnswerIndex = possibleChoices.index(correctAnswer)
    return usersAnswerIndex == correctAnswerIndex



def answerTrueOrFalseQuestion(questionData, questionNumber):
    questionStatement = "Question " + str(questionNumber) + ": True or False\nDecide whether the statement is \"True\" or \"False.\"\n" + questionData[1]
    correctAnswer = questionData[2]
    answeredCorrectly = False

    usersAnswer = (getInputMatchingElementFromListIgnoreCase(questionStatement, ["True", "False"])).lower()
    return usersAnswer == str(correctAnswer).lower()



def answerFillInTheBlankQuestion(questionData, questionNumber):
    questionStatement = "Question " + str(questionNumber) + ": Fill-in-the-Blank\nEnter the answer to the question. Alternate answers may be accepted. Case and spelling matter.\n" + questionData[1]
    correctAnswer = questionData[2]
    acceptableAnswers = questionData[2:]
    answeredCorrectly = False

    usersAnswer = raw_input(questionStatement + "\n")
    for anAcceptableAnswer in acceptableAnswers:
        if stringIsNumber(usersAnswer):
            if float(usersAnswer) == float(anAcceptableAnswer):
                answeredCorrectly = True
        else:
            if str(usersAnswer).lower() == str(anAcceptableAnswer).lower():
                answeredCorrectly = True
                
    return answeredCorrectly



print "Welcome to QuizTaker!\n"

fileName = raw_input("Enter the name of quiz you wish to take. Omit the file extension. It must be located in this directory.\n")
questionsFile = open(fileName + ".txt")
questionLines = questionsFile.read().splitlines()

numberOfQuestions = len(questionLines)
if numberOfQuestions != 0:
    if numberOfQuestions == 1:
        print "There is " + str(numberOfQuestions) + " question in this quiz.\n"
    else:
        print "There are " + str(numberOfQuestions) + " questions in this quiz.\n"
    
    questionsAnsweredCorrectly = 0
    for index in range(numberOfQuestions):
        aLine = questionLines[index]
        questionData = aLine.split("-------")
        questionType = questionData[0]
        userAnsweredCorrectly = False

        if questionType == "Multiple Choice":
            userAnsweredCorrectly = answerMultipleChoiceQuestion(questionData, index+1)
        elif questionType == "True or False":
            userAnsweredCorrectly = answerTrueOrFalseQuestion(questionData, index+1)
        elif questionType == "Fill-in-the-Blank":
            userAnsweredCorrectly = answerFillInTheBlankQuestion(questionData, index+1)

        if userAnsweredCorrectly:
            questionsAnsweredCorrectly += 1

    percentScore = float(questionsAnsweredCorrectly)/numberOfQuestions
    if questionsAnsweredCorrectly == 1:
        scoreStatement = "\nYou got " + str(questionsAnsweredCorrectly) + " question correct out of " + str(numberOfQuestions) + "."
    else:
        scoreStatement = "\nYou got " + str(questionsAnsweredCorrectly) + " questions correct out of " + str(numberOfQuestions) + "."
    gradeStatement = ""
    comment = ""

    if percentScore >= 0.9:
        if percentScore >= 0.97:
            gradeStatement = "Your Grade: A+"
        elif  percentScore >= 0.93:
            gradeStatement = "Your Grade: A"
        else:
            gradeStatement = "Your Grade: A-"
        comment = "Excellent!\n"
    elif percentScore >= 0.8:
        if percentScore >= 0.87:
            gradeStatement = "Your Grade: B+"
        elif  percentScore >= 0.83:
            gradeStatement = "Your Grade: B"
        else:
            gradeStatement = "Your Grade: B-"
        comment = "Not bad.\n"
    elif percentScore >= 0.7:
        if percentScore >= 0.77:
            gradeStatement = "Your Grade: C+"
        elif  percentScore >= 0.73:
            gradeStatement = "Your Grade: C"
        else:
            gradeStatement = "Your Grade: C-"
        comment = "You can do better.\n"
    elif percentScore >= 0.6:
        if percentScore >= 0.67:
            gradeStatement =  "Your Grade: D+"
        elif  percentScore >= 0.63:
            gradeStatement =  "Your Grade: D"
        else:
            gradeStatement =  "Your Grade: D-"
        comment = "You'll need help...\n"
    else:
        gradeStatement =  "Your Grade: F"
        comment = "Are you a monkey?\n"

    print scoreStatement
    print gradeStatement
    print comment

    print "Thank you for taking this quiz!\n"
else:
    print "\nThis quiz has no questions.\n"

questionsFile.close()
