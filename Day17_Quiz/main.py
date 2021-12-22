from question_model import Question
from quiz_brain import QuizBrain
import requests

def CreateQuestionBank(n_questions = 10, difficulty = 'Medium'):
	url = "https://opentdb.com/api.php?amount="+n_questions+"&category=9&difficulty="+difficulty.lower()+"&type=boolean"
	source = requests.get(url).json()

	question_bank = []
	for qdict in source["results"]:
		question_bank.append(Question(qdict["question"], qdict["correct_answer"]))
	return question_bank

if __name__ == "__main__":
	# Get quiz questions based on user inputs
	number_of_questions = input("How many questions would you like? ")
	difficulty = input("Select your level of difficulty ('Easy','Medium','Hard'): ")

	quiz = QuizBrain(CreateQuestionBank(number_of_questions, difficulty))
	while quiz.still_has_questions():
		quiz.next_question()

	print(f"Your final score is {quiz.score}/{quiz.question_number}")
