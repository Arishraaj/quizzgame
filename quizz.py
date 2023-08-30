class QuizzFunction():
    def __init__(self,quizz_lst):
        self.no=0
        self.score=0
        self.quizz_lst=quizz_lst

    def stillquestion(self):
        if self.no < len(self.quizz_lst):
            print("Next Question\n")
            return True
        else:
            return False
        

    def nxt_quizz(self):
        quizz_qt=self.quizz_lst[self.no]
        self.no+=1
        print(f'Q{self.no}:{quizz_qt.question}\nOptions')
        for option in quizz_qt.options:
            print(option)
        user=input("Answer:")
        while user not in quizz_qt.options:
            user=input("Pls Enter a Valid Answer:")
        self.check_answer(user,quizz_qt.answer)
        
    
    def check_answer(self,user_ans,answer):
        if user_ans==answer:
            self.score+=1
            print("Correct Answer")
        else:
            print("Wrong Answer")
        print(f'Correct Answer :{answer}')
        print(f'Your Current Score :{self.score}/{self.no}')