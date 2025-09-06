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
    score=0 
    i=0#new variable to control the number of displayed questions
    while i<numofquestion:
        try:
            start_time = t.time()#start countiung time
            question=create_q(max_num, numofquestion)
            correct_ans = eval(question) #eval evaluates the operation intially counted as string
            user_ans = int(input(question))
            
            if user_ans == correct_ans:
                i+= 1
                score+= 1
                print(f"Correct answer: {score}")
                end_time= t.time()#end counting time
                elapsed_time = int(end_time - start_time)#calculate elapsed time
                print(f"You took {round(elapsed_time,2)} seconds")


            
            else:
                i+= 1              
                print(f"Incorrect! Current score {score} ")                
        
        except ValueError:
            print("Enter a number!!")
    
    average_score = (score/numofquestion)
    print(f"""Quiz over! Your score was:  {score}/{numofquestion}
You averaged {average_score}""")#only print after i=numofquestions(Multiline strings are very cool)

choice = input("""Choose your difficulty: 
1)Easy 
2)Medium 
3)Hard 
-->""").lower()

if choice == "1":
    ask_q(10,5)

if choice == "2":    
    ask_q(20,10)

if choice == "3":
    ask_q(50,15)
