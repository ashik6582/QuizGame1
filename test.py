import logging

def setup_logging():
    logging.basicConfig(
        filename="quiz_log.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def get_user_info():
    try:
        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")
        email = input("Enter your email ID: ")
        if not name or not phone or not email:
            raise ValueError("All fields are required!")
        logging.info(f"User Registered: {name}, {phone}, {email}")
        return name, phone, email
    except Exception as e:
        logging.error(f"Error in user input: {e}")
        print("Invalid input, please try again.")
        return get_user_info()

def quiz_game():
    questions = [
        {"question": "What is the capital of France?", "options": ["A. Berlin", "B. Paris", "C. Madrid"], "answer": "B"},
        {"question": "Which planet is known as the Red Planet?", "options": ["A. Earth", "B. Venus", "C. Mars"], "answer": "C"},
        {"question": "What is the largest ocean on Earth?", "options": ["A. Atlantic", "B. Indian", "C. Pacific"], "answer": "C"}
    ]
    
    score = 0
    
    try:
        for i, q in enumerate(questions, start=1):
            print(f"\nQuestion {i}: {q['question']}")
            for opt in q["options"]:
                print(opt)
            
            user_answer = input("Enter your answer (A/B/C): ").strip().upper()
            if user_answer not in ["A", "B", "C"]:
                raise ValueError("Invalid choice! Please enter A, B, or C.")
            
            if user_answer == q["answer"]:
                score += 1
        
        print(f"\nQuiz Over! You got {score}/{len(questions)} correct.")
        logging.info(f"User Score: {score}/{len(questions)}")
    
    except Exception as e:
        logging.error(f"Error during quiz: {e}")
        print("An error occurred during the quiz.")

def main():
    setup_logging()
    print("Welcome to the Quiz Game!")
    name, phone, email = get_user_info()
    quiz_game()
    print("Thank you for playing!")

if __name__ == "__main__":
    main()
