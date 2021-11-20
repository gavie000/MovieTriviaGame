from documentation_pkg.romance_qa import romance_question_four, romance_question_one,romance_question_two,romance_question_three, romance_question_five,romance_question_four,romance_question_six #,romance_question_seven,romance_question_eight,romance_question_nine,romance_question_ten

class linkedListRomance:
    def __init__(self,value,nextNode=None):
        self.value = value
        self.nextNode = nextNode

"""Question #1 """
node1 = linkedListRomance(romance_question_one()) 

"""Question #2 """
node2= linkedListRomance(romance_question_two())

"""Question #3 """
node3= linkedListRomance(romance_question_three())

"""Question #4 """
node4= linkedListRomance(romance_question_four())

"""Question #5 """
node5= linkedListRomance(romance_question_five())

"""Question #6 """
node6= linkedListRomance(romance_question_six())

"""Question #7 """
node7= linkedListRomance(romance_question_seven())

"""Question #8 """
node8= linkedListRomance(romance_question_eight())

"""Question #9 """
node9= linkedListRomance(romance_question_nine())

"""Question #10 """
node10= linkedListRomance(romance_question_ten())

"""This links all the questions"""
node1.nextNode = node2 # links 1st questions to the 2nd question
node2.nextNode = node3 #links 2nd question to the 3rd question
node3.nextNode = node4#links 3rd question to the 4th question
node4.nextNode = node5#links 4th question to the 5th question
node5.nextNode = node6#links 5th question to the 6th question
node6.nextNode = node7#links 6th question to the 7th question
node7.nextNode = node8#links 7th question to the 8th question
node8.nextNode = node9#links 8th question to the 9th question
node9.nextNode = node10#links 9th question to the 10th question

currentNode = node1
while True:
    print (currentNode.value, "->",)
    if currentNode.nextNode is None: # see if it isnt a tail node
        print("None")
        break
    currentNode = currentNode.nextNode