import tkinter as tk
from tkinter import messagebox, Toplevel, Frame, Label, Button
from functools import partial
import csv
import random


# Class to display the help window
class DisplayHelp:
    def __init__(self, partner):
        background = "#ffe6cc"
        self.help_box = Toplevel()

        # Disable the help button in the main window
        partner.to_help_button.config(state=tk.DISABLED)

        # Protocol for closing the help window
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Setting up the help window frame
        self.help_frame = Frame(self.help_box, width=300, height=200, bg=background)
        self.help_frame.grid()
        self.help_heading_label = Label(self.help_frame, bg=background, text="Help / Info",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        # Help text content
        help_text = ("Your goal in this quiz is to test your knowledge on how well you know football "
                     "stadiums in England. You will get to pick 4 stadium names that go with the question provided.")

        self.help_text_label = Label(self.help_frame, bg=background, text=help_text, wraplength=350, justify="left")
        self.help_text_label.grid(row=1, padx=10)

        # Dismiss button to close the help window
        self.dismiss_button = Button(self.help_frame, font=("Arial", "12", "bold"), text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF", command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

    def close_help(self, partner):
        # Enable the help button in the main window and destroy the help window
        partner.to_help_button.config(state=tk.NORMAL)
        self.help_box.destroy()


# Class for the quiz functionality
class QuizApp:
    def __init__(self, root, questions):
        self.root = root
        self.questions = questions
        self.current_question = 0
        self.score = 0

        # Configure main window
        self.root.title("Football Stadium Quiz")
        self.root.geometry("500x400")
        self.root.configure(bg="white")

        # Title frame
        title_frame = tk.Frame(root, bg="white")
        title_frame.pack(pady=5)
        self.title_label = tk.Label(title_frame, text="In-game quiz", font=("Arial", 14), bg="white")
        self.title_label.pack()

        # Question label with wraplength
        self.question_label = tk.Label(root, text="", font=("Arial", 16), bg="black", fg="white", wraplength=400,
                                       justify="center")
        self.question_label.pack(pady=20)

        # Buttons frame
        buttons_frame = tk.Frame(root, bg="white")
        buttons_frame.pack(pady=20)

        self.buttons = []
        for i in range(4):
            btn = tk.Button(buttons_frame, text="", font=("Arial", 14), width=22, height=2, bg="black", fg="white",
                            relief="flat", wraplength=150, command=lambda b=i: self.check_answer(b))
            self.buttons.append(btn)

        self.buttons[0].grid(row=0, column=0, padx=10, pady=5)
        self.buttons[1].grid(row=0, column=1, padx=10, pady=5)
        self.buttons[2].grid(row=1, column=0, padx=10, pady=5)
        self.buttons[3].grid(row=1, column=1, padx=10, pady=5)

        self.load_question()

    def load_question(self):
        # Load and display the current question and answers
        if self.current_question < len(self.questions):
            q_text, answers = self.questions[self.current_question]

            # Correct answer is always the first in the list
            self.correct_answer = answers[0]

            # Shuffle the answers displayed to the user
            shuffled_answers = answers[:]
            random.shuffle(shuffled_answers)

            self.question_label.config(text=q_text)
            for i, btn in enumerate(self.buttons):
                btn.config(text=shuffled_answers[i])
        else:
            self.show_score()

    def check_answer(self, btn_index):
        # Check if the selected answer is correct
        chosen_answer = self.buttons[btn_index].cget("text")
        if chosen_answer == self.correct_answer:
            self.score += 1
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", f"Incorrect! The correct answer was {self.correct_answer}.")
        self.current_question += 1
        self.load_question()

    def show_score(self):
        # Show the final score after completing the quiz
        score_window = Toplevel(self.root)
        score_window.title("Quiz Completed")
        score_frame = Frame(score_window, bg="lightblue", bd=2, relief="solid")
        score_frame.pack(pady=20, padx=20)
        score_label = Label(score_frame, text=f"{self.score}/{len(self.questions)}", font=("Arial", 40), bg="lightblue")
        score_label.pack(padx=10, pady=10)
        exit_button = Button(score_frame, text="Exit", font=("Arial", 14), bg="#FF3333", fg="white",
                             command=self.root.quit)
        exit_button.pack(pady=10)


# Main application class to manage the different screens and states of the quiz app
class FootballStadiumQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Football Stadium Quiz")
        self.root.geometry("400x200")
        self.create_main_menu()

    def create_main_menu(self):
        # Main menu screen setup
        self.clear_window()
        title_label = tk.Label(self.root, text="Football Stadium Quiz", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        instructions_label = tk.Label(self.root,
                                      text="Each quiz will have 4 stadiums to pick from and a question stating where does the certain club play at",
                                      wraplength=300, justify="center")
        instructions_label.pack(pady=5)
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        self.to_help_button = tk.Button(button_frame, text="Help/Hints", font=("Arial", 12, "bold"), bg="#009900",
                                        fg="white", command=self.show_help)
        self.to_help_button.grid(row=0, column=0, padx=10, pady=5)
        start_button = tk.Button(button_frame, text="Start Quiz", font=("Arial", 12, "bold"), bg="#0000FF", fg="white",
                                 command=self.create_question_selection_screen)
        start_button.grid(row=0, column=1, padx=10, pady=5)
        exit_button = tk.Button(button_frame, text="Exit Quiz", font=("Arial", 12, "bold"), bg="#FF3333", fg="white",
                                command=self.exit_quiz)
        exit_button.grid(row=0, column=2, padx=10, pady=5)

    def create_question_selection_screen(self):
        # Screen to select the number of questions for the quiz
        self.clear_window()
        title_label = tk.Label(self.root, text="Football Stadium Quiz", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        label = tk.Label(self.root, text="Please pick the number of quiz questions below:", wraplength=300,
                         justify="center")
        label.pack(pady=10)
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        five_q_button = tk.Button(button_frame, text="5 Questions", font=("Arial", 12, "bold"), bg="#009900",
                                  fg="white", command=lambda: self.start_quiz(5))
        five_q_button.grid(row=0, column=0, padx=10, pady=5)
        ten_q_button = tk.Button(button_frame, text="10 Questions", font=("Arial", 12, "bold"), bg="#0000FF",
                                 fg="white", command=lambda: self.start_quiz(10))
        ten_q_button.grid(row=0, column=1, padx=10, pady=5)
        twenty_q_button = tk.Button(button_frame, text="20 Questions", font=("Arial", 12, "bold"), bg="#FF3333",
                                    fg="white", command=lambda: self.start_quiz(20))
        twenty_q_button.grid(row=0, column=2, padx=10, pady=5)
        home_button = tk.Button(button_frame, text="Home", font=("Arial", 12, "bold"), bg="#FF3399", fg="white",
                                command=self.create_main_menu)
        home_button.grid(row=1, column=1, padx=10, pady=5)

    def clear_window(self):
        # Clear all widgets in the current window
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_help(self):
        # Display help window
        DisplayHelp(self)

    def start_quiz(self, num_questions):
        # Start the quiz with the selected number of questions
        self.clear_window()
        questions = self.load_questions_from_csv("EPL_Stadiums.csv", num_questions)
        if questions:
            QuizApp(self.root, questions)
        else:
            messagebox.showerror("Error", "No questions loaded from the CSV file.")

    def exit_quiz(self):
        # Exit the application
        self.root.quit()

    def load_questions_from_csv(self, filename, num_questions):
        # Load questions from the CSV file
        questions = []
        try:
            with open(filename, newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip header row
                all_stadiums = [row for row in reader if len(row) >= 2]
                if len(all_stadiums) < num_questions:
                    num_questions = len(all_stadiums)
                for row in random.sample(all_stadiums, num_questions):
                    question = f"What stadium do {row[0]} play at?"
                    correct_answer = row[1]
                    incorrect_answers = random.sample([ans[1] for ans in all_stadiums if ans[1] != correct_answer], 3)
                    answers = [correct_answer] + incorrect_answers
                    questions.append((question, answers))
                print(f"Loaded {len(questions)} questions.")
        except FileNotFoundError:
            messagebox.showerror("Error", f"File {filename} not found")
        except Exception as e:
            print(f"Error loading questions: {e}")
        return questions


if __name__ == "__main__":
    root = tk.Tk()
    app = FootballStadiumQuizApp(root)
    root.mainloop()
