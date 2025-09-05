import time as t
import random

#make question
def create_q(max_num):
    operations= ("+","-","*","/")
    a=random.randint(1,max_num)
    b=random.randint(1,max_num)
    op=random.choice(operations)
    #store the question in a variable
    result =eval((f"{a}{op}{b}"))
    return result

def ask_q(numofquestion):
    print("Current score: 0")
    score=0 
    i=0
    while i<numofquestion:
        try:
            answer= eval(input(result))
            if answer == result:
                i=+ 1
                score=+1
                print(f"Correct answer: {score}")
            else:
                print("Incorrect! ")
        except ValueError:
            print("enter a number")

choice = input("Choose your difficulty: 1)Easy 2)Medium 3)Hard").lower()
if choice == "1":
    create_q(10)
    ask_q(5)

if choice == "2":
    create_q(20)
    ask_q(10)

if choice == "3":
    create_q(50)
    ask_q(15)
