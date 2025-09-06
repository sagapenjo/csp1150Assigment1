import time as t
import random

# Make question
def create_q(max_num, numofquestion):
    operations = ("+", "-")  # Write as string and use eval() later
    a = random.randint(1, max_num)
    b = random.randint(1, max_num)
    op = random.choice(operations)
    # Store the question in a variable
    result = f"{a}{op}{b} "
    return result

def ask_q(max_num, numofquestion):
    print("Current score: 0")
    score = 0
    i = 0  # Control the number of displayed questions
    total_time = 0  # To accumulate elapsed time
    correct = 0
    while i < numofquestion:
        try:
            start_time = t.time()  # Start counting time
            question = create_q(max_num, numofquestion)
            correct_ans = eval(question)  # Eval evaluates the operation
            user_ans = int(input(question))
            end_time = t.time()  # End counting time
            elapsed_time = end_time - start_time  # Calculate elapsed time
            total_time += elapsed_time  # Add to total time

            if user_ans == correct_ans:
                correct += 1
                points = 10 - int(elapsed_time)  # Points for this question
                score += points
                i += 1
                print(f"Correct answer! You took {round(elapsed_time, 2)} seconds, Points awarded: {points}")
            else:
                i += 1
                print(f"Incorrect! Points awarded: 0")

        except ValueError:
            end_time = t.time()  # End counting time for invalid input
            elapsed_time = end_time - start_time  # Calculate elapsed time
            total_time += elapsed_time  # Add to total time
            i += 1
            print("Enter a number!! Points awarded: 0")

    average_time = total_time / numofquestion if numofquestion > 0 else 0  # Calculate average time
    percentage = (correct / numofquestion) * 100 if numofquestion > 0 else 0

    print(f"""Quiz over! 
Your total score was: {score}
You answered {percentage}% of the questions correctly
Your average response time was: {round(average_time, 2)}s""")

print("--------------------------------------Welcome to the (not so) ULTIMATE math quiz--------------------------------------")
while True:
    choice = input("Choose difficulty (1=Easy, 2=Medium, 3=Hard): ").lower()
    try:
        if choice in ("1", "easy"):
            ask_q(10, 5)
            break
        elif choice in ("2", "medium"):
            ask_q(20, 10)
            break
        elif choice in ("3", "hard"):
            ask_q(50, 15)
            break
        print("Invalid difficulty!")
    except ValueError:
        print("Invalid difficulty!")