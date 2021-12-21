from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

def CreateQuestionBank():
	question_bank = []
	for qdict in question_data:
		question_bank.append(Question(qdict["text"], qdict["answer"]))
	return question_bank

quiz = QuizBrain(CreateQuestionBank())
while quiz.still_has_questions():
	quiz.next_question()

print(f"Your final score is {quiz.score}/{quiz.question_number}")
