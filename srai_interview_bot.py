import time

class InterviewBot:
    def __init__(self):
        self.user_details = {}

    def ask_details(self):
        print("Welcome to the SRAI AI interview bot!")
        self.user_details['name'] = input("Please enter your name: ")
        self.user_details['age'] = input("Please enter your age: ")
        self.user_details['education'] = input("Please enter your education qualification: ")

    def ask_interview_questions(self):
        print("\nLet's start with the interview questions:\n")
        time.sleep(1)
        print(f"Hi {self.user_details['name']}, please answer the following questions:")
        time.sleep(1)
        print("1. Tell me about yourself.")
        self.get_user_response()
        time.sleep(1)
        print("2. What interests you about this position?")
        self.get_user_response()
        time.sleep(1)
        print("3. What relevant experience do you have?")
        self.get_user_response()
        time.sleep(1)
        print("4. How do you handle challenges?")
        self.get_user_response()
        time.sleep(1)
        print("5. Where do you see yourself in 5 years?")
        self.get_user_response()

    def get_user_response(self):
        while True:
            user_response = input("Your response: ")
            if user_response.strip():  # Check if user input is not empty
                print("Thank you for your response.")
                break
            else:
                print("Please provide a valid response.")

    def engage_user(self):
        print("\nDo you have any specific questions you'd like to ask?")
        user_choice = input("Enter 'yes' to ask a question or 'no' to continue: ")
        if user_choice.lower() == 'yes':
            self.ask_question()
        elif user_choice.lower() == 'no':
            print("Let's continue with the interview.")
        else:
            print("Invalid choice. Let's continue with the interview.")

    def ask_question(self):
        print("\nPlease enter your question:")
        user_question = input("Your question: ")
        print(f"\nYou asked: {user_question}")
        print("Thank you for your question. Let me answer that for you.")

        # Simulate answering the question (can be replaced with actual response generation)
        print("\n[Answer]: Thanks for your question. Feel free to ask more questions!")
        self.engage_user()

    def conduct_interview(self):
        self.ask_details()
        self.ask_interview_questions()
        self.engage_user()
        print("\nThank you for the interview. We will get back to you soon!")

if __name__ == "__main__":
    bot = InterviewBot()
    bot.conduct_interview()