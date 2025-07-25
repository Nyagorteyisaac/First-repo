import random
import os

def ask_questions():
    questions = {
        "name": "What is your name? ",
        "age": "How old are you? ",
        "color": "What is your favorite color? ",
        "food": "What is your favorite food? ",
        "city": "Which city do you live in? ",
        "shs": "Which SHS did you attend? ",
        "team": "What is your favorite soccer team? "
    }

    # Randomize order of questions
    keys = list(questions.keys())
    random.shuffle(keys)

    answers = {}
    for key in keys:
        answers[key] = input(questions[key])

    return answers

def create_summary(data):
    return (
        f"\nHello, {data['name']}!\n"
        f"You are {data['age']} years old, love the color {data['color']}, and enjoy eating {data['food']}.\n"
        f"Life must be awesome in {data['city']}!\n"
        f"It must have been great attending {data['shs']}.\n"
        f"Go {data['team']}!\n"
    )

def save_to_file(data, summary, rating):
    filename = f"{data['name'].capitalize()}.txt"
    with open(filename, "w") as f:
        f.write(summary)
        f.write(f"\nUser rating for the assistant: {rating} stars\n")
    print(f"Summary saved to {filename}.")

def main():
    while True:
        user_data = ask_questions()
        summary = create_summary(user_data)
        print("\n--- YOUR PERSONAL SUMMARY ---")
        print(summary)

        save = input("\nWould you like to save this summary to a file? (yes/no): ").lower()
        if save in ["yes", "y"]:
            rating = input("Please rate this assistant (1 to 5 stars): ")
            save_to_file(user_data, summary, rating)

        restart = input("\nWould you like to restart and enter another user's details? (yes/no): ").lower()
        if restart not in ["yes", "y"]:
            print("Goodbye! 👋")
            break

if __name__ == "__main__":
    main()
