class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
question_prompts = [
    "what is 1+1? \n (a) 2\n (b) 3\n (c) 4\n"
]
questions = [
    Question(question_prompts[0], "a")
]
def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got "+str(score) + '/' + str(len(questions)) + " correct")
run_quiz(questions)