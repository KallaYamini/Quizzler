from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain

        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}",
                                 font=("Courier", 20, "bold"),bg=THEME_COLOR,fg= "white")
        self.score_label.grid(row=0,column=1,padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,width=280, text="question 1",font=("Arial",20,"italic"))
        self.canvas.grid(row=1, column=0, columnspan=3,padx=20, pady=20)

        self.true_image = PhotoImage(file="images/true.png")
        self.true_mark =Button(image=self.true_image,highlightthickness=0, command=self.answer_true)
        self.true_mark.grid(row=2, column=0,padx=20, pady=20)

        self.false_image = PhotoImage(file="images/false.png")
        self.false_mark =Button(image=self.false_image,highlightthickness=0, command=self.answer_false)
        self.false_mark.grid(row=2, column=1,padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text= q_text)
        else:
            self.canvas.itemconfig(self.question_text,text= f"You've completed the quiz and Score: {self.quiz.score} / 10")
            self.true_mark["state"] = DISABLED
            self.false_mark["state"] = DISABLED
    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
