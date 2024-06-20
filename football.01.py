import tkinter as tk
from tkinter import messagebox, Toplevel, Frame, Label, Button
from functools import partial

# Quiz data: Each tuple contains the question and a list of answer options, with the correct answer first
import random

quiz_data = [
    ("What stadium do Manchester United play at?", ["Old Trafford", "Anfield", "London Stadium", "Villa Park"]),
    ("What stadium do Liverpool play at?", ["Anfield", "Old Trafford", "London Stadium", "Villa Park"]),
    ("What stadium do West Ham United play at?", ["London Stadium", "Old Trafford", "Anfield", "Villa Park"]),
    ("What stadium do Aston Villa play at?", ["Villa Park", "Old Trafford", "Anfield", "London Stadium"]),
    ("What stadium do Chelsea play at?", ["Stamford Bridge", "Old Trafford", "Anfield", "Villa Park"]),
    ("What stadium do Arsenal play at?", ["Emirates Stadium", "Old Trafford", "Anfield", "Villa Park"]),
    ("What stadium do Manchester City play at?", ["Etihad Stadium", "Old Trafford", "Anfield", "Villa Park"]),
    ("What stadium do Tottenham Hotspur play at?", ["Tottenham Hotspur Stadium", "Old Trafford", "Anfield", "Villa Park"]),
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

random.shuffle(quiz_data)

# Print shuffled data to verify
for question in quiz_data:
    print(question)




import csv

def get_all_stadiums(self):
   file = open("00_stadium_list.csv", "r")
   var_all_stadiums = list(csv.reader(file, delimiter=","))
   file.close()

   # removes first entry in list (ie: the header row).
   var_all_stadiums.pop(0)
   return var_all_stadiums
class DisplayHelp:
    def __init__(self, partner):
        # setup dialogue box and background colour
        background = "#ffe6cc"
        self.help_box = Toplevel()

        # disable help button
        partner.to_help_button.config(state=tk.DISABLED)

        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=300, height=200, bg=background)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame, bg=background, text="Help / Info", font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = "Your goal in this quiz to test your knowledge on how well you know football stadiums in England. You will get to pick 4 stadium names that goes with question provided."
        self.help_text_label = Label(self.help_frame, bg=background, text=help_text, wrap=350, justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame, font=("Arial", "12", "bold"), text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF", command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

    # closes help dialogue (used by button and x at top of dialogue)
    def close_help(self, partner):
        # Put help button back to normal...
        partner.to_help_button.config(state=tk.NORMAL)
        self.help_box.destroy()

class QuizApp:
    def __init__(self, root, questions):
        self.root = root
        self.questions = questions
        self.current_question = 0
        self.score = 0

        self.root.title("Football Stadium Quiz")
        self.root.geometry("500x400")
        self.root.configure(bg="white")

        # Title Frame
        title_frame = tk.Frame(root, bg="white")
        title_frame.pack(pady=5)

        # Create the title label
        self.title_label = tk.Label(title_frame, text="In game quiz", font=("Arial", 14), bg="white")
        self.title_label.pack()

        # Create question label
        self.question_label = tk.Label(root, text="", font=("Arial", 16), bg="black", fg="white", wraplength=400, justify="center")
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
        score_window = Toplevel(self.root)
        score_window.title("Quiz Completed")

        score_frame = Frame(score_window, bg="lightblue", bd=2, relief="solid")
        score_frame.pack(pady=20, padx=20)

        score_label = Label(score_frame, text=f"{self.score}/{len(self.questions)}", font=("Arial", 40), bg="lightblue")
        score_label.pack(padx=10, pady=10)

        exit_button = Button(score_frame, text="Exit", font=("Arial", 14), bg="#FF3333", fg="white", command=self.root.quit)
        exit_button.pack(pady=10)

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

        instructions_label = tk.Label(self.root, text="Each quiz will have 4 stadiums to pick from and a question stating where does the certain club plays at", wraplength=300, justify="center")
        instructions_label.pack(pady=5)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        self.to_help_button = tk.Button(button_frame, text="Help/Hints", font=("Arial", 12, "bold"), bg="#009900", fg="white", command=self.show_help)
        self.to_help_button.grid(row=0, column=0, padx=10, pady=5)

        start_button = tk.Button(button_frame, text="Start Quiz", font=("Arial", 12, "bold"), bg="#0000FF", fg="white", command=self.create_question_selection_screen)
        start_button.grid(row=0, column=1, padx=10, pady=5)

        exit_button = tk.Button(button_frame, text="Exit Quiz", font=("Arial", 12, "bold"), bg="#FF3333", fg="white", command=self.exit_quiz)
        exit_button.grid(row=0, column=2, padx=10, pady=5)

    def create_question_selection_screen(self):
        self.clear_window()

        title_label = tk.Label(self.root, text="Football Stadium Quiz", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        label = tk.Label(self.root, text="Please pick the number of quiz questions below:", wraplength=300, justify="center")
        label.pack(pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        five_q_button = tk.Button(button_frame, text="5 Questions", font=("Arial", 12, "bold"), bg="#009900", fg="white", command=lambda: self.start_quiz(5))
        five_q_button.grid(row=0, column=0, padx=10, pady=5)

        ten_q_button = tk.Button(button_frame, text="10 Questions", font=("Arial", 12, "bold"), bg="#0000FF", fg="white", command=lambda: self.start_quiz(10))
        ten_q_button.grid(row=0, column=1, padx=10, pady=5)

        twenty_q_button = tk.Button(button_frame, text="20 Questions", font=("Arial", 12, "bold"), bg="#FF3333", fg="white", command=lambda: self.start_quiz(20))
        twenty_q_button.grid(row=0, column=2, padx=10, pady=5)

        home_button = tk.Button(button_frame, text="Home", font=("Arial", 12, "bold"), bg="#FF3399", fg="white", command=self.create_main_menu)
        home_button.grid(row=1, column=1, padx=10, pady=5)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_help(self):
        DisplayHelp(self)

    def start_quiz(self, num_questions):
        self.clear_window()
        QuizApp(self.root, quiz_data[:num_questions])

    def exit_quiz(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = FootballStadiumQuizApp(root)
    root.mainloop()