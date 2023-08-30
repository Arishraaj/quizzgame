from data import quizzes
from question import QuizzModel
from quizz import QuizzFunction

quizz_list=[]
for quest in quizzes:
    quizz_question=quest["question"]
    quizz_answer=quest["answer"]
    quizz_option=quest["options"]
    quizz_model=QuizzModel(quizz_question,quizz_answer,quizz_option)
    quizz_list.append(quizz_model)
    # print(quizz_model)

quizz_function=QuizzFunction(quizz_list)

while quizz_function.stillquestion():

    quizz_function.nxt_quizz()

print(f'Your Quizz Completed...')

print(f'Your Final Score :{quizz_function.score}/{len(quizz_function.quizz_lst)}')