import tkinter as tk
from tkinter import messagebox


class FootballStadiumQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Football Quiz")
        self.root.geometry("500x300")

        self.questions = [
            {"question": "Which stadium is the home of Manchester United?",
             "options": ["Anfield", "Old Trafford", "Emirates Stadium", "Stamford Bridge"], "answer": 1},
            {"question": "What is the capacity of Wembley Stadium?",
             "options": ["80,000", "85,000", "90,000", "95,000"], "answer": 2},
            {"question": "Which club plays at Stamford Bridge?",
             "options": ["Arsenal FC", "Manchester City", "Chelsea FC", "Tottenham Hotspur"], "answer": 2},
            {"question": "Where is Anfield located?", "options": ["Manchester", "London", "Liverpool", "Newcastle"],
             "answer": 2},
            {"question": "Which stadium has the highest capacity?",
             "options": ["Old Trafford", "Anfield", "Stamford Bridge", "Wembley Stadium"], "answer": 3},
            {"question": "Which stadium is known as the 'Theatre of Dreams'?",
             "options": ["Anfield", "Old Trafford", "Emirates Stadium", "Stamford Bridge"], "answer": 1},
            {"question": "Which stadium is located in Birmingham?",
             "options": ["Villa Park", "St James' Park", "Goodison Park", "Etihad Stadium"], "answer": 0},
            {"question": "What is the capacity of Old Trafford?", "options": ["70,000", "74,140", "80,000", "90,000"],
             "answer": 1},
            {"question": "Which club plays at Goodison Park?",
             "options": ["Liverpool FC", "Everton FC", "Manchester City", "Tottenham Hotspur"], "answer": 1},
            {"question": "Which stadium is located in Newcastle?",
             "options": ["Villa Park", "St James' Park", "Goodison Park", "Etihad Stadium"], "answer": 1},
        ]

        self.num_questions = 0
        self.current_question = 0
        self.score = 0
        self.user_answer = tk.IntVar()

        self.create_main_menu()

    def create_main_menu(self):
        self.clear_window()

        title_label = tk.Label(self.root, text="Football Quiz", font=("Helvetica", 20, "bold"))
        title_label.pack(pady=10)

        instructions_label = tk.Label(self.root,
                                      text="In each question there will be 4 stadiums to choose from, pick on how many questions you are wanting to play",
                                      wraplength=450, justify="center")
        instructions_label.pack(pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)

        button_5 = tk.Button(button_frame, text="5 Questions", font=("Helvetica", 14), bg="red", fg="white",
                             command=lambda: self.start_quiz(5))
        button_5.grid(row=0, column=0, padx=10)

        button_10 = tk.Button(button_frame, text="10 Questions", font=("Helvetica", 14), bg="green", fg="white",
                              command=lambda: self.start_quiz(10))
        button_10.grid(row=0, column=1, padx=10)

        button_15 = tk.Button(button_frame, text="15 Questions", font=("Helvetica", 14), bg="blue", fg="white",
                              command=lambda: self.start_quiz(15))
        button_15.grid(row=0, column=2, padx=10)

    def start_quiz(self, num_questions):
        self.num_questions = num_questions
        self.current_question = 0
        self.score = 0
        self.user_answer.set(-1)
        self.show_question()

    def show_question(self):
        self.clear_window()

        if self.current_question < self.num_questions:
            question = self.questions[self.current_question]

            self.question_label = tk.Label(self.root, text=question["question"], wraplength=450, font=("Helvetica", 16))
            self.question_label.pack(pady=20)

            self.options_frame = tk.Frame(self.root)
            self.options_frame.pack(pady=10)

            self.options = []
            for i in range(4):
                rb = tk.Radiobutton(self.options_frame, text=question["options"][i], variable=self.user_answer, value=i,
                                    font=("Helvetica", 14))
                rb.pack(anchor="w")
                self.options.append(rb)

            self.next_button = tk.Button(self.root, text="Next", command=self.next_question, font=("Helvetica", 14))
            self.next_button.pack(pady=20)
        else:
            self.show_results()

    def next_question(self):
        if self.user_answer.get() == self.questions[self.current_question]["answer"]:
            self.score += 1

        self.current_question += 1
        self.user_answer.set(-1)
        self.show_question()

    def show_results(self):
        self.clear_window()

        result_text = f"Your final score is {self.score} out of {self.num_questions}."
        result_label = tk.Label(self.root, text=result_text, font=("Helvetica", 16))
        result_label.pack(pady=20)

        restart_button = tk.Button(self.root, text="Restart", command=self.create_main_menu, font=("Helvetica", 14))
        restart_button.pack(pady=20)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = FootballStadiumQuiz(root)
    root.mainloop()
