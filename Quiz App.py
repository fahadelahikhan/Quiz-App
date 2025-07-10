import tkinter as tk
from tkinter import messagebox


class SimpleQuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Quiz Application")
        self.master.geometry("400x300")
        self.master.resizable(False, False)

        # Initialize quiz state
        self.question_index = 0
        self.user_score = 0
        self.option_buttons = []

        # Initialize widget attributes
        self.question_label = None
        self.button_frame = None
        self.progress_label = None
        self.restart_btn = None

        # Quiz data - easily customizable
        self.quiz_data = [
            {
                'text': "What is the capital city of France?",
                'choices': ["London", "Madrid", "Paris", "Berlin"],
                'answer': "Paris"
            },
            {
                'text': "Which planet is called the Red Planet?",
                'choices': ["Venus", "Mars", "Jupiter", "Saturn"],
                'answer': "Mars"
            },
            {
                'text': "What is the result of 2 + 2?",
                'choices': ["3", "4", "5", "6"],
                'answer': "4"
            },
            {
                'text': "Which programming language is known as 'Python'?",
                'choices': ["Snake Language", "Python", "Java", "C++"],
                'answer': "Python"
            }
        ]

        self.create_widgets()
        self.display_current_question()

    def create_widgets(self):
        """Create and arrange the main UI components"""
        # Title label
        title_label = tk.Label(
            self.master,
            text="Welcome to the Quiz!",
            font=("Arial", 16, "bold"),
            fg="blue"
        )
        title_label.pack(pady=10)

        # Question display label
        self.question_label = tk.Label(
            self.master,
            text="",
            font=("Arial", 12),
            wraplength=350,
            justify="center"
        )
        self.question_label.pack(pady=20)

        # Frame for answer buttons
        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(pady=10)

        # Progress label
        self.progress_label = tk.Label(
            self.master,
            text="",
            font=("Arial", 10),
            fg="gray"
        )
        self.progress_label.pack(pady=5)

        # Control buttons frame
        control_frame = tk.Frame(self.master)
        control_frame.pack(pady=20)

        # Restart button
        self.restart_btn = tk.Button(
            control_frame,
            text="Restart Quiz",
            command=self.restart_quiz,
            font=("Arial", 10),
            bg="lightblue"
        )
        self.restart_btn.pack(side=tk.LEFT, padx=5)

        # Exit button
        exit_btn = tk.Button(
            control_frame,
            text="Exit",
            command=self.master.quit,
            font=("Arial", 10),
            bg="lightcoral"
        )
        exit_btn.pack(side=tk.LEFT, padx=5)

    def display_current_question(self):
        """Display the current question and its options"""
        if self.question_index < len(self.quiz_data):
            current_quiz = self.quiz_data[self.question_index]

            # Update question text
            self.question_label.config(text=current_quiz['text'])

            # Update progress
            progress_text = f"Question {self.question_index + 1} of {len(self.quiz_data)}"
            self.progress_label.config(text=progress_text)

            # Clear previous buttons
            self.clear_option_buttons()

            # Create new option buttons
            for choice in current_quiz['choices']:
                btn = tk.Button(
                    self.button_frame,
                    text=choice,
                    command=lambda selected=choice: self.handle_answer(selected),
                    font=("Arial", 10),
                    width=15,
                    height=2,
                    bg="lightgreen"
                )
                btn.pack(pady=5, fill="x")
                self.option_buttons.append(btn)
        else:
            self.display_final_results()

    def handle_answer(self, selected_choice):
        """Process the user's answer selection"""
        correct_answer = self.quiz_data[self.question_index]['answer']

        # Check if answer is correct
        if selected_choice == correct_answer:
            self.user_score += 1
            messagebox.showinfo("Correct!", "Well done! That's the right answer.")
        else:
            messagebox.showinfo("Incorrect", f"Sorry, the correct answer is: {correct_answer}")

        # Move to next question
        self.question_index += 1
        self.display_current_question()

    def clear_option_buttons(self):
        """Remove all option buttons from the interface"""
        for button in self.option_buttons:
            button.destroy()
        self.option_buttons.clear()

    def display_final_results(self):
        """Show the final quiz results"""
        self.clear_option_buttons()

        # Calculate percentage
        percentage = (self.user_score / len(self.quiz_data)) * 100

        # Display results
        result_text = f"Quiz Complete!\n\nYour Score: {self.user_score}/{len(self.quiz_data)}\nPercentage: {percentage:.1f}%"

        if percentage >= 80:
            result_text += "\n\nExcellent work! 🎉"
        elif percentage >= 60:
            result_text += "\n\nGood job! 👍"
        else:
            result_text += "\n\nKeep practicing! 📚"

        self.question_label.config(text=result_text)
        self.progress_label.config(text="")

        # Show results in a message box too
        messagebox.showinfo("Quiz Results", result_text)

    def restart_quiz(self):
        """Reset the quiz to start over"""
        self.question_index = 0
        self.user_score = 0
        self.display_current_question()


def main():
    """Main function to run the quiz application"""
    root = tk.Tk()
    SimpleQuizApp(root)  # We don't need to store the app instance
    root.mainloop()


if __name__ == "__main__":
    main()