import random

questions = [
    {
        "prompt": "1 + 1",
        "options": ["A. 1", "B. 2", "C. 3", "D. 4"],
        "answer": "B",
        "type": "multiple_choice"
    },
    {
        "prompt": "Is the sky blue? (True/False)",
        "answer": "True",
        "type": "true_false"
    },
    {
        "prompt": "What is the capital of France?",
        "answer": "Paris",
        "type": "fill_in_the_blank"
    },
]

def run_quiz(questions):
    score = 0
    incorrect_questions = []
    
    random.shuffle(questions)

    for index, question in enumerate(questions):
        print(f"Question {index + 1}: {question['prompt']}")
        
        if question['type'] == "multiple_choice":
            for option in question["options"]:
                print(option)
            answer = input("Enter your answer (A, B, C, D): ")
        elif question['type'] == "true_false":
            answer = input("Enter your answer (True/False): ")
        elif question['type'] == "fill_in_the_blank":
            answer = input("Your answer: ")

        if answer.strip().lower() == question["answer"].strip().lower():
            print("Correct!")
            score += 1
        else:
            print("Wrong, the correct answer was", question["answer"])
            incorrect_questions.append(question['prompt'])

    print(f"Total score is {score} out of {len(questions)} questions correct.")
    if incorrect_questions:
        print("You got the following questions wrong:")
        for q in incorrect_questions:
            print(f"- {q}")

run_quiz(questions)
