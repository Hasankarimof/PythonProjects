from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for entry in question_data:
    text = entry['text']
    answer = entry['answer']
    question_object = Question(text,answer)
    question_bank.append(question_object)
    

for question in question_bank:
    print(question.text, ":", question.answer)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()