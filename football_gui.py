from tkinter import *
from functools import partial  # To prevent unwanted windows


class Choosequestion:

    def __init__(self):
        button_fg = "#FFFFFF"
        button_font = ("Arial", "13", "bold")

        # Set up GUI Frame
        self.intro_frame = Frame(padx=10, pady=10)
        self.intro_frame.grid()

        # heading and brief instructions
        self.intro_heading_label = Label(self.intro_frame, text="Football Quiz",
                                         font=("Arial", "16", "bold"))
        self.intro_heading_label.grid(row=0)

        choose_instructions_txt = "each quiz there will be 4 stadiums to pick from and  " \
                                  "a question stating where does " \
                                  "the certain club plays at\n\n" \

        self.choose_instructions_label = Label(self.intro_frame,
                                               text=choose_instructions_txt,
                                               wraplength=300, justify="left")
        self.choose_instructions_label.grid(row=1)

        # Rounds buttons...
        self.how_many_frame = Frame(self.intro_frame)
        self.how_many_frame.grid(row=2)

        # list to set up questions button.  First item in each
        # sublist is the background color, second item is
        # the number of questions
        btn_color_value = [
            ["#CC0000", 5], ["#009900", 10], ["#000099", 15]
        ]

        for item in range(0, 3):
            self.question_button = Button(self.how_many_frame,
                                        fg=button_fg, bg=btn_color_value[item][0],
                                        text="{} Question".format(btn_color_value[item][1]),
                                        font=button_font, width=10,
                                        command=lambda i=item: self.to_play(btn_color_value[i][1]))
            self.question_button.grid(row=0, column=item,
                                    padx=5, pady=5)

    def to_play(self, num_question):
        Play(num_question)

        # Hide root window (ie: hide questions choice window).
        root.withdraw()


class Play:

    def __init__(self, how_many):
        self.play_box = Toplevel()

        # If users press cross at top, closes help and
        # 'releases' help button
        self.play_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_play))

        self.quiz_frame = Frame(self.play_box, padx=10, pady=10)
        self.quiz_frame.grid()

        rounds_heading = "Choose - Question 1 of {}".format(how_many)
        self.choose_heading = Label(self.quiz_frame, text=rounds_heading,
                                    font=("Arial", "16", "bold")
                                    )
        self.choose_heading.grid(row=0)

        self.control_frame = Frame(self.quiz_frame)
        self.control_frame.grid(row=6)

        self.start_over_button = Button(self.control_frame, text="Start Over",
                                        command=self.close_play)
        self.start_over_button.grid(row=0, column=2)

    def close_play(self):
        # reshow root (ie: choose questions) and end current
        # game / allow new game to start
        root.deiconify()
        self.play_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Football Quiz")
    Choosequestion()
    root.mainloop()