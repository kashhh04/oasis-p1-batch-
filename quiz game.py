import random

# Sample quiz questions and answers
quiz_data = [
    {
        "question": "What is the capital of France?",
        "choices": ["Paris", "London", "Berlin", "Madrid"],
        "correct_answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["Mars", "Jupiter", "Venus", "Mercury"],
        "correct_answer": "Mars"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "choices": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo"],
        "correct_answer": "Leonardo da Vinci"
    }
]

def present_question(question_data):
    print(question_data["question"])
    for i, choice in enumerate(question_data["choices"], start=1):
        print(f"{i}. {choice}")

    user_choice = input("Select your answer (1/2/3/4): ")
    return user_choice

def evaluate_answer(user_choice, correct_answer):
    return user_choice.lower() == correct_answer.lower()

def main():
    print("Welcome to the Quiz Game!")
    print("Answer the following questions by selecting the correct option.")

    score = 0
    total_questions = len(quiz_data)

    random.shuffle(quiz_data)

    for question_data in quiz_data:
        user_choice = present_question(question_data)
        correct_answer = question_data["correct_answer"]

        if evaluate_answer(user_choice, correct_answer):
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}")

    print("\nQuiz completed!")
    print(f"Your score: {score}/{total_questions}")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        main()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    main()

