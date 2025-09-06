import time as t #importing as t just makes it easier as i can wrtite t.start rather than time.start
import random

#make question
def create_q(max_num,numofquestion):
    while True:
        operations= ("+","-")#write as string and use eval() later
        a=random.randint(1,max_num)
        b=random.randint(1,max_num)
        op=random.choice(operations)
    #store the question in a variable
        result =(f"{a}{op}{b} ")
        return result #no brackets as im not calling a function

def ask_q(max_num,numofquestion):
    print("Current score: 0")
    question=create_q(max_num, numofquestion)
    score=0 
    i=0
    while i<numofquestion:
        try:
            correct_ans = eval(question)
            user_ans = int(input(question))
            if user_ans == correct_ans:
                i= i+ 1
                score= score + 1
                print(f"Correct answer: {score}")
            else:
                print("Incorrect! ")
                break
        except ValueError:
            print("enter a number")

choice = input("Choose your difficulty: 1)Easy 2)Medium 3)Hard").lower()
if choice == "1":
    ask_q(10,5)

if choice == "2":    
    ask_q(20,10)

if choice == "3":
    ask_q(50,15)
