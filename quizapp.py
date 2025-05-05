quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
        "answer": "A"
    },
    {
        "question": "2 + 2 = ?",
        "options": ["A. 3", "B. 4", "C. 5", "D. 22"],
        "answer": "B"
    },
    {
        "question": "What color is the sky on a clear day?",
        "options": ["A. Green", "B. Red", "C. Blue", "D. Yellow"],
        "answer": "C"
    },
        {
        "question": "Who won the ICC Cricket World Cup 2019?",
        "options": ["A. India", "B. Australia", "C. England", "D. New Zealand"],
        "answer": "C"
    },
    {
        "question": "Who is known as the 'God of Cricket'?",
        "options": ["A. MS Dhoni", "B. Virat Kohli", "C. Ricky Ponting", "D. Sachin Tendulkar"],
        "answer": "D"
    },
    {
        "question": "How many players are there in a cricket team?",
        "options": ["A. 9", "B. 10", "C. 11", "D. 12"],
        "answer": "C"
    },
    {
        "question": "Which country has won the most ICC Cricket World Cups (50-over format)?",
        "options": ["A. India", "B. Australia", "C. West Indies", "D. Pakistan"],
        "answer": "B"
    },
    {
        "question": "What is the maximum number of overs in a T20 match per team?",
        "options": ["A. 10", "B. 20", "C. 25", "D. 50"],
        "answer": "B"
    }

]

score = 0

for i, q in enumerate(quiz, start=1):
    print("\nQuestion {}: {}".format(i, q["question"]))
    for option in q["options"]:
        print(option)
    
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer was: {}".format(q["answer"]))

print("\nYou got {} out of {} correct.".format(score, len(quiz)))
