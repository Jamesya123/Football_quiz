import tkinter as tk
from tkinter import messagebox

# Quiz data: Each tuple contains the question and a list of answer options, with the correct answer first
quiz_data = [
    ("What stadium do Manchester United play at?", ["Old Trafford", "Anfield", "London Stadium", "Villa Park"]),
    ("What stadium do Liverpool play at?", ["Anfield", "Old Trafford", "London Stadium", "Villa Park"]),
    ("What stadium do West Ham United play at?", ["London Stadium", "Old Trafford", "Anfield", "Villa Park"]),
    ("What stadium do Aston Villa play at?", ["Villa Park", "Old Trafford", "Anfield", "London Stadium"]),
    ("What stadium do Chelsea play at?", ["Stamford Bridge", "Old Trafford", "Anfield", "Villa Park"]),
    ("What stadium do Arsenal play at?", ["Emirates Stadium", "Old Trafford", "Anfield", "Villa Park"]),
    ("What stadium do Manchester City play at?", ["Etihad Stadium", "Old Trafford", "Anfield", "Villa Park"]),
    ("What stadium do Tottenham Hotspur play at?",
     ["Tottenham Hotspur Stadium", "Old Trafford", "Anfield", "Villa Park"]),
    ("What stadium do Leicester City play at?", ["King Power Stadium", "Old Trafford", "Anfield", "Villa Park"]),
    ("What stadium do Everton play at?", ["Goodison Park", "Old Trafford", "Anfield", "Villa Park"]),
    ("What stadium do Newcastle United play at?", ["St James' Park", "Old Trafford", "Anfield", "Villa Park"]),
    ("What stadium do Southampton play at?", ["St Mary's Stadium", "Old Trafford", "Anfield", "Villa Park"]),
    ("What stadium do Crystal Palace play at?", ["Selhurst Park", "Old Trafford", "Anfield", "Villa Park"]),
    ("What stadium do Brighton & Hove Albion play at?", ["Amex Stadium", "Old Trafford", "Anfield", "Villa Park"]),
    ("What stadium do Wolverhampton Wanderers play at?", ["Molineux Stadium", "Old Trafford", "Anfield", "Villa Park"]),
    ("What stadium do Burnley play at?", ["Turf Moor", "Old Trafford", "Anfield", "Villa Park"]),
    ("What stadium do Sheffield United play at?", ["Bramall Lane", "Old Trafford", "Anfield", "Villa Park"]),
    ("What stadium do Leeds United play at?", ["Elland Road", "Old Trafford", "Anfield", "Villa Park"]),
    ("What stadium do Fulham play at?", ["Craven Cottage", "Old Trafford", "Anfield", "Villa Park"]),
    ("What stadium do Brentford play at?", ["Gtech Community Stadium", "Old Trafford", "Anfield", "Villa Park"]),
]


class QuizApp:
    def __init__(self, root, questions):
        self.root = root
        self.questions = questions
        self.current_question = 0
        self.score = 0

        self.root.title("EPL Stadium Quiz")
        self.root.geometry("500x400")
        self.root.configure(bg="white")

        # Title Frame
        title_frame = tk.Frame(root, bg="white")
        title_frame.pack(pady=5)

        # Create the title label
        self.title_label = tk.Label(title_frame, text="In game quiz", font=("Arial", 14), bg="white")
        self.title_label.pack()

        # Create question label
        self.question_label = tk.Label(root, text="", font=("Arial", 16), bg="black", fg="white", wraplength=400,
                                       justify="center")
        self.question_label.pack(pady=20)

        # Answer Buttons Frame
        buttons_frame = tk.Frame(root, bg="white")
        buttons_frame.pack(pady=20)

        # Create answer buttons
        self.buttons = []
        for i in range(4):
            btn = tk.Button(buttons_frame, text="", font=("Arial", 14), width=15, height=2, bg="black", fg="white",
                            relief="flat", command=lambda b=i: self.check_answer(b))
            self.buttons.append(btn)

        # Arrange buttons in a grid layout
        self.buttons[0].grid(row=0, column=0, padx=10, pady=5)
        self.buttons[1].grid(row=0, column=1, padx=10, pady=5)
        self.buttons[2].grid(row=1, column=0, padx=10, pady=5)
        self.buttons[3].grid(row=1, column=1, padx=10, pady=5)

        self.load_question()

    def load_question(self):
        if self.current_question < len(self.questions):
            q_text, answers = self.questions[self.current_question]
            self.question_label.config(text=q_text)
            for i, btn in enumerate(self.buttons):
                btn.config(text=answers[i])
        else:
            self.show_score()

    def check_answer(self, btn_index):
        correct_answer = self.questions[self.current_question][1][0]
        chosen_answer = self.buttons[btn_index].cget("text")

        if chosen_answer == correct_answer:
            self.score += 1

        self.current_question += 1
        self.load_question()

    def show_score(self):
        messagebox.showinfo("Quiz Completed", f"Your score: {self.score}/{len(self.questions)}")
        self.root.quit()


class FootballStadiumQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Football Stadium Quiz")
        self.root.geometry("400x200")  # Smaller window size

        self.create_main_menu()

    def create_main_menu(self):
        self.clear_window()

        title_label = tk.Label(self.root, text="Football Stadium Quiz", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        instructions_label = tk.Label(self.root,
                                      text="Each quiz will have 4 stadiums to pick from and a question stating where does the certain club plays at",
                                      wraplength=300, justify="center")
        instructions_label.pack(pady=5)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        help_button = tk.Button(button_frame, text="Help/Hints", font=("Arial", 12, "bold"), bg="#009900", fg="white",
                                command=self.show_help)
        help_button.grid(row=0, column=0, padx=10, pady=5)

        start_button = tk.Button(button_frame, text="Start Quiz", font=("Arial", 12, "bold"), bg="#0000FF", fg="white",
                                 command=self.create_question_selection_screen)
        start_button.grid(row=0, column=1, padx=10, pady=5)

        exit_button = tk.Button(button_frame, text="Exit Quiz", font=("Arial", 12, "bold"), bg="#FF3333", fg="white",
                                command=self.exit_quiz)
        exit_button.grid(row=0, column=2, padx=10, pady=5)

    def create_question_selection_screen(self):
        self.clear_window()

        title_label = tk.Label(self.root, text="Start Quiz Select How Many Questions", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        instructions_label = tk.Label(self.root,
                                      text="In each round there will be 4 stadiums to choose from.\nPick on how many questions you are wanting to play.",
                                      wraplength=300, justify="center")
        instructions_label.pack(pady=5)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        five_questions_button = tk.Button(button_frame, text="5 questions", font=("Arial", 12, "bold"), bg="#009900",
                                          fg="white", command=lambda: self.start_quiz(5))
        five_questions_button.grid(row=0, column=0, padx=10, pady=5)

        ten_questions_button = tk.Button(button_frame, text="10 questions", font=("Arial", 12, "bold"), bg="#0000FF",
                                         fg="white", command=lambda: self.start_quiz(10))
        ten_questions_button.grid(row=0, column=1, padx=10, pady=5)

        fifteen_questions_button = tk.Button(button_frame, text="15 questions", font=("Arial", 12, "bold"),
                                             bg="#FF3333", fg="white", command=lambda: self.start_quiz(15))
        fifteen_questions_button.grid(row=0, column=2, padx=10, pady=5)

    def show_help(self):
        messagebox.showinfo("Help/Hints",
                            "This is a quiz about football stadiums. Select the correct stadium based on the given questions.")

    def start_quiz(self, num_questions):
        messagebox.showinfo("Start Quiz", f"Starting the quiz with {num_questions} questions...")
        self.clear_window()
        selected_questions = quiz_data[:num_questions]
        QuizApp(self.root, selected_questions)

    def exit_quiz(self):
        self.root.quit()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = FootballStadiumQuizApp(root)
    root.mainloop()