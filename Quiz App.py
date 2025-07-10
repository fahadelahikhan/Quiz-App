import tkinter as tk
from tkinter import messagebox


class SimpleQuizApp:
    """A simple quiz application using tkinter GUI"""

    def __init__(self, window):
        self.window = window
        self.window.title("Simple Quiz Game")
        self.window.geometry("500x400")
        self.window.resizable(False, False)

        # Quiz state variables
        self.question_index = 0
        self.total_score = 0
        self.quiz_questions = self.load_questions()

        # Initialize GUI element references
        self.counter_label = None
        self.question_label = None
        self.button_frame = None
        self.answer_buttons = []
        self.score_label = None

        # GUI elements
        self.setup_ui()
        self.display_current_question()

    @staticmethod
    def load_questions():
        """Load quiz questions and answers"""
        return [
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
                'text': "What is the largest ocean on Earth?",
                'choices': ["Atlantic", "Indian", "Arctic", "Pacific"],
                'answer': "Pacific"
            },
            {
                'text': "How many days are in a leap year?",
                'choices': ["365", "366", "367", "364"],
                'answer': "366"
            }
        ]

    def setup_ui(self):
        """Create and arrange GUI elements"""
        # Title label
        title_label = tk.Label(
            self.window,
            text="🎯 Simple Quiz Game",
            font=("Arial", 16, "bold"),
            fg="blue"
        )
        title_label.pack(pady=10)

        # Question counter
        self.counter_label = tk.Label(
            self.window,
            text="",
            font=("Arial", 10),
            fg="gray"
        )
        self.counter_label.pack(pady=5)

        # Question display
        self.question_label = tk.Label(
            self.window,
            text="",
            font=("Arial", 12),
            wraplength=450,
            justify="center"
        )
        self.question_label.pack(pady=20)

        # Frame for answer buttons
        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack(pady=10)

        # Store button references
        self.answer_buttons = []

        # Score display
        self.score_label = tk.Label(
            self.window,
            text="Score: 0",
            font=("Arial", 10, "bold"),
            fg="green"
        )
        self.score_label.pack(side="bottom", pady=10)

    def display_current_question(self):
        """Show the current question and answer options"""
        if self.question_index < len(self.quiz_questions):
            # Get current question data
            current_q = self.quiz_questions[self.question_index]

            # Update question counter
            self.counter_label.config(
                text=f"Question {self.question_index + 1} of {len(self.quiz_questions)}"
            )

            # Display question text
            self.question_label.config(text=current_q['text'])

            # Clear previous buttons
            self.clear_answer_buttons()

            # Create new answer buttons
            for choice in current_q['choices']:
                btn = tk.Button(
                    self.button_frame,
                    text=choice,
                    font=("Arial", 10),
                    width=15,
                    height=2,
                    command=lambda selected=choice: self.handle_answer(selected)
                )
                btn.pack(pady=5)
                self.answer_buttons.append(btn)

            # Update score display
            self.score_label.config(text=f"Score: {self.total_score}")
        else:
            self.show_final_results()

    def clear_answer_buttons(self):
        """Remove all answer buttons from the screen"""
        for button in self.answer_buttons:
            button.destroy()
        self.answer_buttons.clear()

    def handle_answer(self, selected_choice):
        """Process the selected answer"""
        correct_answer = self.quiz_questions[self.question_index]['answer']

        # Check if answer is correct
        if selected_choice == correct_answer:
            self.total_score += 1
            messagebox.showinfo("Correct! ✓", f"Great job! The answer is {correct_answer}")
        else:
            messagebox.showinfo("Incorrect ✗", f"Sorry, the correct answer is {correct_answer}")

        # Move to next question
        self.question_index += 1
        self.display_current_question()

    def show_final_results(self):
        """Display final score and offer to restart"""
        # Calculate percentage
        percentage = (self.total_score / len(self.quiz_questions)) * 100

        # Create result message
        result_msg = f"Quiz Complete!\n\n"
        result_msg += f"Final Score: {self.total_score} out of {len(self.quiz_questions)}\n"
        result_msg += f"Percentage: {percentage:.1f}%\n\n"

        # Add performance comment
        if percentage >= 80:
            result_msg += "Excellent work! 🌟"
        elif percentage >= 60:
            result_msg += "Good job! 👍"
        else:
            result_msg += "Keep practicing! 📚"

        # Show result dialog
        play_again = messagebox.askyesno("Quiz Results", result_msg + "\n\nWould you like to play again?")

        if play_again:
            self.restart_quiz()
        else:
            self.window.quit()

    def restart_quiz(self):
        """Reset the quiz to start over"""
        self.question_index = 0
        self.total_score = 0
        self.display_current_question()


def main():
    """Main function to run the quiz application"""
    # Create main window
    root = tk.Tk()

    # Create quiz app instance
    SimpleQuizApp(root)

    # Start the GUI event loop
    root.mainloop()


# Run the application
if __name__ == "__main__":
    main()