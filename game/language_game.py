import random
import tkinter as tk
from tkinter import messagebox

# Function to generate a formal language based on difficulty level
def generate_formal_language(difficulty):
    if difficulty == "Easy":
        num_strings = random.randint(3, 5)
        alphabet = ['0', '1']
    elif difficulty == "Medium":
        num_strings = random.randint(4, 6)
        alphabet = ['0', '1', '2']
    elif difficulty == "Hard":
        num_strings = random.randint(5, 7)
        alphabet = ['0', '1', '2', '3']
    else:
        raise ValueError("Invalid difficulty level")

    language = [''.join(random.choices(alphabet, k=random.randint(1, 5))) for _ in range(num_strings)]
    return language

def play_game(difficulty):
    language = generate_formal_language(difficulty)
    num_strings = len(language)
    num_questions = 5
    questions_asked = 0

    def check_string(result):
        nonlocal score, questions_asked, current_string
        if ((current_string in language) and result == "yes") or            ((current_string not in language) and result == "no"):
            output_label.config(text="Correct!")
            score += 1
        else:
            output_label.config(text="Incorrect.")
        questions_asked += 1
        if questions_asked == num_questions:
            yes_button.destroy()
            no_button.destroy()
            try_again_button.pack()
            messagebox.showinfo("Game Over", f"Your score: {score}/{num_questions}")
        else:
            current_string = generate_question_string(language)
            string_var.set(f"String: {current_string}")

    def try_again():
        window.destroy()
        select_difficulty()

    def generate_question_string(language):
        if random.random() < 0.5:
            string = random.choice(language)
        else:
            alphabet = ''.join(set(''.join(language)))
            string = ''.join(random.choices(alphabet, k=random.randint(1, 5)))
        return string

    window = tk.Tk()
    window.title("Language Detective")
    window.geometry("400x200")

    language_str = "Generated Language: " + ", ".join(language)
    language_label = tk.Label(window, text=language_str)
    language_label.pack()

    current_string = generate_question_string(language)
    string_var = tk.StringVar()
    string_var.set(f"String: {current_string}")
    string_label = tk.Label(window, textvariable=string_var)
    string_label.pack()

    question_label = tk.Label(window, text="Does the following string belong to the language?")
    question_label.pack()

    button_frame = tk.Frame(window)
    button_frame.pack()

    yes_button = tk.Button(button_frame, text="Yes", command=lambda: check_string("yes"))
    yes_button.pack(side=tk.LEFT)

    no_button = tk.Button(button_frame, text="No", command=lambda: check_string("no"))
    no_button.pack(side=tk.LEFT)

    output_label = tk.Label(window, text="")
    output_label.pack()

    score = 0
    try_again_button = tk.Button(window, text="Try Again", command=try_again)
    window.mainloop()

def select_difficulty():
    root = tk.Tk()
    root.title("Language Detective")
    root.geometry("300x200")

    def start_game(difficulty):
        root.destroy()
        play_game(difficulty)

    label = tk.Label(root, text="Select Difficulty Level")
    label.pack()

    easy_button = tk.Button(root, text="Easy", command=lambda: start_game("Easy"))
    easy_button.pack()

    medium_button = tk.Button(root, text="Medium", command=lambda: start_game("Medium"))
    medium_button.pack()

    hard_button = tk.Button(root, text="Hard", command=lambda: start_game("Hard"))
    hard_button.pack()

    root.mainloop()

if __name__ == "__main__":
    select_difficulty()
